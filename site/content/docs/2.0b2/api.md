---
title: "Python/C API"
weight: 50
---

# Introduction <span id="intro" label="intro"></span>

The Application Programmer’s Interface to Python gives C and C++ programmers access to the Python interpreter at a variety of levels. The API is equally usable from C++, but for brevity it is generally referred to as the Python/C API. There are two fundamentally different reasons for using the Python/C API. The first reason is to write *extension modules* for specific purposes; these are C modules that extend the Python interpreter. This is probably the most common use. The second reason is to use Python as a component in a larger application; this technique is generally referred to as *embedding* Python in an application.

Writing an extension module is a relatively well-understood process, where a “cookbook” approach works well. There are several tools that automate the process to some extent. While people have embedded Python in other applications since its early existence, the process of embedding Python is less straightforward that writing an extension.

Many API functions are useful independent of whether you’re embedding or extending Python; moreover, most applications that embed Python will need to provide a custom extension as well, so it’s probably a good idea to become familiar with writing an extension before attempting to embed Python in a real application.

## Include Files <span id="includes" label="includes"></span>

All function, type and macro definitions needed to use the Python/C API are included in your code by the following line:

    #include "Python.h"

This implies inclusion of the following standard headers: `<stdio.h>`, `<string.h>`, `<errno.h>`, `<limits.h>`, and `<stdlib.h>` (if available).

All user visible names defined by Python.h (except those defined by the included standard headers) have one of the prefixes `Py` or `_Py`. Names beginning with `_Py` are for internal use by the Python implementation and should not be used by extension writers. Structure member names do not have a reserved prefix.

**Important:** user code should never define names that begin with `Py` or `_Py`. This confuses the reader, and jeopardizes the portability of the user code to future Python versions, which may define additional names beginning with one of these prefixes.

The header files are typically installed with Python. On Unix, these are located in the directories `/include/python`*`version`*`/` and `/include/python`*`version`*`/`, where and are defined by the corresponding parameters to Python’s script and *version* is `sys.version[:3]`. On Windows, the headers are installed in `/include`, where is the installation directory specified to the installer.

To include the headers, place both directories (if different) on your compiler’s search path for includes. Do *not* place the parent directories on the search path and then use `#include <python/Python.h>`; this will break on multi-platform builds since the platform independent headers under include the platform specific headers from .

## Objects, Types and Reference Counts <span id="objects" label="objects"></span>

Most Python/C API functions have one or more arguments as well as a return value of type `PyObject*`. This type is a pointer to an opaque data type representing an arbitrary Python object. Since all Python object types are treated the same way by the Python language in most situations (e.g., assignments, scope rules, and argument passing), it is only fitting that they should be represented by a single C type. Almost all Python objects live on the heap: you never declare an automatic or static variable of type `PyObject`, only pointer variables of type `PyObject*` can be declared. The sole exception are the type objects; since these must never be deallocated, they are typically static `PyTypeObject` objects.

All Python objects (even Python integers) have a *type* and a *reference count*. An object’s type determines what kind of object it is (e.g., an integer, a list, or a user-defined function; there are many more as explained in the Python Reference Manual). For each of the well-known types there is a macro to check whether an object is of that type; for instance, `PyList_Check(`*`a`*`)` is true if (and only if) the object pointed to by *a* is a Python list.

### Reference Counts <span id="refcounts" label="refcounts"></span>

The reference count is important because today’s computers have a finite (and often severely limited) memory size; it counts how many different places there are that have a reference to an object. Such a place could be another object, or a global (or static) C variable, or a local variable in some C function. When an object’s reference count becomes zero, the object is deallocated. If it contains references to other objects, their reference count is decremented. Those other objects may be deallocated in turn, if this decrement makes their reference count become zero, and so on. (There’s an obvious problem with objects that reference each other here; for now, the solution is “don’t do that.”)

Reference counts are always manipulated explicitly. The normal way is to use the macro to increment an object’s reference count by one, and to decrement it by one. The macro is considerably more complex than the incref one, since it must check whether the reference count becomes zero and then cause the object’s deallocator to be called. The deallocator is a function pointer contained in the object’s type structure. The type-specific deallocator takes care of decrementing the reference counts for other objects contained in the object if this is a compound object type, such as a list, as well as performing any additional finalization that’s needed. There’s no chance that the reference count can overflow; at least as many bits are used to hold the reference count as there are distinct memory locations in virtual memory (assuming `sizeof(long) >= sizeof(char*)`). Thus, the reference count increment is a simple operation.

It is not necessary to increment an object’s reference count for every local variable that contains a pointer to an object. In theory, the object’s reference count goes up by one when the variable is made to point to it and it goes down by one when the variable goes out of scope. However, these two cancel each other out, so at the end the reference count hasn’t changed. The only real reason to use the reference count is to prevent the object from being deallocated as long as our variable is pointing to it. If we know that there is at least one other reference to the object that lives at least as long as our variable, there is no need to increment the reference count temporarily. An important situation where this arises is in objects that are passed as arguments to C functions in an extension module that are called from Python; the call mechanism guarantees to hold a reference to every argument for the duration of the call.

However, a common pitfall is to extract an object from a list and hold on to it for a while without incrementing its reference count. Some other operation might conceivably remove the object from the list, decrementing its reference count and possible deallocating it. The real danger is that innocent-looking operations may invoke arbitrary Python code which could do this; there is a code path which allows control to flow back to the user from a , so almost any operation is potentially dangerous.

A safe approach is to always use the generic operations (functions whose name begins with `PyObject_`, `PyNumber_`, `PySequence_` or `PyMapping_`). These operations always increment the reference count of the object they return. This leaves the caller with the responsibility to call when they are done with the result; this soon becomes second nature.

#### Reference Count Details <span id="refcountDetails" label="refcountDetails"></span>

The reference count behavior of functions in the Python/C API is best explained in terms of *ownership of references*. Note that we talk of owning references, never of owning objects; objects are always shared! When a function owns a reference, it has to dispose of it properly — either by passing ownership on (usually to its caller) or by calling or . When a function passes ownership of a reference on to its caller, the caller is said to receive a *new* reference. When no ownership is transferred, the caller is said to *borrow* the reference. Nothing needs to be done for a borrowed reference.

Conversely, when a calling function passes it a reference to an object, there are two possibilities: the function *steals* a reference to the object, or it does not. Few functions steal references; the two notable exceptions are and , which steal a reference to the item (but not to the tuple or list into which the item is put!). These functions were designed to steal a reference because of a common idiom for populating a tuple or list with newly created objects; for example, the code to create the tuple `(1, 2, "three")` could look like this (forgetting about error handling for the moment; a better way to code this is shown below):

    PyObject *t;

    t = PyTuple_New(3);
    PyTuple_SetItem(t, 0, PyInt_FromLong(1L));
    PyTuple_SetItem(t, 1, PyInt_FromLong(2L));
    PyTuple_SetItem(t, 2, PyString_FromString("three"));

Incidentally, is the *only* way to set tuple items; and refuse to do this since tuples are an immutable data type. You should only use for tuples that you are creating yourself.

Equivalent code for populating a list can be written using and . Such code can also use ; this illustrates the difference between the two (the extra calls):

    PyObject *l, *x;

    l = PyList_New(3);
    x = PyInt_FromLong(1L);
    PySequence_SetItem(l, 0, x); Py_DECREF(x);
    x = PyInt_FromLong(2L);
    PySequence_SetItem(l, 1, x); Py_DECREF(x);
    x = PyString_FromString("three");
    PySequence_SetItem(l, 2, x); Py_DECREF(x);

You might find it strange that the “recommended” approach takes more code. However, in practice, you will rarely use these ways of creating and populating a tuple or list. There’s a generic function, , that can create most common objects from C values, directed by a *format string*. For example, the above two blocks of code could be replaced by the following (which also takes care of the error checking):

    PyObject *t, *l;

    t = Py_BuildValue("(iis)", 1, 2, "three");
    l = Py_BuildValue("[iis]", 1, 2, "three");

It is much more common to use and friends with items whose references you are only borrowing, like arguments that were passed in to the function you are writing. In that case, their behaviour regarding reference counts is much saner, since you don’t have to increment a reference count so you can give a reference away (“have it be stolen”). For example, this function sets all items of a list (actually, any mutable sequence) to a given item:

    int set_all(PyObject *target, PyObject *item)
    {
        int i, n;

        n = PyObject_Length(target);
        if (n < 0)
            return -1;
        for (i = 0; i < n; i++) {
            if (PyObject_SetItem(target, i, item) < 0)
                return -1;
        }
        return 0;
    }

The situation is slightly different for function return values. While passing a reference to most functions does not change your ownership responsibilities for that reference, many functions that return a referece to an object give you ownership of the reference. The reason is simple: in many cases, the returned object is created on the fly, and the reference you get is the only reference to the object. Therefore, the generic functions that return object references, like and , always return a new reference (i.e., the caller becomes the owner of the reference).

It is important to realize that whether you own a reference returned by a function depends on which function you call only — *the plumage* (i.e., the type of the type of the object passed as an argument to the function) *doesn’t enter into it!* Thus, if you extract an item from a list using , you don’t own the reference — but if you obtain the same item from the same list using (which happens to take exactly the same arguments), you do own a reference to the returned object.

Here is an example of how you could write a function that computes the sum of the items in a list of integers; once using , and once using .

    long sum_list(PyObject *list)
    {
        int i, n;
        long total = 0;
        PyObject *item;

        n = PyList_Size(list);
        if (n < 0)
            return -1; /* Not a list */
        for (i = 0; i < n; i++) {
            item = PyList_GetItem(list, i); /* Can't fail */
            if (!PyInt_Check(item)) continue; /* Skip non-integers */
            total += PyInt_AsLong(item);
        }
        return total;
    }

    long sum_sequence(PyObject *sequence)
    {
        int i, n;
        long total = 0;
        PyObject *item;
        n = PySequence_Length(sequence);
        if (n < 0)
            return -1; /* Has no length */
        for (i = 0; i < n; i++) {
            item = PySequence_GetItem(sequence, i);
            if (item == NULL)
                return -1; /* Not a sequence, or other failure */
            if (PyInt_Check(item))
                total += PyInt_AsLong(item);
            Py_DECREF(item); /* Discard reference ownership */
        }
        return total;
    }

### Types <span id="types" label="types"></span>

There are few other data types that play a significant role in the Python/C API; most are simple C types such as `int`, `long`, `double` and `char*`. A few structure types are used to describe static tables used to list the functions exported by a module or the data attributes of a new object type, and another is used to describe the value of a complex number. These will be discussed together with the functions that use them.

## Exceptions <span id="exceptions" label="exceptions"></span>

The Python programmer only needs to deal with exceptions if specific error handling is required; unhandled exceptions are automatically propagated to the caller, then to the caller’s caller, and so on, until they reach the top-level interpreter, where they are reported to the user accompanied by a stack traceback.

For C programmers, however, error checking always has to be explicit. All functions in the Python/C API can raise exceptions, unless an explicit claim is made otherwise in a function’s documentation. In general, when a function encounters an error, it sets an exception, discards any object references that it owns, and returns an error indicator — usually NULL or `-1`. A few functions return a Boolean true/false result, with false indicating an error. Very few functions return no explicit error indicator or have an ambiguous return value, and require explicit testing for errors with .

Exception state is maintained in per-thread storage (this is equivalent to using global storage in an unthreaded application). A thread can be in one of two states: an exception has occurred, or not. The function can be used to check for this: it returns a borrowed reference to the exception type object when an exception has occurred, and NULL otherwise. There are a number of functions to set the exception state: is the most common (though not the most general) function to set the exception state, and clears the exception state.

The full exception state consists of three objects (all of which can be NULL): the exception type, the corresponding exception value, and the traceback. These have the same meanings as the Python objects `sys.exc_type`, `sys.exc_value`, and `sys.exc_traceback`; however, they are not the same: the Python objects represent the last exception being handled by a Python …  statement, while the C level exception state only exists while an exception is being passed on between C functions until it reaches the Python bytecode interpreter’s main loop, which takes care of transferring it to `sys.exc_type` and friends.

Note that starting with Python 1.5, the preferred, thread-safe way to access the exception state from Python code is to call the function `sys.exc_info()`, which returns the per-thread exception state for Python code. Also, the semantics of both ways to access the exception state have changed so that a function which catches an exception will save and restore its thread’s exception state so as to preserve the exception state of its caller. This prevents common bugs in exception handling code caused by an innocent-looking function overwriting the exception being handled; it also reduces the often unwanted lifetime extension for objects that are referenced by the stack frames in the traceback.

As a general principle, a function that calls another function to perform some task should check whether the called function raised an exception, and if so, pass the exception state on to its caller. It should discard any object references that it owns, and return an error indicator, but it should *not* set another exception — that would overwrite the exception that was just raised, and lose important information about the exact cause of the error.

A simple example of detecting exceptions and passing them on is shown in the example above. It so happens that that example doesn’t need to clean up any owned references when it detects an error. The following example function shows some error cleanup. First, to remind you why you like Python, we show the equivalent Python code:

    def incr_item(dict, key):
        try:
            item = dict[key]
        except KeyError:
            item = 0
        return item + 1

Here is the corresponding C code, in all its glory:

    int incr_item(PyObject *dict, PyObject *key)
    {
        /* Objects all initialized to NULL for Py_XDECREF */
        PyObject *item = NULL, *const_one = NULL, *incremented_item = NULL;
        int rv = -1; /* Return value initialized to -1 (failure) */

        item = PyObject_GetItem(dict, key);
        if (item == NULL) {
            /* Handle KeyError only: */
            if (!PyErr_ExceptionMatches(PyExc_KeyError)) goto error;

            /* Clear the error and use zero: */
            PyErr_Clear();
            item = PyInt_FromLong(0L);
            if (item == NULL) goto error;
        }

        const_one = PyInt_FromLong(1L);
        if (const_one == NULL) goto error;

        incremented_item = PyNumber_Add(item, const_one);
        if (incremented_item == NULL) goto error;

        if (PyObject_SetItem(dict, key, incremented_item) < 0) goto error;
        rv = 0; /* Success */
        /* Continue with cleanup code */

     error:
        /* Cleanup code, shared by success and failure path */

        /* Use Py_XDECREF() to ignore NULL references */
        Py_XDECREF(item);
        Py_XDECREF(const_one);
        Py_XDECREF(incremented_item);

        return rv; /* -1 for error, 0 for success */
    }

This example represents an endorsed use of the statement in C! It illustrates the use of and to handle specific exceptions, and the use of to dispose of owned references that may be NULL (note the in the name; would crash when confronted with a NULL reference). It is important that the variables used to hold owned references are initialized to NULL for this to work; likewise, the proposed return value is initialized to `-1` (failure) and only set to success after the final call made is successful.

## Embedding Python <span id="embedding" label="embedding"></span>

The one important task that only embedders (as opposed to extension writers) of the Python interpreter have to worry about is the initialization, and possibly the finalization, of the Python interpreter. Most functionality of the interpreter can only be used after the interpreter has been initialized.

The basic initialization function is . This initializes the table of loaded modules, and creates the fundamental modules `__builtin__`, `__main__`and `sys`. It also initializes the module search path (`sys.path`). does not set the “script argument list” (`sys.argv`). If this variable is needed by Python code that will be executed later, it must be set explicitly with a call to `PySys_SetArgv(`*`argc`*`, `*`argv`*`)`subsequent to the call to .

On most systems (in particular, on Unix and Windows, although the details are slightly different), calculates the module search path based upon its best guess for the location of the standard Python interpreter executable, assuming that the Python library is found in a fixed location relative to the Python interpreter executable. In particular, it looks for a directory named `lib/python` relative to the parent directory where the executable named `python` is found on the shell command search path (the environment variable ).

For instance, if the Python executable is found in `/usr/local/bin/python`, it will assume that the libraries are in `/usr/local/lib/python`. (In fact, this particular path is also the “fallback” location, used when no executable file named `python` is found along .) The user can override this behavior by setting the environment variable , or insert additional directories in front of the standard path by setting .

The embedding application can steer the search by calling `Py_SetProgramName(`*`file`*`)`*before* calling . Note that still overrides this and is still inserted in front of the standard path. An application that requires total control has to provide its own implementation of , , , and (all defined in `Modules/getpath.c`).

Sometimes, it is desirable to “uninitialize” Python. For instance, the application may want to start over (make another call to ) or the application is simply done with its use of Python and wants to free all memory allocated by Python. This can be accomplished by calling . The function returns true if Python is currently in the initialized state. More information about these functions is given in a later chapter.

# The Very High Level Layer <span id="veryhigh" label="veryhigh"></span>

The functions in this chapter will let you execute Python source code given in a file or a buffer, but they will not let you interact in a more detailed way with the interpreter.

Several of these functions accept a start symbol from the grammar as a parameter. The available start symbols are , , and . These are described following the functions which accept them as parameters.

Note also that several of these functions take `FILE*` parameters. On particular issue which needs to be handled carefully is that the `FILE` structure for different C libraries can be different and incompatible. Under Windows (at least), it is possible for dynamically linked extensions to actually use different libraries, so care should be taken that `FILE*` parameters are only passed to these functions if it is certain that they were created by the same library that the Python runtime is using.

<div class="cfuncdesc">

intPyRun_AnyFileFILE \*fp, char \*filename If *fp* refers to a file associated with an interactive device (console or terminal input or Unix pseudo-terminal), return the value of , otherwise return the result of . If *filename* is NULL, this function uses `"???"` as the filename.

</div>

<div class="cfuncdesc">

intPyRun_SimpleStringchar \*command Executes the Python source code from *command* in the `__main__` module. If `__main__` does not already exist, it is created. Returns `0` on success or `-1` if an exception was raised. If there was an error, there is no way to get the exception information.

</div>

<div class="cfuncdesc">

intPyRun_SimpleFileFILE \*fp, char \*filename Similar to , but the Python source code is read from *fp* instead of an in-memory string. *filename* should be the name of the file.

</div>

<div class="cfuncdesc">

intPyRun_InteractiveOneFILE \*fp, char \*filename Read and execute a single statement from a file associated with an interactive device. If *filename* is NULL, `"???"` is used instead. The user will be prompted using `sys.ps1` and `sys.ps2`. Returns `0` when the input was executed successfully, `-1` if there was an exception, or an error code from the `errcode.h` include file distributed as part of Python in case of a parse error. (Note that `errcode.h` is not included by `Python.h`, so must be included specifically if needed.)

</div>

<div class="cfuncdesc">

intPyRun_InteractiveLoopFILE \*fp, char \*filename Read and execute statements from a file associated with an interactive device until EOF is reached. If *filename* is NULL, `"???"` is used instead. The user will be prompted using `sys.ps1` and `sys.ps2`. Returns `0` at EOF.

</div>

<div class="cfuncdesc">

struct \_node\*PyParser_SimpleParseStringchar \*str, int start Parse Python source code from *str* using the start token *start*. The result can be used to create a code object which can be evaluated efficiently. This is useful if a code fragment must be evaluated many times.

</div>

<div class="cfuncdesc">

struct \_node\*PyParser_SimpleParseFileFILE \*fp, char \*filename, int start Similar to , but the Python source code is read from *fp* instead of an in-memory string. *filename* should be the name of the file.

</div>

<div class="cfuncdesc">

PyObject\*PyRun_Stringchar \*str, int start, PyObject \*globals, PyObject \*locals Execute Python source code from *str* in the context specified by the dictionaries *globals* and *locals*. The parameter *start* specifies the start token that should be used to parse the source code.

Returns the result of executing the code as a Python object, or NULL if an exception was raised.

</div>

<div class="cfuncdesc">

PyObject\*PyRun_FileFILE \*fp, char \*filename, int start, PyObject \*globals, PyObject \*locals Similar to , but the Python source code is read from *fp* instead of an in-memory string. *filename* should be the name of the file.

</div>

<div class="cfuncdesc">

PyObject\*Py_CompileStringchar \*str, char \*filename, int start Parse and compile the Python source code in *str*, returning the resulting code object. The start token is given by *start*; this can be used to constrain the code which can be compiled and should be , , or . The filename specified by *filename* is used to construct the code object and may appear in tracebacks or `SyntaxError` exception messages. This returns NULL if the code cannot be parsed or compiled.

</div>

<div class="cvardesc">

intPy_eval_input The start symbol from the Python grammar for isolated expressions; for use with .

</div>

<div class="cvardesc">

intPy_file_input The start symbol from the Python grammar for sequences of statements as read from a file or other source; for use with . This is the symbol to use when compiling arbitrarily long Python source code.

</div>

<div class="cvardesc">

intPy_single_input The start symbol from the Python grammar for a single statement; for use with . This is the symbol used for the interactive interpreter loop.

</div>

# Reference Counting <span id="countingRefs" label="countingRefs"></span>

The macros in this section are used for managing reference counts of Python objects.

<div class="cfuncdesc">

voidPy_INCREFPyObject \*o Increment the reference count for object *o*. The object must not be NULL; if you aren’t sure that it isn’t NULL, use .

</div>

<div class="cfuncdesc">

voidPy_XINCREFPyObject \*o Increment the reference count for object *o*. The object may be NULL, in which case the macro has no effect.

</div>

<div class="cfuncdesc">

voidPy_DECREFPyObject \*o Decrement the reference count for object *o*. The object must not be NULL; if you aren’t sure that it isn’t NULL, use . If the reference count reaches zero, the object’s type’s deallocation function (which must not be NULL) is invoked.

**Warning:** The deallocation function can cause arbitrary Python code to be invoked (e.g. when a class instance with a `__del__()` method is deallocated). While exceptions in such code are not propagated, the executed code has free access to all Python global variables. This means that any object that is reachable from a global variable should be in a consistent state before is invoked. For example, code to delete an object from a list should copy a reference to the deleted object in a temporary variable, update the list data structure, and then call for the temporary variable.

</div>

<div class="cfuncdesc">

voidPy_XDECREFPyObject \*o Decrement the reference count for object *o*. The object may be NULL, in which case the macro has no effect; otherwise the effect is the same as for , and the same warning applies.

</div>

The following functions or macros are only for use within the interpreter core: , , , as well as the global variable .

# Exception Handling <span id="exceptionHandling" label="exceptionHandling"></span>

The functions described in this chapter will let you handle and raise Python exceptions. It is important to understand some of the basics of Python exception handling. It works somewhat like the Unix variable: there is a global indicator (per thread) of the last error that occurred. Most functions don’t clear this on success, but will set it to indicate the cause of the error on failure. Most functions also return an error indicator, usually NULL if they are supposed to return a pointer, or `-1` if they return an integer (exception: the functions return `1` for success and `0` for failure). When a function must fail because some function it called failed, it generally doesn’t set the error indicator; the function it called already set it.

The error indicator consists of three Python objects corresponding to the Python variables `sys.exc_type`, `sys.exc_value` and `sys.exc_traceback`. API functions exist to interact with the error indicator in various ways. There is a separate error indicator for each thread.

<div class="cfuncdesc">

voidPyErr_Print Print a standard traceback to `sys.stderr` and clear the error indicator. Call this function only when the error indicator is set. (Otherwise it will cause a fatal error!)

</div>

<div class="cfuncdesc">

PyObject\*PyErr_Occurred Test whether the error indicator is set. If set, return the exception *type* (the first argument to the last call to one of the functions or to ). If not set, return NULL. You do not own a reference to the return value, so you do not need to it. **Note:** Do not compare the return value to a specific exception; use instead, shown below. (The comparison could easily fail since the exception may be an instance instead of a class, in the case of a class exception, or it may the a subclass of the expected exception.)

</div>

<div class="cfuncdesc">

intPyErr_ExceptionMatchesPyObject \*exc Equivalent to `PyErr_GivenExceptionMatches(PyErr_Occurred(), `*`exc`*`)`. This should only be called when an exception is actually set; a memory access violation will occur if no exception has been raised.

</div>

<div class="cfuncdesc">

intPyErr_GivenExceptionMatchesPyObject \*given, PyObject \*exc Return true if the *given* exception matches the exception in *exc*. If *exc* is a class object, this also returns true when *given* is an instance of a subclass. If *exc* is a tuple, all exceptions in the tuple (and recursively in subtuples) are searched for a match. If *given* is NULL, a memory access violation will occur.

</div>

<div class="cfuncdesc">

voidPyErr_NormalizeExceptionPyObject\*\*exc, PyObject\*\*val, PyObject\*\*tb Under certain circumstances, the values returned by below can be “unnormalized”, meaning that `*`*`exc`* is a class object but `*`*`val`* is not an instance of the same class. This function can be used to instantiate the class in that case. If the values are already normalized, nothing happens. The delayed normalization is implemented to improve performance.

</div>

<div class="cfuncdesc">

voidPyErr_Clear Clear the error indicator. If the error indicator is not set, there is no effect.

</div>

<div class="cfuncdesc">

voidPyErr_FetchPyObject \*\*ptype, PyObject \*\*pvalue, PyObject \*\*ptraceback Retrieve the error indicator into three variables whose addresses are passed. If the error indicator is not set, set all three variables to NULL. If it is set, it will be cleared and you own a reference to each object retrieved. The value and traceback object may be NULL even when the type object is not. **Note:** This function is normally only used by code that needs to handle exceptions or by code that needs to save and restore the error indicator temporarily.

</div>

<div class="cfuncdesc">

voidPyErr_RestorePyObject \*type, PyObject \*value, PyObject \*traceback Set the error indicator from the three objects. If the error indicator is already set, it is cleared first. If the objects are NULL, the error indicator is cleared. Do not pass a NULL type and non-NULL value or traceback. The exception type should be a string or class; if it is a class, the value should be an instance of that class. Do not pass an invalid exception type or value. (Violating these rules will cause subtle problems later.) This call takes away a reference to each object, i.e. you must own a reference to each object before the call and after the call you no longer own these references. (If you don’t understand this, don’t use this function. I warned you.) **Note:** This function is normally only used by code that needs to save and restore the error indicator temporarily.

</div>

<div class="cfuncdesc">

voidPyErr_SetStringPyObject \*type, char \*message This is the most common way to set the error indicator. The first argument specifies the exception type; it is normally one of the standard exceptions, e.g. . You need not increment its reference count. The second argument is an error message; it is converted to a string object.

</div>

<div class="cfuncdesc">

voidPyErr_SetObjectPyObject \*type, PyObject \*value This function is similar to but lets you specify an arbitrary Python object for the “value” of the exception. You need not increment its reference count.

</div>

<div class="cfuncdesc">

PyObject\*PyErr_FormatPyObject \*exception, const char \*format, This function sets the error indicator. *exception* should be a Python object. *fmt* should be a string, containing format codes, similar to . The `width.precision` before a format code is parsed, but the width part is ignored.

|                    |                              |
|:-------------------|:-----------------------------|
| CharacterMeaning c | Character, as an             |
| parameter          | Number in decimal, as an     |
| parameter          | Number in hexadecimal, as an |
| parameter          | A string, as a               |
| parameter          |                              |

An unrecognized format character causes all the rest of the format string to be copied as-is to the result string, and any extra arguments discarded.

A new reference is returned, which is owned by the caller.

</div>

<div class="cfuncdesc">

voidPyErr_SetNonePyObject \*type This is a shorthand for `PyErr_SetObject(`*`type`*`, Py_None)`.

</div>

<div class="cfuncdesc">

intPyErr_BadArgument This is a shorthand for `PyErr_SetString(PyExc_TypeError, `*`message`*`)`, where *message* indicates that a built-in operation was invoked with an illegal argument. It is mostly for internal use.

</div>

<div class="cfuncdesc">

PyObject\*PyErr_NoMemory This is a shorthand for `PyErr_SetNone(PyExc_MemoryError)`; it returns NULL so an object allocation function can write `return PyErr_NoMemory();` when it runs out of memory.

</div>

<div class="cfuncdesc">

PyObject\*PyErr_SetFromErrnoPyObject \*type This is a convenience function to raise an exception when a C library function has returned an error and set the C variable . It constructs a tuple object whose first item is the integer value and whose second item is the corresponding error message (gotten from ), and then calls `PyErr_SetObject(`*`type`*`, `*`object`*`)`. On Unix, when the value is , indicating an interrupted system call, this calls , and if that set the error indicator, leaves it set to that. The function always returns NULL, so a wrapper function around a system call can write `return PyErr_SetFromErrno();` when the system call returns an error.

</div>

<div class="cfuncdesc">

voidPyErr_BadInternalCall This is a shorthand for `PyErr_SetString(PyExc_TypeError, `*`message`*`)`, where *message* indicates that an internal operation (e.g. a Python/C API function) was invoked with an illegal argument. It is mostly for internal use.

</div>

<div class="cfuncdesc">

intPyErr_CheckSignals This function interacts with Python’s signal handling. It checks whether a signal has been sent to the processes and if so, invokes the corresponding signal handler. If the `signal`module is supported, this can invoke a signal handler written in Python. In all cases, the default effect for is to raise the `KeyboardInterrupt` exception. If an exception is raised the error indicator is set and the function returns `1`; otherwise the function returns `0`. The error indicator may or may not be cleared if it was previously set.

</div>

<div class="cfuncdesc">

voidPyErr_SetInterrupt This function is obsolete. It simulates the effect of a signal arriving — the next time is called, `KeyboardInterrupt` will be raised. It may be called without holding the interpreter lock.

</div>

<div class="cfuncdesc">

PyObject\*PyErr_NewExceptionchar \*name, PyObject \*base, PyObject \*dict This utility function creates and returns a new exception object. The *name* argument must be the name of the new exception, a C string of the form `module.class`. The *base* and *dict* arguments are normally NULL. This creates a class object derived from the root for all exceptions, the built-in name `Exception` (accessible in C as ). The `__module__` attribute of the new class is set to the first part (up to the last dot) of the *name* argument, and the class name is set to the last part (after the last dot). The *base* argument can be used to specify an alternate base class. The *dict* argument can be used to specify a dictionary of class variables and methods.

</div>

<div class="cfuncdesc">

voidPyErr_WriteUnraisablePyObject \*obj This utility function prints a warning message to *sys.stderr* when an exception has been set but it is impossible for the interpreter to actually raise the exception. It is used, for example, when an exception occurs in an `__del__` method.

The function is called with a single argument *obj* that identifies where the context in which the unraisable exception occurred. The repr of *obj* will be printed in the warning message.

</div>

## Standard Exceptions <span id="standardExceptions" label="standardExceptions"></span>

All standard Python exceptions are available as global variables whose names are `PyExc_` followed by the Python exception name. These have the type `PyObject*`; they are all class objects. For completeness, here are all the variables:

|                                        |     |     |
|:---------------------------------------|:----|:----|
| C NamePython NameNotes PyExc_Exception |     |     |
|                                        |     |     |
|                                        |     |     |
|                                        |     |     |
|                                        |     |     |
|                                        |     |     |
|                                        |     |     |
|                                        |     |     |
|                                        |     |     |
|                                        |     |     |
|                                        |     |     |
|                                        |     |     |
|                                        |     |     |
|                                        |     |     |
|                                        |     |     |
|                                        |     |     |
|                                        |     |     |
|                                        |     |     |
|                                        |     |     |
|                                        |     |     |
|                                        |     |     |
|                                        |     |     |
|                                        |     |     |
|                                        |     |     |
|                                        |     |     |
|                                        |     |     |
|                                        |     |     |
|                                        |     |     |

Notes:

\(1\)  
This is a base class for other standard exceptions.

\(2\)  
Only defined on Windows; protect code that uses this by testing that the preprocessor macro `MS_WINDOWS` is defined.

## Deprecation of String Exceptions

All exceptions built into Python or provided in the standard library are derived from `Exception`. String exceptions are still supported in the interpreter to allow existing code to run unmodified, but this will also change in a future release.

# Utilities <span id="utilities" label="utilities"></span>

The functions in this chapter perform various utility tasks, such as parsing function arguments and constructing Python values from C values.

## OS Utilities <span id="os" label="os"></span>

<div class="cfuncdesc">

intPy_FdIsInteractiveFILE \*fp, char \*filename Return true (nonzero) if the standard I/O file *fp* with name *filename* is deemed interactive. This is the case for files for which `isatty(fileno(`*`fp`*`))` is true. If the global flag is true, this function also returns true if the *name* pointer is NULL or if the name is equal to one of the strings `’<stdin>’` or `’???’`.

</div>

<div class="cfuncdesc">

longPyOS_GetLastModificationTimechar \*filename Return the time of last modification of the file *filename*. The result is encoded in the same way as the timestamp returned by the standard C library function .

</div>

<div class="cfuncdesc">

voidPyOS_AfterFork Function to update some internal state after a process fork; this should be called in the new process if the Python interpreter will continue to be used. If a new executable is loaded into the new process, this function does not need to be called.

</div>

<div class="cfuncdesc">

intPyOS_CheckStack Return true when the interpreter runs out of stack space. This is a reliable check, but is only available when `USE_STACKCHECK` is defined (currently on Windows using the Microsoft Visual C++ compiler and on the Macintosh). `USE_CHECKSTACK` will be defined automatically; you should never change the definition in your own code.

</div>

<div class="cfuncdesc">

PyOS_sighandler_tPyOS_getsigint i Return the current signal handler for signal *i*. This is a thin wrapper around either or . Do not call those functions directly! `PyOS_sighandler_t` is a typedef alias for `void (*)(int)`.

</div>

<div class="cfuncdesc">

PyOS_sighandler_tPyOS_setsigint i, PyOS_sighandler_t h Set the signal handler for signal *i* to be *h*; return the old signal handler. This is a thin wrapper around either or . Do not call those functions directly! `PyOS_sighandler_t` is a typedef alias for `void (*)(int)`.

</div>

## Process Control <span id="processControl" label="processControl"></span>

<div class="cfuncdesc">

voidPy_FatalErrorchar \*message Print a fatal error message and kill the process. No cleanup is performed. This function should only be invoked when a condition is detected that would make it dangerous to continue using the Python interpreter; e.g., when the object administration appears to be corrupted. On Unix, the standard C library function is called which will attempt to produce a `core` file.

</div>

<div class="cfuncdesc">

voidPy_Exitint status Exit the current process. This calls and then calls the standard C library function `exit(`*`status`*`)`.

</div>

<div class="cfuncdesc">

intPy_AtExitvoid (\*func) () Register a cleanup function to be called by . The cleanup function will be called with no arguments and should return no value. At most 32 cleanup functions can be registered. When the registration is successful, returns `0`; on failure, it returns `-1`. The cleanup function registered last is called first. Each cleanup function will be called at most once. Since Python’s internal finallization will have completed before the cleanup function, no Python APIs should be called by *func*.

</div>

## Importing Modules <span id="importing" label="importing"></span>

<div class="cfuncdesc">

PyObject\*PyImport_ImportModulechar \*name This is a simplified interface to below, leaving the *globals* and *locals* arguments set to NULL. When the *name* argument contains a dot (i.e., when it specifies a submodule of a package), the *fromlist* argument is set to the list `[’*’]` so that the return value is the named module rather than the top-level package containing it as would otherwise be the case. (Unfortunately, this has an additional side effect when *name* in fact specifies a subpackage instead of a submodule: the submodules specified in the package’s `__all__` variable are loaded.) Return a new reference to the imported module, or NULL with an exception set on failure (the module may still be created in this case — examine `sys.modules` to find out).

</div>

<div class="cfuncdesc">

PyObject\*PyImport_ImportModuleExchar \*name, PyObject \*globals, PyObject \*locals, PyObject \*fromlist Import a module. This is best described by referring to the built-in Python function `__import__()`, as the standard `__import__()` function calls this function directly.

The return value is a new reference to the imported module or top-level package, or NULL with an exception set on failure (the module may still be created in this case). Like for `__import__()`, the return value when a submodule of a package was requested is normally the top-level package, unless a non-empty *fromlist* was given.

</div>

<div class="cfuncdesc">

PyObject\*PyImport_ImportPyObject \*name This is a higher-level interface that calls the current “import hook function”. It invokes the `__import__()` function from the `__builtins__` of the current globals. This means that the import is done using whatever import hooks are installed in the current environment, e.g. by `rexec`or `ihooks`.

</div>

<div class="cfuncdesc">

PyObject\*PyImport_ReloadModulePyObject \*m Reload a module. This is best described by referring to the built-in Python function `reload()`, as the standard `reload()` function calls this function directly. Return a new reference to the reloaded module, or NULL with an exception set on failure (the module still exists in this case).

</div>

<div class="cfuncdesc">

PyObject\*PyImport_AddModulechar \*name Return the module object corresponding to a module name. The *name* argument may be of the form `package.module`). First check the modules dictionary if there’s one there, and if not, create a new one and insert in in the modules dictionary. Warning: this function does not load or import the module; if the module wasn’t already loaded, you will get an empty module object. Use or one of its variants to import a module. Return NULL with an exception set on failure.

</div>

<div class="cfuncdesc">

PyObject\*PyImport_ExecCodeModulechar \*name, PyObject \*co Given a module name (possibly of the form `package.module`) and a code object read from a Python bytecode file or obtained from the built-in function `compile()`, load the module. Return a new reference to the module object, or NULL with an exception set if an error occurred (the module may still be created in this case). (This function would reload the module if it was already imported.)

</div>

<div class="cfuncdesc">

longPyImport_GetMagicNumber Return the magic number for Python bytecode files (a.k.a. `.pyc` and `.pyo` files). The magic number should be present in the first four bytes of the bytecode file, in little-endian byte order.

</div>

<div class="cfuncdesc">

PyObject\*PyImport_GetModuleDict Return the dictionary used for the module administration (a.k.a. `sys.modules`). Note that this is a per-interpreter variable.

</div>

<div class="cfuncdesc">

void\_PyImport_Init Initialize the import mechanism. For internal use only.

</div>

<div class="cfuncdesc">

voidPyImport_Cleanup Empty the module table. For internal use only.

</div>

<div class="cfuncdesc">

void\_PyImport_Fini Finalize the import mechanism. For internal use only.

</div>

<div class="cfuncdesc">

PyObject\*\_PyImport_FindExtensionchar \*, char \* For internal use only.

</div>

<div class="cfuncdesc">

PyObject\*\_PyImport_FixupExtensionchar \*, char \* For internal use only.

</div>

<div class="cfuncdesc">

intPyImport_ImportFrozenModulechar \*name Load a frozen module named *name*. Return `1` for success, `0` if the module is not found, and `-1` with an exception set if the initialization failed. To access the imported module on a successful load, use . (Note the misnomer — this function would reload the module if it was already imported.)

</div>

<div class="ctypedesc">

struct \_frozen This is the structure type definition for frozen module descriptors, as generated by the utility (see `Tools/freeze/` in the Python source distribution). Its definition, found in `Include/import.h`, is:

    struct _frozen {
        char *name;
        unsigned char *code;
        int size;
    };

</div>

<div class="cvardesc">

struct \_frozen\*PyImport_FrozenModules This pointer is initialized to point to an array of `struct _frozen` records, terminated by one whose members are all NULL or zero. When a frozen module is imported, it is searched in this table. Third-party code could play tricks with this to provide a dynamically created collection of frozen modules.

</div>

<div class="cfuncdesc">

intPyImport_AppendInittabchar \*name, void (\*initfunc)(void) Add a single module to the existing table of built-in modules. This is a convenience wrapper around , returning `-1` if the table could not be extended. The new module can be imported by the name *name*, and uses the function *initfunc* as the initialization function called on the first attempted import. This should be called before .

</div>

<div class="ctypedesc">

struct \_inittab Structure describing a single entry in the list of built-in modules. Each of these structures gives the name and initialization function for a module built into the interpreter. Programs which embed Python may use an array of these structures in conjunction with to provide additional built-in modules. The structure is defined in `Include/import.h` as:

    struct _inittab {
        char *name;
        void (*initfunc)(void);
    };

</div>

<div class="cfuncdesc">

intPyImport_ExtendInittabstruct \_inittab \*newtab Add a collection of modules to the table of built-in modules. The *newtab* array must end with a sentinel entry which contains NULL for the `name` field; failure to provide the sentinel value can result in a memory fault. Returns `0` on success or `-1` if insufficient memory could be allocated to extend the internal table. In the event of failure, no modules are added to the internal table. This should be called before .

</div>

# Abstract Objects Layer <span id="abstract" label="abstract"></span>

The functions in this chapter interact with Python objects regardless of their type, or with wide classes of object types (e.g. all numerical types, or all sequence types). When used on object types for which they do not apply, they will raise a Python exception.

## Object Protocol <span id="object" label="object"></span>

<div class="cfuncdesc">

intPyObject_PrintPyObject \*o, FILE \*fp, int flags Print an object *o*, on file *fp*. Returns `-1` on error. The flags argument is used to enable certain printing options. The only option currently supported is ; if given, the `str()` of the object is written instead of the `repr()`.

</div>

<div class="cfuncdesc">

intPyObject_HasAttrStringPyObject \*o, char \*attr_name Returns `1` if *o* has the attribute *attr_name*, and `0` otherwise. This is equivalent to the Python expression `hasattr(`*`o`*`, `*`attr_name`*`)`. This function always succeeds.

</div>

<div class="cfuncdesc">

PyObject\*PyObject_GetAttrStringPyObject \*o, char \*attr_name Retrieve an attribute named *attr_name* from object *o*. Returns the attribute value on success, or NULL on failure. This is the equivalent of the Python expression *`o`*`.`*`attr_name`*.

</div>

<div class="cfuncdesc">

intPyObject_HasAttrPyObject \*o, PyObject \*attr_name Returns `1` if *o* has the attribute *attr_name*, and `0` otherwise. This is equivalent to the Python expression `hasattr(`*`o`*`, `*`attr_name`*`)`. This function always succeeds.

</div>

<div class="cfuncdesc">

PyObject\*PyObject_GetAttrPyObject \*o, PyObject \*attr_name Retrieve an attribute named *attr_name* from object *o*. Returns the attribute value on success, or NULL on failure. This is the equivalent of the Python expression *`o`*`.`*`attr_name`*.

</div>

<div class="cfuncdesc">

intPyObject_SetAttrStringPyObject \*o, char \*attr_name, PyObject \*v Set the value of the attribute named *attr_name*, for object *o*, to the value *v*. Returns `-1` on failure. This is the equivalent of the Python statement *`o`*`.`*`attr_name`*` = `*`v`*.

</div>

<div class="cfuncdesc">

intPyObject_SetAttrPyObject \*o, PyObject \*attr_name, PyObject \*v Set the value of the attribute named *attr_name*, for object *o*, to the value *v*. Returns `-1` on failure. This is the equivalent of the Python statement *`o`*`.`*`attr_name`*` = `*`v`*.

</div>

<div class="cfuncdesc">

intPyObject_DelAttrStringPyObject \*o, char \*attr_name Delete attribute named *attr_name*, for object *o*. Returns `-1` on failure. This is the equivalent of the Python statement: `del `*`o`*`.`*`attr_name`*.

</div>

<div class="cfuncdesc">

intPyObject_DelAttrPyObject \*o, PyObject \*attr_name Delete attribute named *attr_name*, for object *o*. Returns `-1` on failure. This is the equivalent of the Python statement `del `*`o`*`.`*`attr_name`*.

</div>

<div class="cfuncdesc">

intPyObject_CmpPyObject \*o1, PyObject \*o2, int \*result Compare the values of *o1* and *o2* using a routine provided by *o1*, if one exists, otherwise with a routine provided by *o2*. The result of the comparison is returned in *result*. Returns `-1` on failure. This is the equivalent of the Python statement*`result`*` = cmp(`*`o1`*`, `*`o2`*`)`.

</div>

<div class="cfuncdesc">

intPyObject_ComparePyObject \*o1, PyObject \*o2 Compare the values of *o1* and *o2* using a routine provided by *o1*, if one exists, otherwise with a routine provided by *o2*. Returns the result of the comparison on success. On error, the value returned is undefined; use to detect an error. This is equivalent to the Python expression`cmp(`*`o1`*`, `*`o2`*`)`.

</div>

<div class="cfuncdesc">

PyObject\*PyObject_ReprPyObject \*o Compute a string representation of object *o*. Returns the string representation on success, NULL on failure. This is the equivalent of the Python expression `repr(`*`o`*`)`. Called by the `repr()`built-in function and by reverse quotes.

</div>

<div class="cfuncdesc">

PyObject\*PyObject_StrPyObject \*o Compute a string representation of object *o*. Returns the string representation on success, NULL on failure. This is the equivalent of the Python expression `str(`*`o`*`)`. Called by the `str()`built-in function and by the statement.

</div>

<div class="cfuncdesc">

intPyCallable_CheckPyObject \*o Determine if the object *o* is callable. Return `1` if the object is callable and `0` otherwise. This function always succeeds.

</div>

<div class="cfuncdesc">

PyObject\*PyObject_CallObjectPyObject \*callable_object, PyObject \*args Call a callable Python object *callable_object*, with arguments given by the tuple *args*. If no arguments are needed, then *args* may be NULL. Returns the result of the call on success, or NULL on failure. This is the equivalent of the Python expression `apply(`*`o`*`, `*`args`*`)`.

</div>

<div class="cfuncdesc">

PyObject\*PyObject_CallFunctionPyObject \*callable_object, char \*format, ... Call a callable Python object *callable_object*, with a variable number of C arguments. The C arguments are described using a style format string. The format may be NULL, indicating that no arguments are provided. Returns the result of the call on success, or NULL on failure. This is the equivalent of the Python expression `apply(`*`o`*`, `*`args`*`)`.

</div>

<div class="cfuncdesc">

PyObject\*PyObject_CallMethodPyObject \*o, char \*m, char \*format, ... Call the method named *m* of object *o* with a variable number of C arguments. The C arguments are described by a format string. The format may be NULL, indicating that no arguments are provided. Returns the result of the call on success, or NULL on failure. This is the equivalent of the Python expression *`o`*`.`*`method`*`(`*`args`*`)`. Note that special method names, such as `__add__()`, `__getitem__()`, and so on are not supported. The specific abstract-object routines for these must be used.

</div>

<div class="cfuncdesc">

intPyObject_HashPyObject \*o Compute and return the hash value of an object *o*. On failure, return `-1`. This is the equivalent of the Python expression `hash(`*`o`*`)`.

</div>

<div class="cfuncdesc">

intPyObject_IsTruePyObject \*o Returns `1` if the object *o* is considered to be true, and `0` otherwise. This is equivalent to the Python expression `not not `*`o`*. This function always succeeds.

</div>

<div class="cfuncdesc">

PyObject\*PyObject_TypePyObject \*o On success, returns a type object corresponding to the object type of object *o*. On failure, returns NULL. This is equivalent to the Python expression `type(`*`o`*`)`.

</div>

<div class="cfuncdesc">

intPyObject_LengthPyObject \*o Return the length of object *o*. If the object *o* provides both sequence and mapping protocols, the sequence length is returned. On error, `-1` is returned. This is the equivalent to the Python expression `len(`*`o`*`)`.

</div>

<div class="cfuncdesc">

PyObject\*PyObject_GetItemPyObject \*o, PyObject \*key Return element of *o* corresponding to the object *key* or NULL on failure. This is the equivalent of the Python expression *`o`*`[`*`key`*`]`.

</div>

<div class="cfuncdesc">

intPyObject_SetItemPyObject \*o, PyObject \*key, PyObject \*v Map the object *key* to the value *v*. Returns `-1` on failure. This is the equivalent of the Python statement *`o`*`[`*`key`*`] = `*`v`*.

</div>

<div class="cfuncdesc">

intPyObject_DelItemPyObject \*o, PyObject \*key Delete the mapping for *key* from *o*. Returns `-1` on failure. This is the equivalent of the Python statement `del `*`o`*`[`*`key`*`]`.

</div>

<div class="cfuncdesc">

intPyObject_AsFileDescriptorPyObject \*o Derives a file-descriptor from a Python object. If the object is an integer or long integer, its value is returned. If not, the object’s `fileno()` method is called if it exists; the method must return an integer or long integer, which is returned as the file descriptor value. Returns `-1` on failure.

</div>

## Number Protocol <span id="number" label="number"></span>

<div class="cfuncdesc">

intPyNumber_CheckPyObject \*o Returns `1` if the object *o* provides numeric protocols, and false otherwise. This function always succeeds.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_AddPyObject \*o1, PyObject \*o2 Returns the result of adding *o1* and *o2*, or NULL on failure. This is the equivalent of the Python expression *`o1`*` + `*`o2`*.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_SubtractPyObject \*o1, PyObject \*o2 Returns the result of subtracting *o2* from *o1*, or NULL on failure. This is the equivalent of the Python expression *`o1`*` - `*`o2`*.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_MultiplyPyObject \*o1, PyObject \*o2 Returns the result of multiplying *o1* and *o2*, or NULL on failure. This is the equivalent of the Python expression *`o1`*` * `*`o2`*.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_DividePyObject \*o1, PyObject \*o2 Returns the result of dividing *o1* by *o2*, or NULL on failure. This is the equivalent of the Python expression *`o1`*` / `*`o2`*.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_RemainderPyObject \*o1, PyObject \*o2 Returns the remainder of dividing *o1* by *o2*, or NULL on failure. This is the equivalent of the Python expression *`o1`*` % `*`o2`*.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_DivmodPyObject \*o1, PyObject \*o2 See the built-in function `divmod()`. Returns NULL on failure. This is the equivalent of the Python expression `divmod(`*`o1`*`, `*`o2`*`)`.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_PowerPyObject \*o1, PyObject \*o2, PyObject \*o3 See the built-in function `pow()`. Returns NULL on failure. This is the equivalent of the Python expression `pow(`*`o1`*`, `*`o2`*`, `*`o3`*`)`, where *o3* is optional. If *o3* is to be ignored, pass in its place (passing NULL for *o3* would cause an illegal memory access).

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_NegativePyObject \*o Returns the negation of *o* on success, or NULL on failure. This is the equivalent of the Python expression `-`*`o`*.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_PositivePyObject \*o Returns *o* on success, or NULL on failure. This is the equivalent of the Python expression `+`*`o`*.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_AbsolutePyObject \*o Returns the absolute value of *o*, or NULL on failure. This is the equivalent of the Python expression `abs(`*`o`*`)`.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_InvertPyObject \*o Returns the bitwise negation of *o* on success, or NULL on failure. This is the equivalent of the Python expression *`o`*.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_LshiftPyObject \*o1, PyObject \*o2 Returns the result of left shifting *o1* by *o2* on success, or NULL on failure. This is the equivalent of the Python expression *`o1`*` << `*`o2`*.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_RshiftPyObject \*o1, PyObject \*o2 Returns the result of right shifting *o1* by *o2* on success, or NULL on failure. This is the equivalent of the Python expression *`o1`*` >> `*`o2`*.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_AndPyObject \*o1, PyObject \*o2 Returns the “bitwise and” of *o2* and *o2* on success and NULL on failure. This is the equivalent of the Python expression *`o1`*` & `*`o2`*.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_XorPyObject \*o1, PyObject \*o2 Returns the “bitwise exclusive or” of *o1* by *o2* on success, or NULL on failure. This is the equivalent of the Python expression *`o1`*` ^`*`o2`*.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_OrPyObject \*o1, PyObject \*o2 Returns the “bitwise or” of *o1* and *o2* on success, or NULL on failure. This is the equivalent of the Python expression *`o1`*` | `*`o2`*.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_InPlaceAddPyObject \*o1, PyObject \*o2 Returns the result of adding *o1* and *o2*, or NULL on failure. The operation is done *in-place* when *o1* supports it. This is the equivalent of the Python expression *`o1`*` += `*`o2`*.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_InPlaceSubtractPyObject \*o1, PyObject \*o2 Returns the result of subtracting *o2* from *o1*, or NULL on failure. The operation is done *in-place* when *o1* supports it. This is the equivalent of the Python expression *`o1`*` -= `*`o2`*.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_InPlaceMultiplyPyObject \*o1, PyObject \*o2 Returns the result of multiplying *o1* and *o2*, or NULL on failure. The operation is done *in-place* when *o1* supports it. This is the equivalent of the Python expression *`o1`*` *= `*`o2`*.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_InPlaceDividePyObject \*o1, PyObject \*o2 Returns the result of dividing *o1* by *o2*, or NULL on failure. The operation is done *in-place* when *o1* supports it. This is the equivalent of the Python expression *`o1`*` /= `*`o2`*.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_InPlaceRemainderPyObject \*o1, PyObject \*o2 Returns the remainder of dividing *o1* by *o2*, or NULL on failure. The operation is done *in-place* when *o1* supports it. This is the equivalent of the Python expression *`o1`*` %= `*`o2`*.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_InPlacePowerPyObject \*o1, PyObject \*o2, PyObject \*o3 See the built-in function `pow()`. Returns NULL on failure. The operation is done *in-place* when *o1* supports it. This is the equivalent of the Python expression *`o1`*` **= `*`o2`* when o3 is , or an in-place variant of `pow(`*`o1`*`, `*`o2`*`, var``o3``)` otherwise. If *o3* is to be ignored, pass in its place (passing NULL for *o3* would cause an illegal memory access).

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_InPlaceLshiftPyObject \*o1, PyObject \*o2 Returns the result of left shifting *o1* by *o2* on success, or NULL on failure. The operation is done *in-place* when *o1* supports it. This is the equivalent of the Python expression *`o1`*` <<= `*`o2`*.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_InPlaceRshiftPyObject \*o1, PyObject \*o2 Returns the result of right shifting *o1* by *o2* on success, or NULL on failure. The operation is done *in-place* when *o1* supports it. This is the equivalent of the Python expression *`o1`*` >>= `*`o2`*.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_InPlaceAndPyObject \*o1, PyObject \*o2 Returns the “bitwise and” of *o2* and *o2* on success and NULL on failure. The operation is done *in-place* when *o1* supports it. This is the equivalent of the Python expression *`o1`*` &= `*`o2`*.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_InPlaceXorPyObject \*o1, PyObject \*o2 Returns the “bitwise exclusive or” of *o1* by *o2* on success, or NULL on failure. The operation is done *in-place* when *o1* supports it. This is the equivalent of the Python expression *`o1`*` =̂ `*`o2`*.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_InPlaceOrPyObject \*o1, PyObject \*o2 Returns the “bitwise or” of *o1* and *o2* on success, or NULL on failure. The operation is done *in-place* when *o1* supports it. This is the equivalent of the Python expression *`o1`*` |= `*`o2`*.

</div>

<div class="cfuncdesc">

intPyNumber_CoercePyObject \*\*p1, PyObject \*\*p2 This function takes the addresses of two variables of type `PyObject*`. If the objects pointed to by `*`*`p1`* and `*`*`p2`* have the same type, increment their reference count and return `0` (success). If the objects can be converted to a common numeric type, replace `*p1` and `*p2` by their converted value (with ’new’ reference counts), and return `0`. If no conversion is possible, or if some other error occurs, return `-1` (failure) and don’t increment the reference counts. The call `PyNumber_Coerce(&o1, &o2)` is equivalent to the Python statement *`o1`*`, `*`o2`*` = coerce(`*`o1`*`, `*`o2`*`)`.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_IntPyObject \*o Returns the *o* converted to an integer object on success, or NULL on failure. This is the equivalent of the Python expression `int(`*`o`*`)`.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_LongPyObject \*o Returns the *o* converted to a long integer object on success, or NULL on failure. This is the equivalent of the Python expression `long(`*`o`*`)`.

</div>

<div class="cfuncdesc">

PyObject\*PyNumber_FloatPyObject \*o Returns the *o* converted to a float object on success, or NULL on failure. This is the equivalent of the Python expression `float(`*`o`*`)`.

</div>

## Sequence Protocol <span id="sequence" label="sequence"></span>

<div class="cfuncdesc">

intPySequence_CheckPyObject \*o Return `1` if the object provides sequence protocol, and `0` otherwise. This function always succeeds.

</div>

<div class="cfuncdesc">

intPySequence_LengthPyObject \*o Returns the number of objects in sequence *o* on success, and `-1` on failure. For objects that do not provide sequence protocol, this is equivalent to the Python expression `len(`*`o`*`)`.

</div>

<div class="cfuncdesc">

PyObject\*PySequence_ConcatPyObject \*o1, PyObject \*o2 Return the concatenation of *o1* and *o2* on success, and NULL on failure. This is the equivalent of the Python expression *`o1`*` + `*`o2`*.

</div>

<div class="cfuncdesc">

PyObject\*PySequence_RepeatPyObject \*o, int count Return the result of repeating sequence object *o* *count* times, or NULL on failure. This is the equivalent of the Python expression *`o`*` * `*`count`*.

</div>

<div class="cfuncdesc">

PyObject\*PySequence_InPlaceConcatPyObject \*o1, PyObject \*o2 Return the concatenation of *o1* and *o2* on success, and NULL on failure. The operation is done *in-place* when *o1* supports it. This is the equivalent of the Python expression *`o1`*` += `*`o2`*.

</div>

<div class="cfuncdesc">

PyObject\*PySequence_InPlaceRepeatPyObject \*o, int count Return the result of repeating sequence object *o* *count* times, or NULL on failure. The operation is done *in-place* when *o* supports it. This is the equivalent of the Python expression *`o`*` *= `*`count`*.

</div>

<div class="cfuncdesc">

PyObject\*PySequence_GetItemPyObject \*o, int i Return the *i*th element of *o*, or NULL on failure. This is the equivalent of the Python expression *`o`*`[`*`i`*`]`.

</div>

<div class="cfuncdesc">

PyObject\*PySequence_GetSlicePyObject \*o, int i1, int i2 Return the slice of sequence object *o* between *i1* and *i2*, or NULL on failure. This is the equivalent of the Python expression *`o`*`[`*`i1`*`:`*`i2`*`]`.

</div>

<div class="cfuncdesc">

intPySequence_SetItemPyObject \*o, int i, PyObject \*v Assign object *v* to the *i*th element of *o*. Returns `-1` on failure. This is the equivalent of the Python statement *`o`*`[`*`i`*`] = `*`v`*.

</div>

<div class="cfuncdesc">

intPySequence_DelItemPyObject \*o, int i Delete the *i*th element of object *v*. Returns `-1` on failure. This is the equivalent of the Python statement `del `*`o`*`[`*`i`*`]`.

</div>

<div class="cfuncdesc">

intPySequence_SetSlicePyObject \*o, int i1, int i2, PyObject \*v Assign the sequence object *v* to the slice in sequence object *o* from *i1* to *i2*. This is the equivalent of the Python statement *`o`*`[`*`i1`*`:`*`i2`*`] = `*`v`*.

</div>

<div class="cfuncdesc">

intPySequence_DelSlicePyObject \*o, int i1, int i2 Delete the slice in sequence object *o* from *i1* to *i2*. Returns `-1` on failure. This is the equivalent of the Python statement `del `*`o`*`[`*`i1`*`:`*`i2`*`]`.

</div>

<div class="cfuncdesc">

PyObject\*PySequence_TuplePyObject \*o Returns the *o* as a tuple on success, and NULL on failure. This is equivalent to the Python expression `tuple(`*`o`*`)`.

</div>

<div class="cfuncdesc">

intPySequence_CountPyObject \*o, PyObject \*value Return the number of occurrences of *value* in *o*, that is, return the number of keys for which *`o`*`[`*`key`*`] == `*`value`*. On failure, return `-1`. This is equivalent to the Python expression *`o`*`.count(`*`value`*`)`.

</div>

<div class="cfuncdesc">

intPySequence_ContainsPyObject \*o, PyObject \*value Determine if *o* contains *value*. If an item in *o* is equal to *value*, return `1`, otherwise return `0`. On error, return `-1`. This is equivalent to the Python expression *`value`*` in `*`o`*.

</div>

<div class="cfuncdesc">

intPySequence_IndexPyObject \*o, PyObject \*value Return the first index *i* for which *`o`*`[`*`i`*`] == `*`value`*. On error, return `-1`. This is equivalent to the Python expression *`o`*`.index(`*`value`*`)`.

</div>

<div class="cfuncdesc">

PyObject\*PySequence_ListPyObject \*o Return a list object with the same contents as the arbitrary sequence *o*. The returned list is guaranteed to be new.

</div>

<div class="cfuncdesc">

PyObject\*PySequence_TuplePyObject \*o Return a tuple object with the same contents as the arbitrary sequence *o*. If *o* is a tuple, a new reference will be returned, otherwise a tuple will be constructed with the appropriate contents.

</div>

<div class="cfuncdesc">

PyObject\*PySequence_FastPyObject \*o, const char \*m Returns the sequence *o* as a tuple, unless it is already a tuple or list, in which case *o* is returned. Use to access the members of the result. Returns NULL on failure. If the object is not a sequence, raises `TypeError` with *m* as the message text.

</div>

<div class="cfuncdesc">

PyObject\*PySequence_Fast_GET_ITEMPyObject \*o, int i Return the *i*th element of *o*, assuming that *o* was returned by , and that *i* is within bounds. The caller is expected to get the length of the sequence by calling on *o*, since lists and tuples are guaranteed to always return their true length.

</div>

## Mapping Protocol <span id="mapping" label="mapping"></span>

<div class="cfuncdesc">

intPyMapping_CheckPyObject \*o Return `1` if the object provides mapping protocol, and `0` otherwise. This function always succeeds.

</div>

<div class="cfuncdesc">

intPyMapping_LengthPyObject \*o Returns the number of keys in object *o* on success, and `-1` on failure. For objects that do not provide mapping protocol, this is equivalent to the Python expression `len(`*`o`*`)`.

</div>

<div class="cfuncdesc">

intPyMapping_DelItemStringPyObject \*o, char \*key Remove the mapping for object *key* from the object *o*. Return `-1` on failure. This is equivalent to the Python statement `del `*`o`*`[`*`key`*`]`.

</div>

<div class="cfuncdesc">

intPyMapping_DelItemPyObject \*o, PyObject \*key Remove the mapping for object *key* from the object *o*. Return `-1` on failure. This is equivalent to the Python statement `del `*`o`*`[`*`key`*`]`.

</div>

<div class="cfuncdesc">

intPyMapping_HasKeyStringPyObject \*o, char \*key On success, return `1` if the mapping object has the key *key* and `0` otherwise. This is equivalent to the Python expression *`o`*`.has_key(`*`key`*`)`. This function always succeeds.

</div>

<div class="cfuncdesc">

intPyMapping_HasKeyPyObject \*o, PyObject \*key Return `1` if the mapping object has the key *key* and `0` otherwise. This is equivalent to the Python expression *`o`*`.has_key(`*`key`*`)`. This function always succeeds.

</div>

<div class="cfuncdesc">

PyObject\*PyMapping_KeysPyObject \*o On success, return a list of the keys in object *o*. On failure, return NULL. This is equivalent to the Python expression *`o`*`.keys()`.

</div>

<div class="cfuncdesc">

PyObject\*PyMapping_ValuesPyObject \*o On success, return a list of the values in object *o*. On failure, return NULL. This is equivalent to the Python expression *`o`*`.values()`.

</div>

<div class="cfuncdesc">

PyObject\*PyMapping_ItemsPyObject \*o On success, return a list of the items in object *o*, where each item is a tuple containing a key-value pair. On failure, return NULL. This is equivalent to the Python expression *`o`*`.items()`.

</div>

<div class="cfuncdesc">

PyObject\*PyMapping_GetItemStringPyObject \*o, char \*key Return element of *o* corresponding to the object *key* or NULL on failure. This is the equivalent of the Python expression *`o`*`[`*`key`*`]`.

</div>

<div class="cfuncdesc">

intPyMapping_SetItemStringPyObject \*o, char \*key, PyObject \*v Map the object *key* to the value *v* in object *o*. Returns `-1` on failure. This is the equivalent of the Python statement *`o`*`[`*`key`*`] = `*`v`*.

</div>

# Concrete Objects Layer <span id="concrete" label="concrete"></span>

The functions in this chapter are specific to certain Python object types. Passing them an object of the wrong type is not a good idea; if you receive an object from a Python program and you are not sure that it has the right type, you must perform a type check first; for example. to check that an object is a dictionary, use . The chapter is structured like the “family tree” of Python object types.

## Fundamental Objects <span id="fundamental" label="fundamental"></span>

This section describes Python type objects and the singleton object `None`.

### Type Objects <span id="typeObjects" label="typeObjects"></span>

<div class="ctypedesc">

PyTypeObject The C structure of the objects used to describe built-in types.

</div>

<div class="cvardesc">

PyObject\*PyType_Type This is the type object for type objects; it is the same object as `types.TypeType` in the Python layer.

</div>

<div class="cfuncdesc">

intPyType_CheckPyObject \*o Returns true is the object *o* is a type object.

</div>

<div class="cfuncdesc">

intPyType_HasFeaturePyObject \*o, int feature Returns true if the type object *o* sets the feature *feature*. Type features are denoted by single bit flags. The only defined feature flag is , described in section <a href="#buffer-structs" data-reference-type="ref" data-reference="buffer-structs">[buffer-structs]</a>.

</div>

### The None Object <span id="noneObject" label="noneObject"></span>

Note that the `PyTypeObject` for `None` is not directly exposed in the Python/C API. Since `None` is a singleton, testing for object identity (using `==` in C) is sufficient. There is no function for the same reason.

<div class="cvardesc">

PyObject\*Py_None The Python `None` object, denoting lack of value. This object has no methods.

</div>

## Sequence Objects <span id="sequenceObjects" label="sequenceObjects"></span>

Generic operations on sequence objects were discussed in the previous chapter; this section deals with the specific kinds of sequence objects that are intrinsic to the Python language.

### String Objects <span id="stringObjects" label="stringObjects"></span>

<div class="ctypedesc">

PyStringObject This subtype of `PyObject` represents a Python string object.

</div>

<div class="cvardesc">

PyTypeObjectPyString_Type This instance of `PyTypeObject` represents the Python string type; it is the same object as `types.TypeType` in the Python layer..

</div>

<div class="cfuncdesc">

intPyString_CheckPyObject \*o Returns true if the object *o* is a string object.

</div>

<div class="cfuncdesc">

PyObject\*PyString_FromStringconst char \*v Returns a new string object with the value *v* on success, and NULL on failure.

</div>

<div class="cfuncdesc">

PyObject\*PyString_FromStringAndSizeconst char \*v, int len Returns a new string object with the value *v* and length *len* on success, and NULL on failure. If *v* is NULL, the contents of the string are uninitialized.

</div>

<div class="cfuncdesc">

intPyString_SizePyObject \*string Returns the length of the string in string object *string*.

</div>

<div class="cfuncdesc">

intPyString_GET_SIZEPyObject \*string Macro form of but without error checking.

</div>

<div class="cfuncdesc">

char\*PyString_AsStringPyObject \*string Returns a null-terminated representation of the contents of *string*. The pointer refers to the internal buffer of *string*, not a copy. The data must not be modified in any way. It must not be de-allocated.

</div>

<div class="cfuncdesc">

char\*PyString_AS_STRINGPyObject \*string Macro form of but without error checking.

</div>

<div class="cfuncdesc">

intPyString_AsStringAndSizePyObject \*obj, char \*\*buffer, int \*length Returns a null-terminated representation of the contents of the object *obj* through the output variables *buffer* and *length*.

The function accepts both string and Unicode objects as input. For Unicode objects it returns the default encoded version of the object. If *length* is set to NULL, the resulting buffer may not contain null characters; if it does, the function returns -1 and a TypeError is raised.

The buffer refers to an internal string buffer of *obj*, not a copy. The data must not be modified in any way. It must not be de-allocated.

</div>

<div class="cfuncdesc">

voidPyString_ConcatPyObject \*\*string, PyObject \*newpart Creates a new string object in *\*string* containing the contents of *newpart* appended to *string*; the caller will own the new reference. The reference to the old value of *string* will be stolen. If the new string cannot be created, the old reference to *string* will still be discarded and the value of *\*string* will be set to NULL; the appropriate exception will be set.

</div>

<div class="cfuncdesc">

voidPyString_ConcatAndDelPyObject \*\*string, PyObject \*newpart Creates a new string object in *\*string* containing the contents of *newpart* appended to *string*. This version decrements the reference count of *newpart*.

</div>

<div class="cfuncdesc">

int\_PyString_ResizePyObject \*\*string, int newsize A way to resize a string object even though it is “immutable”. Only use this to build up a brand new string object; don’t use this if the string may already be known in other parts of the code.

</div>

<div class="cfuncdesc">

PyObject\*PyString_FormatPyObject \*format, PyObject \*args Returns a new string object from *format* and *args*. Analogous to *`format`*` % `*`args`*. The *args* argument must be a tuple.

</div>

<div class="cfuncdesc">

voidPyString_InternInPlacePyObject \*\*string Intern the argument *\*string* in place. The argument must be the address of a pointer variable pointing to a Python string object. If there is an existing interned string that is the same as *\*string*, it sets *\*string* to it (decrementing the reference count of the old string object and incrementing the reference count of the interned string object), otherwise it leaves *\*string* alone and interns it (incrementing its reference count). (Clarification: even though there is a lot of talk about reference counts, think of this function as reference-count-neutral; you own the object after the call if and only if you owned it before the call.)

</div>

<div class="cfuncdesc">

PyObject\*PyString_InternFromStringconst char \*v A combination of and , returning either a new string object that has been interned, or a new (“owned”) reference to an earlier interned string object with the same value.

</div>

<div class="cfuncdesc">

PyObject\*PyString_Decodeconst char \*s, int size, const char \*encoding, const char \*errors Create a string object by decoding *size* bytes of the encoded buffer *s*. *encoding* and *errors* have the same meaning as the parameters of the same name in the unicode() builtin function. The codec to be used is looked up using the Python codec registry. Returns NULL in case an exception was raised by the codec.

</div>

<div class="cfuncdesc">

PyObject\*PyString_Encodeconst Py_UNICODE \*s, int size, const char \*encoding, const char \*errors Encodes the `Py_UNICODE` buffer of the given size and returns a Python string object. *encoding* and *errors* have the same meaning as the parameters of the same name in the string .encode() method. The codec to be used is looked up using the Python codec registry. Returns NULL in case an exception was raised by the codec.

</div>

<div class="cfuncdesc">

PyObject\*PyString_AsEncodedStringPyObject \*unicode, const char \*encoding, const char \*errors Encodes a string object and returns the result as Python string object. *encoding* and *errors* have the same meaning as the parameters of the same name in the string .encode() method. The codec to be used is looked up using the Python codec registry. Returns NULL in case an exception was raised by the codec.

</div>

### Unicode Objects <span id="unicodeObjects" label="unicodeObjects"></span>

These are the basic Unicode object types used for the Unicode implementation in Python:

<div class="ctypedesc">

Py_UNICODE This type represents a 16-bit unsigned storage type which is used by Python internally as basis for holding Unicode ordinals. On platforms where `wchar_t` is available and also has 16-bits, `Py_UNICODE` is a typedef alias for `wchar_t` to enhance native platform compatibility. On all other platforms, `Py_UNICODE` is a typedef alias for `unsigned short`.

</div>

<div class="ctypedesc">

PyUnicodeObject This subtype of `PyObject` represents a Python Unicode object.

</div>

<div class="cvardesc">

PyTypeObjectPyUnicode_Type This instance of `PyTypeObject` represents the Python Unicode type.

</div>

The following APIs are really C macros and can be used to do fast checks and to access internal read-only data of Unicode objects:

<div class="cfuncdesc">

intPyUnicode_CheckPyObject \*o Returns true if the object *o* is a Unicode object.

</div>

<div class="cfuncdesc">

intPyUnicode_GET_SIZEPyObject \*o Returns the size of the object. o has to be a PyUnicodeObject (not checked).

</div>

<div class="cfuncdesc">

intPyUnicode_GET_DATA_SIZEPyObject \*o Returns the size of the object’s internal buffer in bytes. o has to be a PyUnicodeObject (not checked).

</div>

<div class="cfuncdesc">

Py_UNICODE\*PyUnicode_AS_UNICODEPyObject \*o Returns a pointer to the internal Py_UNICODE buffer of the object. o has to be a PyUnicodeObject (not checked).

</div>

<div class="cfuncdesc">

const char\*PyUnicode_AS_DATAPyObject \*o Returns a (const char \*) pointer to the internal buffer of the object. o has to be a PyUnicodeObject (not checked).

</div>

Unicode provides many different character properties. The most often needed ones are available through these macros which are mapped to C functions depending on the Python configuration.

<div class="cfuncdesc">

intPy_UNICODE_ISSPACEPy_UNICODE ch Returns 1/0 depending on whether *ch* is a whitespace character.

</div>

<div class="cfuncdesc">

intPy_UNICODE_ISLOWERPy_UNICODE ch Returns 1/0 depending on whether *ch* is a lowercase character.

</div>

<div class="cfuncdesc">

intPy_UNICODE_ISUPPERPy_UNICODE ch Returns 1/0 depending on whether *ch* is an uppercase character.

</div>

<div class="cfuncdesc">

intPy_UNICODE_ISTITLEPy_UNICODE ch Returns 1/0 depending on whether *ch* is a titlecase character.

</div>

<div class="cfuncdesc">

intPy_UNICODE_ISLINEBREAKPy_UNICODE ch Returns 1/0 depending on whether *ch* is a linebreak character.

</div>

<div class="cfuncdesc">

intPy_UNICODE_ISDECIMALPy_UNICODE ch Returns 1/0 depending on whether *ch* is a decimal character.

</div>

<div class="cfuncdesc">

intPy_UNICODE_ISDIGITPy_UNICODE ch Returns 1/0 depending on whether *ch* is a digit character.

</div>

<div class="cfuncdesc">

intPy_UNICODE_ISNUMERICPy_UNICODE ch Returns 1/0 depending on whether *ch* is a numeric character.

</div>

<div class="cfuncdesc">

intPy_UNICODE_ISALPHAPy_UNICODE ch Returns 1/0 depending on whether *ch* is an alphabetic character.

</div>

<div class="cfuncdesc">

intPy_UNICODE_ISALNUMPy_UNICODE ch Returns 1/0 depending on whether *ch* is an alphanumeric character.

</div>

These APIs can be used for fast direct character conversions:

<div class="cfuncdesc">

Py_UNICODEPy_UNICODE_TOLOWERPy_UNICODE ch Returns the character *ch* converted to lower case.

</div>

<div class="cfuncdesc">

Py_UNICODEPy_UNICODE_TOUPPERPy_UNICODE ch Returns the character *ch* converted to upper case.

</div>

<div class="cfuncdesc">

Py_UNICODEPy_UNICODE_TOTITLEPy_UNICODE ch Returns the character *ch* converted to title case.

</div>

<div class="cfuncdesc">

intPy_UNICODE_TODECIMALPy_UNICODE ch Returns the character *ch* converted to a decimal positive integer. Returns -1 in case this is not possible. Does not raise exceptions.

</div>

<div class="cfuncdesc">

intPy_UNICODE_TODIGITPy_UNICODE ch Returns the character *ch* converted to a single digit integer. Returns -1 in case this is not possible. Does not raise exceptions.

</div>

<div class="cfuncdesc">

doublePy_UNICODE_TONUMERICPy_UNICODE ch Returns the character *ch* converted to a (positive) double. Returns -1.0 in case this is not possible. Does not raise exceptions.

</div>

To create Unicode objects and access their basic sequence properties, use these APIs:

<div class="cfuncdesc">

PyObject\*PyUnicode_FromUnicodeconst Py_UNICODE \*u, int size

Create a Unicode Object from the Py_UNICODE buffer *u* of the given size. *u* may be NULL which causes the contents to be undefined. It is the user’s responsibility to fill in the needed data. The buffer is copied into the new object.

</div>

<div class="cfuncdesc">

Py_UNICODE\*PyUnicode_AsUnicodePyObject \*unicode Return a read-only pointer to the Unicode object’s internal `Py_UNICODE` buffer.

</div>

<div class="cfuncdesc">

intPyUnicode_GetSizePyObject \*unicode Return the length of the Unicode object.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_FromEncodedObjectPyObject \*obj, const char \*encoding, const char \*errors

Coerce an encoded object obj to an Unicode object and return a reference with incremented refcount.

Coercion is done in the following way:

1.  Unicode objects are passed back as-is with incremented refcount. Note: these cannot be decoded; passing a non-NULL value for encoding will result in a TypeError.

2.  String and other char buffer compatible objects are decoded according to the given encoding and using the error handling defined by errors. Both can be NULL to have the interface use the default values (see the next section for details).

3.  All other objects cause an exception.

The API returns NULL in case of an error. The caller is responsible for decref’ing the returned objects.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_FromObjectPyObject \*obj

Shortcut for PyUnicode_FromEncodedObject(obj, NULL, “strict”) which is used throughout the interpreter whenever coercion to Unicode is needed.

</div>

If the platform supports `wchar_t` and provides a header file wchar.h, Python can interface directly to this type using the following functions. Support is optimized if Python’s own `Py_UNICODE` type is identical to the system’s `wchar_t`.

<div class="cfuncdesc">

PyObject\*PyUnicode_FromWideCharconst wchar_t \*w, int size Create a Unicode Object from the `whcar_t` buffer *w* of the given size. Returns NULL on failure.

</div>

<div class="cfuncdesc">

intPyUnicode_AsWideCharPyUnicodeObject \*unicode, wchar_t \*w, int size Copies the Unicode Object contents into the `whcar_t` buffer *w*. At most *size* `whcar_t` characters are copied. Returns the number of `whcar_t` characters copied or -1 in case of an error.

</div>

#### Builtin Codecs <span id="builtinCodecs" label="builtinCodecs"></span>

Python provides a set of builtin codecs which are written in C for speed. All of these codecs are directly usable via the following functions.

Many of the following APIs take two arguments encoding and errors. These parameters encoding and errors have the same semantics as the ones of the builtin unicode() Unicode object constructor.

Setting encoding to NULL causes the default encoding to be used which is UTF-8.

Error handling is set by errors which may also be set to NULL meaning to use the default handling defined for the codec. Default error handling for all builtin codecs is “strict” (ValueErrors are raised).

The codecs all use a similar interface. Only deviation from the following generic ones are documented for simplicity.

These are the generic codec APIs:

<div class="cfuncdesc">

PyObject\*PyUnicode_Decodeconst char \*s, int size, const char \*encoding, const char \*errors Create a Unicode object by decoding *size* bytes of the encoded string *s*. *encoding* and *errors* have the same meaning as the parameters of the same name in the unicode() builtin function. The codec to be used is looked up using the Python codec registry. Returns NULL in case an exception was raised by the codec.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_Encodeconst Py_UNICODE \*s, int size, const char \*encoding, const char \*errors Encodes the `Py_UNICODE` buffer of the given size and returns a Python string object. *encoding* and *errors* have the same meaning as the parameters of the same name in the Unicode .encode() method. The codec to be used is looked up using the Python codec registry. Returns NULL in case an exception was raised by the codec.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_AsEncodedStringPyObject \*unicode, const char \*encoding, const char \*errors Encodes a Unicode object and returns the result as Python string object. *encoding* and *errors* have the same meaning as the parameters of the same name in the Unicode .encode() method. The codec to be used is looked up using the Python codec registry. Returns NULL in case an exception was raised by the codec.

</div>

These are the UTF-8 codec APIs:

<div class="cfuncdesc">

PyObject\*PyUnicode_DecodeUTF8const char \*s, int size, const char \*errors Creates a Unicode object by decoding *size* bytes of the UTF-8 encoded string *s*. Returns NULL in case an exception was raised by the codec.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_EncodeUTF8const Py_UNICODE \*s, int size, const char \*errors Encodes the `Py_UNICODE` buffer of the given size using UTF-8 and returns a Python string object. Returns NULL in case an exception was raised by the codec.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_AsUTF8StringPyObject \*unicode Encodes a Unicode objects using UTF-8 and returns the result as Python string object. Error handling is “strict”. Returns NULL in case an exception was raised by the codec.

</div>

These are the UTF-16 codec APIs:

<div class="cfuncdesc">

PyObject\*PyUnicode_DecodeUTF16const char \*s, int size, const char \*errors, int \*byteorder Decodes *length* bytes from a UTF-16 encoded buffer string and returns the corresponding Unicode object.

*errors* (if non-NULL) defines the error handling. It defaults to “strict”.

If *byteorder* is non-NULL, the decoder starts decoding using the given byte order:

       *byteorder == -1: little endian
       *byteorder == 0:  native order
       *byteorder == 1:  big endian

and then switches according to all byte order marks (BOM) it finds in the input data. BOM marks are not copied into the resulting Unicode string. After completion, *\*byteorder* is set to the current byte order at the end of input data.

If *byteorder* is NULL, the codec starts in native order mode.

Returns NULL in case an exception was raised by the codec.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_EncodeUTF16const Py_UNICODE \*s, int size, const char \*errors, int byteorder Returns a Python string object holding the UTF-16 encoded value of the Unicode data in *s*.

If *byteorder* is not `0`, output is written according to the following byte order:

       byteorder == -1: little endian
       byteorder == 0:  native byte order (writes a BOM mark)
       byteorder == 1:  big endian

If byteorder is `0`, the output string will always start with the Unicode BOM mark (U+FEFF). In the other two modes, no BOM mark is prepended.

Note that `Py_UNICODE` data is being interpreted as UTF-16 reduced to UCS-2. This trick makes it possible to add full UTF-16 capabilities at a later point without comprimising the APIs.

Returns NULL in case an exception was raised by the codec.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_AsUTF16StringPyObject \*unicode Returns a Python string using the UTF-16 encoding in native byte order. The string always starts with a BOM mark. Error handling is “strict”. Returns NULL in case an exception was raised by the codec.

</div>

These are the “Unicode Esacpe” codec APIs:

<div class="cfuncdesc">

PyObject\*PyUnicode_DecodeUnicodeEscapeconst char \*s, int size, const char \*errors Creates a Unicode object by decoding *size* bytes of the Unicode-Esacpe encoded string *s*. Returns NULL in case an exception was raised by the codec.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_EncodeUnicodeEscapeconst Py_UNICODE \*s, int size, const char \*errors Encodes the `Py_UNICODE` buffer of the given size using Unicode-Escape and returns a Python string object. Returns NULL in case an exception was raised by the codec.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_AsUnicodeEscapeStringPyObject \*unicode Encodes a Unicode objects using Unicode-Escape and returns the result as Python string object. Error handling is “strict”. Returns NULL in case an exception was raised by the codec.

</div>

These are the “Raw Unicode Esacpe” codec APIs:

<div class="cfuncdesc">

PyObject\*PyUnicode_DecodeRawUnicodeEscapeconst char \*s, int size, const char \*errors Creates a Unicode object by decoding *size* bytes of the Raw-Unicode-Esacpe encoded string *s*. Returns NULL in case an exception was raised by the codec.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_EncodeRawUnicodeEscapeconst Py_UNICODE \*s, int size, const char \*errors Encodes the `Py_UNICODE` buffer of the given size using Raw-Unicode-Escape and returns a Python string object. Returns NULL in case an exception was raised by the codec.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_AsRawUnicodeEscapeStringPyObject \*unicode Encodes a Unicode objects using Raw-Unicode-Escape and returns the result as Python string object. Error handling is “strict”. Returns NULL in case an exception was raised by the codec.

</div>

These are the Latin-1 codec APIs:

Latin-1 corresponds to the first 256 Unicode ordinals and only these are accepted by the codecs during encoding.

<div class="cfuncdesc">

PyObject\*PyUnicode_DecodeLatin1const char \*s, int size, const char \*errors Creates a Unicode object by decoding *size* bytes of the Latin-1 encoded string *s*. Returns NULL in case an exception was raised by the codec.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_EncodeLatin1const Py_UNICODE \*s, int size, const char \*errors Encodes the `Py_UNICODE` buffer of the given size using Latin-1 and returns a Python string object. Returns NULL in case an exception was raised by the codec.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_AsLatin1StringPyObject \*unicode Encodes a Unicode objects using Latin-1 and returns the result as Python string object. Error handling is “strict”. Returns NULL in case an exception was raised by the codec.

</div>

These are the codec APIs. Only 7-bit data is accepted. All other codes generate errors.

<div class="cfuncdesc">

PyObject\*PyUnicode_DecodeASCIIconst char \*s, int size, const char \*errors Creates a Unicode object by decoding *size* bytes of the encoded string *s*. Returns NULL in case an exception was raised by the codec.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_EncodeASCIIconst Py_UNICODE \*s, int size, const char \*errors Encodes the `Py_UNICODE` buffer of the given size using and returns a Python string object. Returns NULL in case an exception was raised by the codec.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_AsASCIIStringPyObject \*unicode Encodes a Unicode objects using and returns the result as Python string object. Error handling is “strict”. Returns NULL in case an exception was raised by the codec.

</div>

These are the mapping codec APIs:

This codec is special in that it can be used to implement many different codecs (and this is in fact what was done to obtain most of the standard codecs included in the `encodings` package). The codec uses mapping to encode and decode characters.

Decoding mappings must map single string characters to single Unicode characters, integers (which are then interpreted as Unicode ordinals) or None (meaning "undefined mapping" and causing an error).

Encoding mappings must map single Unicode characters to single string characters, integers (which are then interpreted as Latin-1 ordinals) or None (meaning "undefined mapping" and causing an error).

The mapping objects provided must only support the \_\_getitem\_\_ mapping interface.

If a character lookup fails with a LookupError, the character is copied as-is meaning that its ordinal value will be interpreted as Unicode or Latin-1 ordinal resp. Because of this, mappings only need to contain those mappings which map characters to different code points.

<div class="cfuncdesc">

PyObject\*PyUnicode_DecodeCharmapconst char \*s, int size, PyObject \*mapping, const char \*errors Creates a Unicode object by decoding *size* bytes of the encoded string *s* using the given *mapping* object. Returns NULL in case an exception was raised by the codec.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_EncodeCharmapconst Py_UNICODE \*s, int size, PyObject \*mapping, const char \*errors Encodes the `Py_UNICODE` buffer of the given size using the given *mapping* object and returns a Python string object. Returns NULL in case an exception was raised by the codec.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_AsCharmapStringPyObject \*unicode, PyObject \*mapping Encodes a Unicode objects using the given *mapping* object and returns the result as Python string object. Error handling is “strict”. Returns NULL in case an exception was raised by the codec.

</div>

The following codec API is special in that maps Unicode to Unicode.

<div class="cfuncdesc">

PyObject\*PyUnicode_TranslateCharmapconst Py_UNICODE \*s, int size, PyObject \*table, const char \*errors Translates a `Py_UNICODE` buffer of the given length by applying a character mapping *table* to it and returns the resulting Unicode object. Returns NULL when an exception was raised by the codec.

The *mapping* table must map Unicode ordinal integers to Unicode ordinal integers or None (causing deletion of the character).

Mapping tables must only provide the \_\_getitem\_\_ interface, e.g. dictionaries or sequences. Unmapped character ordinals (ones which cause a LookupError) are left untouched and are copied as-is.

</div>

These are the MBCS codec APIs. They are currently only available on Windows and use the Win32 MBCS converters to implement the conversions. Note that MBCS (or DBCS) is a class of encodings, not just one. The target encoding is defined by the user settings on the machine running the codec.

<div class="cfuncdesc">

PyObject\*PyUnicode_DecodeMBCSconst char \*s, int size, const char \*errors Creates a Unicode object by decoding *size* bytes of the MBCS encoded string *s*. Returns NULL in case an exception was raised by the codec.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_EncodeMBCSconst Py_UNICODE \*s, int size, const char \*errors Encodes the `Py_UNICODE` buffer of the given size using MBCS and returns a Python string object. Returns NULL in case an exception was raised by the codec.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_AsMBCSStringPyObject \*unicode Encodes a Unicode objects using MBCS and returns the result as Python string object. Error handling is “strict”. Returns NULL in case an exception was raised by the codec.

</div>

#### Methods and Slot Functions <span id="unicodeMethodsAndSlots" label="unicodeMethodsAndSlots"></span>

The following APIs are capable of handling Unicode objects and strings on input (we refer to them as strings in the descriptions) and return Unicode objects or integers as apporpriate.

They all return NULL or -1 in case an exception occurrs.

<div class="cfuncdesc">

PyObject\*PyUnicode_ConcatPyObject \*left, PyObject \*right Concat two strings giving a new Unicode string.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_SplitPyObject \*s, PyObject \*sep, int maxsplit Split a string giving a list of Unicode strings.

If sep is NULL, splitting will be done at all whitespace substrings. Otherwise, splits occur at the given separator.

At most maxsplit splits will be done. If negative, no limit is set.

Separators are not included in the resulting list.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_SplitlinesPyObject \*s, int maxsplit Split a Unicode string at line breaks, returning a list of Unicode strings. CRLF is considered to be one line break. The Line break characters are not included in the resulting strings.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_TranslatePyObject \*str, PyObject \*table, const char \*errors Translate a string by applying a character mapping table to it and return the resulting Unicode object.

The mapping table must map Unicode ordinal integers to Unicode ordinal integers or None (causing deletion of the character).

Mapping tables must only provide the \_\_getitem\_\_ interface, e.g. dictionaries or sequences. Unmapped character ordinals (ones which cause a LookupError) are left untouched and are copied as-is.

*errors* has the usual meaning for codecs. It may be NULL which indicates to use the default error handling.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_JoinPyObject \*separator, PyObject \*seq Join a sequence of strings using the given separator and return the resulting Unicode string.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_TailmatchPyObject \*str, PyObject \*substr, int start, int end, int direction Return 1 if *substr* matches *str*\[*start*:*end*\] at the given tail end (*direction* == -1 means to do a prefix match, *direction* == 1 a suffix match), 0 otherwise.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_FindPyObject \*str, PyObject \*substr, int start, int end, int direction Return the first position of *substr* in *str*\[*start*:*end*\] using the given *direction* (*direction* == 1 means to do a forward search, *direction* == -1 a backward search), 0 otherwise.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_CountPyObject \*str, PyObject \*substr, int start, int end Count the number of occurrences of *substr* in *str*\[*start*:*end*\]

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_ReplacePyObject \*str, PyObject \*substr, PyObject \*replstr, int maxcount Replace at most *maxcount* occurrences of *substr* in *str* with *replstr* and return the resulting Unicode object. *maxcount* == -1 means: replace all occurrences.

</div>

<div class="cfuncdesc">

intPyUnicode_ComparePyObject \*left, PyObject \*right Compare two strings and return -1, 0, 1 for less than, equal, greater than resp.

</div>

<div class="cfuncdesc">

PyObject\*PyUnicode_FormatPyObject \*format, PyObject \*args Returns a new string object from *format* and *args*; this is analogous to *`format`*` % `*`args`*. The *args* argument must be a tuple.

</div>

<div class="cfuncdesc">

intPyUnicode_ContainsPyObject \*container, PyObject \*element Checks whether *element* is contained in *container* and returns true or false accordingly.

*element* has to coerce to a one element Unicode string. `-1` is returned in case of an error.

</div>

### Buffer Objects <span id="bufferObjects" label="bufferObjects"></span>

Python objects implemented in C can export a group of functions called the “bufferinterface.” These functions can be used by an object to expose its data in a raw, byte-oriented format. Clients of the object can use the buffer interface to access the object data directly, without needing to copy it first.

Two examples of objects that support the buffer interface are strings and arrays. The string object exposes the character contents in the buffer interface’s byte-oriented form. An array can also expose its contents, but it should be noted that array elements may be multi-byte values.

An example user of the buffer interface is the file object’s `write()` method. Any object that can export a series of bytes through the buffer interface can be written to a file. There are a number of format codes to that operate against an object’s buffer interface, returning data from the target object.

More information on the buffer interface is provided in the section “Buffer Object Structures” (section <a href="#buffer-structs" data-reference-type="ref" data-reference="buffer-structs">[buffer-structs]</a>), under the description for `PyBufferProcs`.

A “buffer object” is defined in the `bufferobject.h` header (included by `Python.h`). These objects look very similar to string objects at the Python programming level: they support slicing, indexing, concatenation, and some other standard string operations. However, their data can come from one of two sources: from a block of memory, or from another object which exports the buffer interface.

Buffer objects are useful as a way to expose the data from another object’s buffer interface to the Python programmer. They can also be used as a zero-copy slicing mechanism. Using their ability to reference a block of memory, it is possible to expose any data to the Python programmer quite easily. The memory could be a large, constant array in a C extension, it could be a raw block of memory for manipulation before passing to an operating system library, or it could be used to pass around structured data in its native, in-memory format.

<div class="ctypedesc">

PyBufferObject This subtype of `PyObject` represents a buffer object.

</div>

<div class="cvardesc">

PyTypeObjectPyBuffer_Type The instance of `PyTypeObject` which represents the Python buffer type; it is the same object as `types.BufferType` in the Python layer..

</div>

<div class="cvardesc">

intPy_END_OF_BUFFER This constant may be passed as the *size* parameter to or . It indicates that the new `PyBufferObject` should refer to *base* object from the specified *offset* to the end of its exported buffer. Using this enables the caller to avoid querying the *base* object for its length.

</div>

<div class="cfuncdesc">

intPyBuffer_CheckPyObject \*p Return true if the argument has type .

</div>

<div class="cfuncdesc">

PyObject\*PyBuffer_FromObjectPyObject \*base, int offset, int size Return a new read-only buffer object. This raises `TypeError` if *base* doesn’t support the read-only buffer protocol or doesn’t provide exactly one buffer segment, or it raises `ValueError` if *offset* is less than zero. The buffer will hold a reference to the *base* object, and the buffer’s contents will refer to the *base* object’s buffer interface, starting as position *offset* and extending for *size* bytes. If *size* is , then the new buffer’s contents extend to the length of the *base* object’s exported buffer data.

</div>

<div class="cfuncdesc">

PyObject\*PyBuffer_FromReadWriteObjectPyObject \*base, int offset, int size Return a new writable buffer object. Parameters and exceptions are similar to those for . If the *base* object does not export the writeable buffer protocol, then `TypeError` is raised.

</div>

<div class="cfuncdesc">

PyObject\*PyBuffer_FromMemoryvoid \*ptr, int size Return a new read-only buffer object that reads from a specified location in memory, with a specified size. The caller is responsible for ensuring that the memory buffer, passed in as *ptr*, is not deallocated while the returned buffer object exists. Raises `ValueError` if *size* is less than zero. Note that may *not* be passed for the *size* parameter; `ValueError` will be raised in that case.

</div>

<div class="cfuncdesc">

PyObject\*PyBuffer_FromReadWriteMemoryvoid \*ptr, int size Similar to , but the returned buffer is writable.

</div>

<div class="cfuncdesc">

PyObject\*PyBuffer_Newint size Returns a new writable buffer object that maintains its own memory buffer of *size* bytes. `ValueError` is returned if *size* is not zero or positive.

</div>

### Tuple Objects <span id="tupleObjects" label="tupleObjects"></span>

<div class="ctypedesc">

PyTupleObject This subtype of `PyObject` represents a Python tuple object.

</div>

<div class="cvardesc">

PyTypeObjectPyTuple_Type This instance of `PyTypeObject` represents the Python tuple type; it is the same object as `types.TupleType` in the Python layer..

</div>

<div class="cfuncdesc">

intPyTuple_CheckPyObject \*p Return true if the argument is a tuple object.

</div>

<div class="cfuncdesc">

PyObject\*PyTuple_Newint len Return a new tuple object of size *len*, or NULL on failure.

</div>

<div class="cfuncdesc">

intPyTuple_SizePyTupleObject \*p Takes a pointer to a tuple object, and returns the size of that tuple.

</div>

<div class="cfuncdesc">

PyObject\*PyTuple_GetItemPyTupleObject \*p, int pos Returns the object at position *pos* in the tuple pointed to by *p*. If *pos* is out of bounds, returns NULL and sets an `IndexError` exception.

</div>

<div class="cfuncdesc">

PyObject\*PyTuple_GET_ITEMPyTupleObject \*p, int pos Does the same, but does no checking of its arguments.

</div>

<div class="cfuncdesc">

PyObject\*PyTuple_GetSlicePyTupleObject \*p, int low, int high Takes a slice of the tuple pointed to by *p* from *low* to *high* and returns it as a new tuple.

</div>

<div class="cfuncdesc">

intPyTuple_SetItemPyObject \*p, int pos, PyObject \*o Inserts a reference to object *o* at position *pos* of the tuple pointed to by *p*. It returns `0` on success. **Note:** This function “steals” a reference to *o*.

</div>

<div class="cfuncdesc">

voidPyTuple_SET_ITEMPyObject \*p, int pos, PyObject \*o Does the same, but does no error checking, and should *only* be used to fill in brand new tuples. **Note:** This function “steals” a reference to *o*.

</div>

<div class="cfuncdesc">

int\_PyTuple_ResizePyTupleObject \*p, int newsize, int last_is_sticky Can be used to resize a tuple. *newsize* will be the new length of the tuple. Because tuples are *supposed* to be immutable, this should only be used if there is only one reference to the object. Do *not* use this if the tuple may already be known to some other part of the code. *last_is_sticky* is a flag — if true, the tuple will grow or shrink at the front, otherwise it will grow or shrink at the end. Think of this as destroying the old tuple and creating a new one, only more efficiently. Returns `0` on success and `-1` on failure (in which case a `MemoryError` or `SystemError` will be raised).

</div>

### List Objects <span id="listObjects" label="listObjects"></span>

<div class="ctypedesc">

PyListObject This subtype of `PyObject` represents a Python list object.

</div>

<div class="cvardesc">

PyTypeObjectPyList_Type This instance of `PyTypeObject` represents the Python list type. This is the same object as `types.ListType`.

</div>

<div class="cfuncdesc">

intPyList_CheckPyObject \*p Returns true if its argument is a `PyListObject`.

</div>

<div class="cfuncdesc">

PyObject\*PyList_Newint len Returns a new list of length *len* on success, or NULL on failure.

</div>

<div class="cfuncdesc">

intPyList_SizePyObject \*list Returns the length of the list object in *list*; this is equivalent to `len(`*`list`*`)` on a list object.

</div>

<div class="cfuncdesc">

intPyList_GET_SIZEPyObject \*list Macro form of without error checking.

</div>

<div class="cfuncdesc">

PyObject\*PyList_GetItemPyObject \*list, int index Returns the object at position *pos* in the list pointed to by *p*. If *pos* is out of bounds, returns NULL and sets an `IndexError` exception.

</div>

<div class="cfuncdesc">

PyObject\*PyList_GET_ITEMPyObject \*list, int i Macro form of without error checking.

</div>

<div class="cfuncdesc">

intPyList_SetItemPyObject \*list, int index, PyObject \*item Sets the item at index *index* in list to *item*. **Note:** This function “steals” a reference to *item*.

</div>

<div class="cfuncdesc">

PyObject\*PyList_SET_ITEMPyObject \*list, int i, PyObject \*o Macro form of without error checking. **Note:** This function “steals” a reference to *item*.

</div>

<div class="cfuncdesc">

intPyList_InsertPyObject \*list, int index, PyObject \*item Inserts the item *item* into list *list* in front of index *index*. Returns `0` if successful; returns `-1` and raises an exception if unsuccessful. Analogous to *`list`*`.insert(`*`index`*`, `*`item`*`)`.

</div>

<div class="cfuncdesc">

intPyList_AppendPyObject \*list, PyObject \*item Appends the object *item* at the end of list *list*. Returns `0` if successful; returns `-1` and sets an exception if unsuccessful. Analogous to *`list`*`.append(`*`item`*`)`.

</div>

<div class="cfuncdesc">

PyObject\*PyList_GetSlicePyObject \*list, int low, int high Returns a list of the objects in *list* containing the objects *between* *low* and *high*. Returns NULL and sets an exception if unsuccessful. Analogous to *`list`*`[`*`low`*`:`*`high`*`]`.

</div>

<div class="cfuncdesc">

intPyList_SetSlicePyObject \*list, int low, int high, PyObject \*itemlist Sets the slice of *list* between *low* and *high* to the contents of *itemlist*. Analogous to *`list`*`[`*`low`*`:`*`high`*`] = `*`itemlist`*. Returns `0` on success, `-1` on failure.

</div>

<div class="cfuncdesc">

intPyList_SortPyObject \*list Sorts the items of *list* in place. Returns `0` on success, `-1` on failure. This is equivalent to *`list`*`.sort()`.

</div>

<div class="cfuncdesc">

intPyList_ReversePyObject \*list Reverses the items of *list* in place. Returns `0` on success, `-1` on failure. This is the equivalent of *`list`*`.reverse()`.

</div>

<div class="cfuncdesc">

PyObject\*PyList_AsTuplePyObject \*list Returns a new tuple object containing the contents of *list*; equivalent to `tuple(`*`list`*`)`.

</div>

## Mapping Objects <span id="mapObjects" label="mapObjects"></span>

### Dictionary Objects <span id="dictObjects" label="dictObjects"></span>

<div class="ctypedesc">

PyDictObject This subtype of `PyObject` represents a Python dictionary object.

</div>

<div class="cvardesc">

PyTypeObjectPyDict_Type This instance of `PyTypeObject` represents the Python dictionary type. This is exposed to Python programs as `types.DictType` and `types.DictionaryType`.

</div>

<div class="cfuncdesc">

intPyDict_CheckPyObject \*p Returns true if its argument is a `PyDictObject`.

</div>

<div class="cfuncdesc">

PyObject\*PyDict_New Returns a new empty dictionary, or NULL on failure.

</div>

<div class="cfuncdesc">

voidPyDict_ClearPyObject \*p Empties an existing dictionary of all key-value pairs.

</div>

<div class="cfuncdesc">

PyObject\*PyDict_CopyPyObject \*p Returns a new dictionary that contains the same key-value pairs as p. Empties an existing dictionary of all key-value pairs.

</div>

<div class="cfuncdesc">

intPyDict_SetItemPyObject \*p, PyObject \*key, PyObject \*val Inserts *value* into the dictionary with a key of *key*. *key* must be hashable; if it isn’t, `TypeError` will be raised.

</div>

<div class="cfuncdesc">

intPyDict_SetItemStringPyDictObject \*p, char \*key, PyObject \*val Inserts *value* into the dictionary using *key* as a key. *key* should be a `char*`. The key object is created using `PyString_FromString(`*`key`*`)`.

</div>

<div class="cfuncdesc">

intPyDict_DelItemPyObject \*p, PyObject \*key Removes the entry in dictionary *p* with key *key*. *key* must be hashable; if it isn’t, `TypeError` is raised.

</div>

<div class="cfuncdesc">

intPyDict_DelItemStringPyObject \*p, char \*key Removes the entry in dictionary *p* which has a key specified by the string *key*.

</div>

<div class="cfuncdesc">

PyObject\*PyDict_GetItemPyObject \*p, PyObject \*key Returns the object from dictionary *p* which has a key *key*. Returns NULL if the key *key* is not present, but *without* setting an exception.

</div>

<div class="cfuncdesc">

PyObject\*PyDict_GetItemStringPyObject \*p, char \*key This is the same as , but *key* is specified as a `char*`, rather than a `PyObject*`.

</div>

<div class="cfuncdesc">

PyObject\*PyDict_ItemsPyObject \*p Returns a `PyListObject` containing all the items from the dictionary, as in the dictinoary method `items()` (see the Python Library Reference).

</div>

<div class="cfuncdesc">

PyObject\*PyDict_KeysPyObject \*p Returns a `PyListObject` containing all the keys from the dictionary, as in the dictionary method `keys()` (see the Python Library Reference).

</div>

<div class="cfuncdesc">

PyObject\*PyDict_ValuesPyObject \*p Returns a `PyListObject` containing all the values from the dictionary *p*, as in the dictionary method `values()` (see the Python Library Reference).

</div>

<div class="cfuncdesc">

intPyDict_SizePyObject \*p Returns the number of items in the dictionary. This is equivalent to `len(`*`p`*`)` on a dictionary.

</div>

<div class="cfuncdesc">

intPyDict_NextPyDictObject \*p, int \*ppos, PyObject \*\*pkey, PyObject \*\*pvalue

</div>

## Numeric Objects <span id="numericObjects" label="numericObjects"></span>

### Plain Integer Objects <span id="intObjects" label="intObjects"></span>

<div class="ctypedesc">

PyIntObject This subtype of `PyObject` represents a Python integer object.

</div>

<div class="cvardesc">

PyTypeObjectPyInt_Type This instance of `PyTypeObject` represents the Python plain integer type. This is the same object as `types.IntType`.

</div>

<div class="cfuncdesc">

intPyInt_CheckPyObject\* o Returns true if *o* is of type .

</div>

<div class="cfuncdesc">

PyObject\*PyInt_FromLonglong ival Creates a new integer object with a value of *ival*.

The current implementation keeps an array of integer objects for all integers between `-1` and `100`, when you create an int in that range you actually just get back a reference to the existing object. So it should be possible to change the value of `1`. I suspect the behaviour of Python in this case is undefined. :-)

</div>

<div class="cfuncdesc">

longPyInt_AsLongPyObject \*io Will first attempt to cast the object to a `PyIntObject`, if it is not already one, and then return its value.

</div>

<div class="cfuncdesc">

longPyInt_AS_LONGPyObject \*io Returns the value of the object *io*. No error checking is performed.

</div>

<div class="cfuncdesc">

longPyInt_GetMax Returns the system’s idea of the largest integer it can handle (, as defined in the system header files).

</div>

### Long Integer Objects <span id="longObjects" label="longObjects"></span>

<div class="ctypedesc">

PyLongObject This subtype of `PyObject` represents a Python long integer object.

</div>

<div class="cvardesc">

PyTypeObjectPyLong_Type This instance of `PyTypeObject` represents the Python long integer type. This is the same object as `types.LongType`.

</div>

<div class="cfuncdesc">

intPyLong_CheckPyObject \*p Returns true if its argument is a `PyLongObject`.

</div>

<div class="cfuncdesc">

PyObject\*PyLong_FromLonglong v Returns a new `PyLongObject` object from *v*, or NULL on failure.

</div>

<div class="cfuncdesc">

PyObject\*PyLong_FromUnsignedLongunsigned long v Returns a new `PyLongObject` object from a C `unsigned long`, or NULL on failure.

</div>

<div class="cfuncdesc">

PyObject\*PyLong_FromDoubledouble v Returns a new `PyLongObject` object from the integer part of *v*, or NULL on failure.

</div>

<div class="cfuncdesc">

longPyLong_AsLongPyObject \*pylong Returns a C `long` representation of the contents of *pylong*. If *pylong* is greater than , an `OverflowError` is raised.

</div>

<div class="cfuncdesc">

unsigned longPyLong_AsUnsignedLongPyObject \*pylong Returns a C `unsigned long` representation of the contents of *pylong*. If *pylong* is greater than , an `OverflowError` is raised.

</div>

<div class="cfuncdesc">

doublePyLong_AsDoublePyObject \*pylong Returns a C `double` representation of the contents of *pylong*.

</div>

<div class="cfuncdesc">

PyObject\*PyLong_FromStringchar \*str, char \*\*pend, int base Return a new `PyLongObject` based on the string value in *str*, which is interpreted according to the radix in *base*. If *pend* is non-NULL, `*`*`pend`* will point to the first character in *str* which follows the representation of the number. If *base* is `0`, the radix will be determined base on the leading characters of *str*: if *str* starts with `’0x’` or `’0X’`, radix 16 will be used; if *str* starts with `’0’`, radix 8 will be used; otherwise radix 10 will be used. If *base* is not `0`, it must be between `2` and `36`, inclusive. Leading spaces are ignored. If there are no digits, `ValueError` will be raised.

</div>

### Floating Point Objects <span id="floatObjects" label="floatObjects"></span>

<div class="ctypedesc">

PyFloatObject This subtype of `PyObject` represents a Python floating point object.

</div>

<div class="cvardesc">

PyTypeObjectPyFloat_Type This instance of `PyTypeObject` represents the Python floating point type. This is the same object as `types.FloatType`.

</div>

<div class="cfuncdesc">

intPyFloat_CheckPyObject \*p Returns true if its argument is a `PyFloatObject`.

</div>

<div class="cfuncdesc">

PyObject\*PyFloat_FromDoubledouble v Creates a `PyFloatObject` object from *v*, or NULL on failure.

</div>

<div class="cfuncdesc">

doublePyFloat_AsDoublePyObject \*pyfloat Returns a C `double` representation of the contents of *pyfloat*.

</div>

<div class="cfuncdesc">

doublePyFloat_AS_DOUBLEPyObject \*pyfloat Returns a C `double` representation of the contents of *pyfloat*, but without error checking.

</div>

### Complex Number Objects <span id="complexObjects" label="complexObjects"></span>

Python’s complex number objects are implemented as two distinct types when viewed from the C API: one is the Python object exposed to Python programs, and the other is a C structure which represents the actual complex number value. The API provides functions for working with both.

#### Complex Numbers as C Structures

Note that the functions which accept these structures as parameters and return them as results do so *by value* rather than dereferencing them through pointers. This is consistent throughout the API.

<div class="ctypedesc">

Py_complex The C structure which corresponds to the value portion of a Python complex number object. Most of the functions for dealing with complex number objects use structures of this type as input or output values, as appropriate. It is defined as:

    typedef struct {
       double real;
       double imag;
    } Py_complex;

</div>

<div class="cfuncdesc">

Py_complex\_Py_c_sumPy_complex left, Py_complex right Return the sum of two complex numbers, using the C `Py_complex` representation.

</div>

<div class="cfuncdesc">

Py_complex\_Py_c_diffPy_complex left, Py_complex right Return the difference between two complex numbers, using the C `Py_complex` representation.

</div>

<div class="cfuncdesc">

Py_complex\_Py_c_negPy_complex complex Return the negation of the complex number *complex*, using the C `Py_complex` representation.

</div>

<div class="cfuncdesc">

Py_complex\_Py_c_prodPy_complex left, Py_complex right Return the product of two complex numbers, using the C `Py_complex` representation.

</div>

<div class="cfuncdesc">

Py_complex\_Py_c_quotPy_complex dividend, Py_complex divisor Return the quotient of two complex numbers, using the C `Py_complex` representation.

</div>

<div class="cfuncdesc">

Py_complex\_Py_c_powPy_complex num, Py_complex exp Return the exponentiation of *num* by *exp*, using the C `Py_complex` representation.

</div>

#### Complex Numbers as Python Objects

<div class="ctypedesc">

PyComplexObject This subtype of `PyObject` represents a Python complex number object.

</div>

<div class="cvardesc">

PyTypeObjectPyComplex_Type This instance of `PyTypeObject` represents the Python complex number type.

</div>

<div class="cfuncdesc">

intPyComplex_CheckPyObject \*p Returns true if its argument is a `PyComplexObject`.

</div>

<div class="cfuncdesc">

PyObject\*PyComplex_FromCComplexPy_complex v Create a new Python complex number object from a C `Py_complex` value.

</div>

<div class="cfuncdesc">

PyObject\*PyComplex_FromDoublesdouble real, double imag Returns a new `PyComplexObject` object from *real* and *imag*.

</div>

<div class="cfuncdesc">

doublePyComplex_RealAsDoublePyObject \*op Returns the real part of *op* as a C `double`.

</div>

<div class="cfuncdesc">

doublePyComplex_ImagAsDoublePyObject \*op Returns the imaginary part of *op* as a C `double`.

</div>

<div class="cfuncdesc">

Py_complexPyComplex_AsCComplexPyObject \*op Returns the `Py_complex` value of the complex number *op*.

</div>

## Other Objects <span id="otherObjects" label="otherObjects"></span>

### File Objects <span id="fileObjects" label="fileObjects"></span>

Python’s built-in file objects are implemented entirely on the `FILE*` support from the C standard library. This is an implementation detail and may change in future releases of Python.

<div class="ctypedesc">

PyFileObject This subtype of `PyObject` represents a Python file object.

</div>

<div class="cvardesc">

PyTypeObjectPyFile_Type This instance of `PyTypeObject` represents the Python file type. This is exposed to Python programs as `types.FileType`.

</div>

<div class="cfuncdesc">

intPyFile_CheckPyObject \*p Returns true if its argument is a `PyFileObject`.

</div>

<div class="cfuncdesc">

PyObject\*PyFile_FromStringchar \*filename, char \*mode On success, returns a new file object that is opened on the file given by *filename*, with a file mode given by *mode*, where *mode* has the same semantics as the standard C routine . On failure, returns NULL.

</div>

<div class="cfuncdesc">

PyObject\*PyFile_FromFileFILE \*fp, char \*name, char \*mode, int (\*close)(FILE\*) Creates a new `PyFileObject` from the already-open standard C file pointer, *fp*. The function *close* will be called when the file should be closed. Returns NULL on failure.

</div>

<div class="cfuncdesc">

FILE\*PyFile_AsFilePyFileObject \*p Returns the file object associated with *p* as a `FILE*`.

</div>

<div class="cfuncdesc">

PyObject\*PyFile_GetLinePyObject \*p, int n Equivalent to *`p`*`.readline()`, this function reads one line from the object *p*. *p* may be a file object or any object with a `readline()` method. If *n* is `0`, exactly one line is read, regardless of the length of the line. If *n* is greater than `0`, no more than *n* bytes will be read from the file; a partial line can be returned. In both cases, an empty string is returned if the end of the file is reached immediately. If *n* is less than `0`, however, one line is read regardless of length, but `EOFError` is raised if the end of the file is reached immediately.

</div>

<div class="cfuncdesc">

PyObject\*PyFile_NamePyObject \*p Returns the name of the file specified by *p* as a string object.

</div>

<div class="cfuncdesc">

voidPyFile_SetBufSizePyFileObject \*p, int n Available on systems with only. This should only be called immediately after file object creation.

</div>

<div class="cfuncdesc">

intPyFile_SoftSpacePyObject \*p, int newflag This function exists for internal use by the interpreter. Sets the `softspace` attribute of *p* to *newflag* and returns the previous value. *p* does not have to be a file object for this function to work properly; any object is supported (thought its only interesting if the `softspace` attribute can be set). This function clears any errors, and will return `0` as the previous value if the attribute either does not exist or if there were errors in retrieving it. There is no way to detect errors from this function, but doing so should not be needed.

</div>

<div class="cfuncdesc">

intPyFile_WriteObjectPyObject \*obj, PyFileObject \*p, int flags Writes object *obj* to file object *p*. The only supported flag for *flags* is ; if given, the `str()` of the object is written instead of the `repr()`. Returns `0` on success or `-1` on failure; the appropriate exception will be set.

</div>

<div class="cfuncdesc">

intPyFile_WriteStringchar \*s, PyFileObject \*p, int flags Writes string *s* to file object *p*. Returns `0` on success or `-1` on failure; the appropriate exception will be set.

</div>

### Module Objects <span id="moduleObjects" label="moduleObjects"></span>

There are only a few functions special to module objects.

<div class="cvardesc">

PyTypeObjectPyModule_Type This instance of `PyTypeObject` represents the Python module type. This is exposed to Python programs as `types.ModuleType`.

</div>

<div class="cfuncdesc">

intPyModule_CheckPyObject \*p Returns true if its argument is a module object.

</div>

<div class="cfuncdesc">

PyObject\*PyModule_Newchar \*name Return a new module object with the `__name__` attribute set to *name*. Only the module’s `__doc__` and `__name__` attributes are filled in; the caller is responsible for providing a `__file__` attribute.

</div>

<div class="cfuncdesc">

PyObject\*PyModule_GetDictPyObject \*module Return the dictionary object that implements *module*’s namespace; this object is the same as the `__dict__` attribute of the module object. This function never fails.

</div>

<div class="cfuncdesc">

char\*PyModule_GetNamePyObject \*module Return *module*’s `__name__` value. If the module does not provide one, or if it is not a string, `SystemError` is raised and NULL is returned.

</div>

<div class="cfuncdesc">

char\*PyModule_GetFilenamePyObject \*module Return the name of the file from which *module* was loaded using *module*’s `__file__` attribute. If this is not defined, or if it is not a string, raise `SystemError` and return NULL.

</div>

<div class="cfuncdesc">

intPyModule_AddObjectPyObject \*module, char \*name, PyObject \*value Add an object to *module* as *name*. This is a convenience function which can be used from the module’s initialization function. This steals a reference to *value*. Returns `-1` on error, `0` on success. *New in version 2.0.*

</div>

<div class="cfuncdesc">

intPyModule_AddIntConstantPyObject \*module, char \*name, int value Add an integer constant to *module* as *name*. This convenience function can be used from the module’s initialization function. Returns `-1` on error, `0` on success. *New in version 2.0.*

</div>

<div class="cfuncdesc">

intPyModule_AddStringConstantPyObject \*module, char \*name, char \*value Add a string constant to *module* as *name*. This convenience function can be used from the module’s initialization function. The string *value* must be null-terminated. Returns `-1` on error, `0` on success. *New in version 2.0.*

</div>

### CObjects <span id="cObjects" label="cObjects"></span>

Refer to *Extending and Embedding the Python Interpreter*, section 1.12 (“Providing a C API for an Extension Module”), for more information on using these objects.

<div class="ctypedesc">

PyCObject This subtype of `PyObject` represents an opaque value, useful for C extension modules who need to pass an opaque value (as a `void*` pointer) through Python code to other C code. It is often used to make a C function pointer defined in one module available to other modules, so the regular import mechanism can be used to access C APIs defined in dynamically loaded modules.

</div>

<div class="cfuncdesc">

intPyCObject_CheckPyObject \*p Returns true if its argument is a `PyCObject`.

</div>

<div class="cfuncdesc">

PyObject\*PyCObject_FromVoidPtrvoid\* cobj, void (\*destr)(void \*) Creates a `PyCObject` from the `void *`*cobj*. The *destr* function will be called when the object is reclaimed, unless it is NULL.

</div>

<div class="cfuncdesc">

PyObject\*PyCObject_FromVoidPtrAndDescvoid\* cobj, void\* desc, void (\*destr)(void \*, void \*) Creates a `PyCObject` from the `void *`*cobj*. The *destr* function will be called when the object is reclaimed. The *desc* argument can be used to pass extra callback data for the destructor function.

</div>

<div class="cfuncdesc">

void\*PyCObject_AsVoidPtrPyObject\* self Returns the object `void *` that the `PyCObject` *self* was created with.

</div>

<div class="cfuncdesc">

void\*PyCObject_GetDescPyObject\* self Returns the description `void *` that the `PyCObject` *self* was created with.

</div>

# Initialization, Finalization, and Threads <span id="initialization" label="initialization"></span>

<div class="cfuncdesc">

voidPy_Initialize Initialize the Python interpreter. In an application embedding Python, this should be called before using any other Python/C API functions; with the exception of , , , and . This initializes the table of loaded modules (`sys.modules`), and creates the fundamental modules `__builtin__`, `__main__`and `sys`. It also initializes the module searchpath (`sys.path`). It does not set `sys.argv`; use for that. This is a no-op when called for a second time (without calling first). There is no return value; it is a fatal error if the initialization fails.

</div>

<div class="cfuncdesc">

intPy_IsInitialized Return true (nonzero) when the Python interpreter has been initialized, false (zero) if not. After is called, this returns false until is called again.

</div>

<div class="cfuncdesc">

voidPy_Finalize Undo all initializations made by and subsequent use of Python/C API functions, and destroy all sub-interpreters (see below) that were created and not yet destroyed since the last call to . Ideally, this frees all memory allocated by the Python interpreter. This is a no-op when called for a second time (without calling again first). There is no return value; errors during finalization are ignored.

This function is provided for a number of reasons. An embedding application might want to restart Python without having to restart the application itself. An application that has loaded the Python interpreter from a dynamically loadable library (or DLL) might want to free all memory allocated by Python before unloading the DLL. During a hunt for memory leaks in an application a developer might want to free all memory allocated by Python before exiting from the application.

**Bugs and caveats:** The destruction of modules and objects in modules is done in random order; this may cause destructors (`__del__()` methods) to fail when they depend on other objects (even functions) or modules. Dynamically loaded extension modules loaded by Python are not unloaded. Small amounts of memory allocated by the Python interpreter may not be freed (if you find a leak, please report it). Memory tied up in circular references between objects is not freed. Some memory allocated by extension modules may not be freed. Some extension may not work properly if their initialization routine is called more than once; this can happen if an applcation calls and more than once.

</div>

<div class="cfuncdesc">

PyThreadState\*Py_NewInterpreter Create a new sub-interpreter. This is an (almost) totally separate environment for the execution of Python code. In particular, the new interpreter has separate, independent versions of all imported modules, including the fundamental modules `__builtin__`, `__main__`and `sys`. The table of loaded modules (`sys.modules`) and the module search path (`sys.path`) are also separate. The new environment has no `sys.argv` variable. It has new standard I/O stream file objects `sys.stdin`, `sys.stdout` and `sys.stderr` (however these refer to the same underlying `FILE` structures in the C library). The return value points to the first thread state created in the new sub-interpreter. This thread state is made the current thread state. Note that no actual thread is created; see the discussion of thread states below. If creation of the new interpreter is unsuccessful, NULL is returned; no exception is set since the exception state is stored in the current thread state and there may not be a current thread state. (Like all other Python/C API functions, the global interpreter lock must be held before calling this function and is still held when it returns; however, unlike most other Python/C API functions, there needn’t be a current thread state on entry.)

Extension modules are shared between (sub-)interpreters as follows: the first time a particular extension is imported, it is initialized normally, and a (shallow) copy of its module’s dictionary is squirreled away. When the same extension is imported by another (sub-)interpreter, a new module is initialized and filled with the contents of this copy; the extension’s `init` function is not called. Note that this is different from what happens when an extension is imported after the interpreter has been completely re-initialized by calling and ; in that case, the extension’s `init`*`module`* function *is* called again.

**Bugs and caveats:** Because sub-interpreters (and the main interpreter) are part of the same process, the insulation between them isn’t perfect — for example, using low-level file operations like `os.close()` they can (accidentally or maliciously) affect each other’s open files. Because of the way extensions are shared between (sub-)interpreters, some extensions may not work properly; this is especially likely when the extension makes use of (static) global variables, or when the extension manipulates its module’s dictionary after its initialization. It is possible to insert objects created in one sub-interpreter into a namespace of another sub-interpreter; this should be done with great care to avoid sharing user-defined functions, methods, instances or classes between sub-interpreters, since import operations executed by such objects may affect the wrong (sub-)interpreter’s dictionary of loaded modules. (XXX This is a hard-to-fix bug that will be addressed in a future release.)

</div>

<div class="cfuncdesc">

voidPy_EndInterpreterPyThreadState \*tstate Destroy the (sub-)interpreter represented by the given thread state. The given thread state must be the current thread state. See the discussion of thread states below. When the call returns, the current thread state is NULL. All thread states associated with this interpreted are destroyed. (The global interpreter lock must be held before calling this function and is still held when it returns.) will destroy all sub-interpreters that haven’t been explicitly destroyed at that point.

</div>

<div class="cfuncdesc">

voidPy_SetProgramNamechar \*name This function should be called before is called for the first time, if it is called at all. It tells the interpreter the value of the `argv[0]` argument to the function of the program. This is used by and some other functions below to find the Python run-time libraries relative to the interpreter executable. The default value is `’python’`. The argument should point to a zero-terminated character string in static storage whose contents will not change for the duration of the program’s execution. No code in the Python interpreter will change the contents of this storage.

</div>

<div class="cfuncdesc">

char\*Py_GetProgramName Return the program name set with , or the default. The returned string points into static storage; the caller should not modify its value.

</div>

<div class="cfuncdesc">

char\*Py_GetPrefix Return the *prefix* for installed platform-independent files. This is derived through a number of complicated rules from the program name set with and some environment variables; for example, if the program name is `’/usr/local/bin/python’`, the prefix is `’/usr/local’`. The returned string points into static storage; the caller should not modify its value. This corresponds to the variable in the top-level `Makefile` and the argument to the script at build time. The value is available to Python code as `sys.prefix`. It is only useful on Unix. See also the next function.

</div>

<div class="cfuncdesc">

char\*Py_GetExecPrefix Return the *exec-prefix* for installed platform-*de*pendent files. This is derived through a number of complicated rules from the program name set with and some environment variables; for example, if the program name is `’/usr/local/bin/python’`, the exec-prefix is `’/usr/local’`. The returned string points into static storage; the caller should not modify its value. This corresponds to the variable in the top-level `Makefile` and the argument to the script at build time. The value is available to Python code as `sys.exec_prefix`. It is only useful on Unix.

Background: The exec-prefix differs from the prefix when platform dependent files (such as executables and shared libraries) are installed in a different directory tree. In a typical installation, platform dependent files may be installed in the `/usr/local/plat` subtree while platform independent may be installed in `/usr/local`.

Generally speaking, a platform is a combination of hardware and software families, e.g. Sparc machines running the Solaris 2.x operating system are considered the same platform, but Intel machines running Solaris 2.x are another platform, and Intel machines running Linux are yet another platform. Different major revisions of the same operating system generally also form different platforms. Non-Unix operating systems are a different story; the installation strategies on those systems are so different that the prefix and exec-prefix are meaningless, and set to the empty string. Note that compiled Python bytecode files are platform independent (but not independent from the Python version by which they were compiled!).

System administrators will know how to configure the or programs to share `/usr/local` between platforms while having `/usr/local/plat` be a different filesystem for each platform.

</div>

<div class="cfuncdesc">

char\*Py_GetProgramFullPath Return the full program name of the Python executable; this is computed as a side-effect of deriving the default module search path from the program name (set by above). The returned string points into static storage; the caller should not modify its value. The value is available to Python code as `sys.executable`.

</div>

<div class="cfuncdesc">

char\*Py_GetPath Return the default module search path; this is computed from the program name (set by above) and some environment variables. The returned string consists of a series of directory names separated by a platform dependent delimiter character. The delimiter character is on Unix, on DOS/Windows, and (the newline character) on Macintosh. The returned string points into static storage; the caller should not modify its value. The value is available to Python code as the list `sys.path`, which may be modified to change the future search path for loaded modules.

</div>

<div class="cfuncdesc">

const char\*Py_GetVersion Return the version of this Python interpreter. This is a string that looks something like

    "1.5 (#67, Dec 31 1997, 22:34:28) [GCC 2.7.2.2]"

The first word (up to the first space character) is the current Python version; the first three characters are the major and minor version separated by a period. The returned string points into static storage; the caller should not modify its value. The value is available to Python code as the list `sys.version`.

</div>

<div class="cfuncdesc">

const char\*Py_GetPlatform Return the platform identifier for the current platform. On Unix, this is formed from the “official” name of the operating system, converted to lower case, followed by the major revision number; e.g., for Solaris 2.x, which is also known as SunOS 5.x, the value is `’sunos5’`. On Macintosh, it is `’mac’`. On Windows, it is `’win’`. The returned string points into static storage; the caller should not modify its value. The value is available to Python code as `sys.platform`.

</div>

<div class="cfuncdesc">

const char\*Py_GetCopyright Return the official copyright string for the current Python version, for example

`’Copyright 1991-1995 Stichting Mathematisch Centrum, Amsterdam’`

The returned string points into static storage; the caller should not modify its value. The value is available to Python code as the list `sys.copyright`.

</div>

<div class="cfuncdesc">

const char\*Py_GetCompiler Return an indication of the compiler used to build the current Python version, in square brackets, for example:

    "[GCC 2.7.2.2]"

The returned string points into static storage; the caller should not modify its value. The value is available to Python code as part of the variable `sys.version`.

</div>

<div class="cfuncdesc">

const char\*Py_GetBuildInfo Return information about the sequence number and build date and time of the current Python interpreter instance, for example

    "#67, Aug  1 1997, 22:34:28"

The returned string points into static storage; the caller should not modify its value. The value is available to Python code as part of the variable `sys.version`.

</div>

<div class="cfuncdesc">

intPySys_SetArgvint argc, char \*\*argv Set `sys.argv` based on *argc* and *argv*. These parameters are similar to those passed to the program’s function with the difference that the first entry should refer to the script file to be executed rather than the executable hosting the Python interpreter. If there isn’t a script that will be run, the first entry in *argv* can be an empty string. If this function fails to initialize `sys.argv`, a fatal condition is signalled using .

</div>

## Thread State and the Global Interpreter Lock <span id="threads" label="threads"></span>

The Python interpreter is not fully thread safe. In order to support multi-threaded Python programs, there’s a global lock that must be held by the current thread before it can safely access Python objects. Without the lock, even the simplest operations could cause problems in a multi-threaded program: for example, when two threads simultaneously increment the reference count of the same object, the reference count could end up being incremented only once instead of twice.

Therefore, the rule exists that only the thread that has acquired the global interpreter lock may operate on Python objects or call Python/C API functions. In order to support multi-threaded Python programs, the interpreter regularly releases and reacquires the lock — by default, every ten bytecode instructions (this can be changed with `sys.setcheckinterval()`). The lock is also released and reacquired around potentially blocking I/O operations like reading or writing a file, so that other threads can run while the thread that requests the I/O is waiting for the I/O operation to complete.

The Python interpreter needs to keep some bookkeeping information separate per thread — for this it uses a data structure called `PyThreadState`. This is new in Python 1.5; in earlier versions, such state was stored in global variables, and switching threads could cause problems. In particular, exception handling is now thread safe, when the application uses `sys.exc_info()` to access the exception last raised in the current thread.

There’s one global variable left, however: the pointer to the current `PyThreadState`structure. While most thread packages have a way to store “per-thread global data,” Python’s internal platform independent thread abstraction doesn’t support this yet. Therefore, the current thread state must be manipulated explicitly.

This is easy enough in most cases. Most code manipulating the global interpreter lock has the following simple structure:

    Save the thread state in a local variable.
    Release the interpreter lock.
    ...Do some blocking I/O operation...
    Reacquire the interpreter lock.
    Restore the thread state from the local variable.

This is so common that a pair of macros exists to simplify it:

    Py_BEGIN_ALLOW_THREADS
    ...Do some blocking I/O operation...
    Py_END_ALLOW_THREADS

The `Py_BEGIN_ALLOW_THREADS`macro opens a new block and declares a hidden local variable; the `Py_END_ALLOW_THREADS`macro closes the block. Another advantage of using these two macros is that when Python is compiled without thread support, they are defined empty, thus saving the thread state and lock manipulations.

When thread support is enabled, the block above expands to the following code:

        PyThreadState *_save;

        _save = PyEval_SaveThread();
        ...Do some blocking I/O operation...
        PyEval_RestoreThread(_save);

Using even lower level primitives, we can get roughly the same effect as follows:

        PyThreadState *_save;

        _save = PyThreadState_Swap(NULL);
        PyEval_ReleaseLock();
        ...Do some blocking I/O operation...
        PyEval_AcquireLock();
        PyThreadState_Swap(_save);

There are some subtle differences; in particular, saves and restores the value of the global variable , since the lock manipulation does not guarantee that is left alone. Also, when thread support is disabled, and don’t manipulate the lock; in this case, and are not available. This is done so that dynamically loaded extensions compiled with thread support enabled can be loaded by an interpreter that was compiled with disabled thread support.

The global interpreter lock is used to protect the pointer to the current thread state. When releasing the lock and saving the thread state, the current thread state pointer must be retrieved before the lock is released (since another thread could immediately acquire the lock and store its own thread state in the global variable). Reversely, when acquiring the lock and restoring the thread state, the lock must be acquired before storing the thread state pointer.

Why am I going on with so much detail about this? Because when threads are created from C, they don’t have the global interpreter lock, nor is there a thread state data structure for them. Such threads must bootstrap themselves into existence, by first creating a thread state data structure, then acquiring the lock, and finally storing their thread state pointer, before they can start using the Python/C API. When they are done, they should reset the thread state pointer, release the lock, and finally free their thread state data structure.

When creating a thread data structure, you need to provide an interpreter state data structure. The interpreter state data structure hold global data that is shared by all threads in an interpreter, for example the module administration (`sys.modules`). Depending on your needs, you can either create a new interpreter state data structure, or share the interpreter state data structure used by the Python main thread (to access the latter, you must obtain the thread state and access its `interp` member; this must be done by a thread that is created by Python or by the main thread after Python is initialized).

<div class="ctypedesc">

PyInterpreterState This data structure represents the state shared by a number of cooperating threads. Threads belonging to the same interpreter share their module administration and a few other internal items. There are no public members in this structure.

Threads belonging to different interpreters initially share nothing, except process state like available memory, open file descriptors and such. The global interpreter lock is also shared by all threads, regardless of to which interpreter they belong.

</div>

<div class="ctypedesc">

PyThreadState This data structure represents the state of a single thread. The only public data member is `PyInterpreterState *``interp`, which points to this thread’s interpreter state.

</div>

<div class="cfuncdesc">

voidPyEval_InitThreads Initialize and acquire the global interpreter lock. It should be called in the main thread before creating a second thread or engaging in any other thread operations such as or `PyEval_ReleaseThread(`*`tstate`*`)`. It is not needed before calling or .

This is a no-op when called for a second time. It is safe to call this function before calling .

When only the main thread exists, no lock operations are needed. This is a common situation (most Python programs do not use threads), and the lock operations slow the interpreter down a bit. Therefore, the lock is not created initially. This situation is equivalent to having acquired the lock: when there is only a single thread, all object accesses are safe. Therefore, when this function initializes the lock, it also acquires it. Before the Python `thread`module creates a new thread, knowing that either it has the lock or the lock hasn’t been created yet, it calls . When this call returns, it is guaranteed that the lock has been created and that it has acquired it.

It is **not** safe to call this function when it is unknown which thread (if any) currently has the global interpreter lock.

This function is not available when thread support is disabled at compile time.

</div>

<div class="cfuncdesc">

voidPyEval_AcquireLock Acquire the global interpreter lock. The lock must have been created earlier. If this thread already has the lock, a deadlock ensues. This function is not available when thread support is disabled at compile time.

</div>

<div class="cfuncdesc">

voidPyEval_ReleaseLock Release the global interpreter lock. The lock must have been created earlier. This function is not available when thread support is disabled at compile time.

</div>

<div class="cfuncdesc">

voidPyEval_AcquireThreadPyThreadState \*tstate Acquire the global interpreter lock and then set the current thread state to *tstate*, which should not be NULL. The lock must have been created earlier. If this thread already has the lock, deadlock ensues. This function is not available when thread support is disabled at compile time.

</div>

<div class="cfuncdesc">

voidPyEval_ReleaseThreadPyThreadState \*tstate Reset the current thread state to NULL and release the global interpreter lock. The lock must have been created earlier and must be held by the current thread. The *tstate* argument, which must not be NULL, is only used to check that it represents the current thread state — if it isn’t, a fatal error is reported. This function is not available when thread support is disabled at compile time.

</div>

<div class="cfuncdesc">

PyThreadState\*PyEval_SaveThread Release the interpreter lock (if it has been created and thread support is enabled) and reset the thread state to NULL, returning the previous thread state (which is not NULL). If the lock has been created, the current thread must have acquired it. (This function is available even when thread support is disabled at compile time.)

</div>

<div class="cfuncdesc">

voidPyEval_RestoreThreadPyThreadState \*tstate Acquire the interpreter lock (if it has been created and thread support is enabled) and set the thread state to *tstate*, which must not be NULL. If the lock has been created, the current thread must not have acquired it, otherwise deadlock ensues. (This function is available even when thread support is disabled at compile time.)

</div>

The following macros are normally used without a trailing semicolon; look for example usage in the Python source distribution.

<div class="csimplemacrodesc">

Py_BEGIN_ALLOW_THREADS This macro expands to `{ PyThreadState *_save; _save = PyEval_SaveThread();`. Note that it contains an opening brace; it must be matched with a following `Py_END_ALLOW_THREADS` macro. See above for further discussion of this macro. It is a no-op when thread support is disabled at compile time.

</div>

<div class="csimplemacrodesc">

Py_END_ALLOW_THREADS This macro expands to `PyEval_RestoreThread(_save); }`. Note that it contains a closing brace; it must be matched with an earlier `Py_BEGIN_ALLOW_THREADS` macro. See above for further discussion of this macro. It is a no-op when thread support is disabled at compile time.

</div>

<div class="csimplemacrodesc">

Py_BEGIN_BLOCK_THREADS This macro expands to `PyEval_RestoreThread(_save);` i.e. it is equivalent to `Py_END_ALLOW_THREADS` without the closing brace. It is a no-op when thread support is disabled at compile time.

</div>

<div class="csimplemacrodesc">

Py_BEGIN_UNBLOCK_THREADS This macro expands to `_save = PyEval_SaveThread();` i.e. it is equivalent to `Py_BEGIN_ALLOW_THREADS` without the opening brace and variable declaration. It is a no-op when thread support is disabled at compile time.

</div>

All of the following functions are only available when thread support is enabled at compile time, and must be called only when the interpreter lock has been created.

<div class="cfuncdesc">

PyInterpreterState\*PyInterpreterState_New Create a new interpreter state object. The interpreter lock need not be held, but may be held if it is necessary to serialize calls to this function.

</div>

<div class="cfuncdesc">

voidPyInterpreterState_ClearPyInterpreterState \*interp Reset all information in an interpreter state object. The interpreter lock must be held.

</div>

<div class="cfuncdesc">

voidPyInterpreterState_DeletePyInterpreterState \*interp Destroy an interpreter state object. The interpreter lock need not be held. The interpreter state must have been reset with a previous call to .

</div>

<div class="cfuncdesc">

PyThreadState\*PyThreadState_NewPyInterpreterState \*interp Create a new thread state object belonging to the given interpreter object. The interpreter lock need not be held, but may be held if it is necessary to serialize calls to this function.

</div>

<div class="cfuncdesc">

voidPyThreadState_ClearPyThreadState \*tstate Reset all information in a thread state object. The interpreter lock must be held.

</div>

<div class="cfuncdesc">

voidPyThreadState_DeletePyThreadState \*tstate Destroy a thread state object. The interpreter lock need not be held. The thread state must have been reset with a previous call to .

</div>

<div class="cfuncdesc">

PyThreadState\*PyThreadState_Get Return the current thread state. The interpreter lock must be held. When the current thread state is NULL, this issues a fatal error (so that the caller needn’t check for NULL).

</div>

<div class="cfuncdesc">

PyThreadState\*PyThreadState_SwapPyThreadState \*tstate Swap the current thread state with the thread state given by the argument *tstate*, which may be NULL. The interpreter lock must be held.

</div>

# Memory Management <span id="memory" label="memory"></span>

## Overview <span id="memoryOverview" label="memoryOverview"></span>

Memory management in Python involves a private heap containing all Python objects and data structures. The management of this private heap is ensured internally by the *Python memory manager*. The Python memory manager has different components which deal with various dynamic storage management aspects, like sharing, segmentation, preallocation or caching.

At the lowest level, a raw memory allocator ensures that there is enough room in the private heap for storing all Python-related data by interacting with the memory manager of the operating system. On top of the raw memory allocator, several object-specific allocators operate on the same heap and implement distinct memory management policies adapted to the peculiarities of every object type. For example, integer objects are managed differently within the heap than strings, tuples or dictionaries because integers imply different storage requirements and speed/space tradeoffs. The Python memory manager thus delegates some of the work to the object-specific allocators, but ensures that the latter operate within the bounds of the private heap.

It is important to understand that the management of the Python heap is performed by the interpreter itself and that the user has no control on it, even if she regularly manipulates object pointers to memory blocks inside that heap. The allocation of heap space for Python objects and other internal buffers is performed on demand by the Python memory manager through the Python/C API functions listed in this document.

To avoid memory corruption, extension writers should never try to operate on Python objects with the functions exported by the C library: , , and . This will result in mixed calls between the C allocator and the Python memory manager with fatal consequences, because they implement different algorithms and operate on different heaps. However, one may safely allocate and release memory blocks with the C library allocator for individual purposes, as shown in the following example:

        PyObject *res;
        char *buf = (char *) malloc(BUFSIZ); /* for I/O */

        if (buf == NULL)
            return PyErr_NoMemory();
        ...Do some I/O operation involving buf...
        res = PyString_FromString(buf);
        free(buf); /* malloc'ed */
        return res;

In this example, the memory request for the I/O buffer is handled by the C library allocator. The Python memory manager is involved only in the allocation of the string object returned as a result.

In most situations, however, it is recommended to allocate memory from the Python heap specifically because the latter is under control of the Python memory manager. For example, this is required when the interpreter is extended with new object types written in C. Another reason for using the Python heap is the desire to *inform* the Python memory manager about the memory needs of the extension module. Even when the requested memory is used exclusively for internal, highly-specific purposes, delegating all memory requests to the Python memory manager causes the interpreter to have a more accurate image of its memory footprint as a whole. Consequently, under certain circumstances, the Python memory manager may or may not trigger appropriate actions, like garbage collection, memory compaction or other preventive procedures. Note that by using the C library allocator as shown in the previous example, the allocated memory for the I/O buffer escapes completely the Python memory manager.

## Memory Interface <span id="memoryInterface" label="memoryInterface"></span>

The following function sets, modeled after the ANSI C standard, are available for allocating and releasing memory from the Python heap:

<div class="cfuncdesc">

void\*PyMem_Mallocsize_t n Allocates *n* bytes and returns a pointer of type `void*` to the allocated memory, or NULL if the request fails. Requesting zero bytes returns a non-NULL pointer.

</div>

<div class="cfuncdesc">

void\*PyMem_Reallocvoid \*p, size_t n Resizes the memory block pointed to by *p* to *n* bytes. The contents will be unchanged to the minimum of the old and the new sizes. If *p* is NULL, the call is equivalent to ; if *n* is equal to zero, the memory block is resized but is not freed, and the returned pointer is non-NULL. Unless *p* is NULL, it must have been returned by a previous call to or .

</div>

<div class="cfuncdesc">

voidPyMem_Freevoid \*p Frees the memory block pointed to by *p*, which must have been returned by a previous call to or . Otherwise, or if has been called before, undefined behaviour occurs. If *p* is NULL, no operation is performed.

</div>

The following type-oriented macros are provided for convenience. Note that *TYPE* refers to any C type.

<div class="cfuncdesc">

*TYPE*\*PyMem_NewTYPE, size_t n Same as , but allocates `(`*`n`*` * sizeof(`*`TYPE`*`))` bytes of memory. Returns a pointer cast to *`TYPE`*`*`.

</div>

<div class="cfuncdesc">

*TYPE*\*PyMem_Resizevoid \*p, TYPE, size_t n Same as , but the memory block is resized to `(`*`n`*` * sizeof(`*`TYPE`*`))` bytes. Returns a pointer cast to *`TYPE`*`*`.

</div>

<div class="cfuncdesc">

voidPyMem_Delvoid \*p Same as .

</div>

In addition, the following macro sets are provided for calling the Python memory allocator directly, without involving the C API functions listed above. However, note that their use does not preserve binary compatibility accross Python versions and is therefore deprecated in extension modules.

, , .

, , .

## Examples <span id="memoryExamples" label="memoryExamples"></span>

Here is the example from section <a href="#memoryOverview" data-reference-type="ref" data-reference="memoryOverview">[memoryOverview]</a>, rewritten so that the I/O buffer is allocated from the Python heap by using the first function set:

        PyObject *res;
        char *buf = (char *) PyMem_Malloc(BUFSIZ); /* for I/O */

        if (buf == NULL)
            return PyErr_NoMemory();
        /* ...Do some I/O operation involving buf... */
        res = PyString_FromString(buf);
        PyMem_Free(buf); /* allocated with PyMem_Malloc */
        return res;

The same code using the type-oriented function set:

        PyObject *res;
        char *buf = PyMem_New(char, BUFSIZ); /* for I/O */

        if (buf == NULL)
            return PyErr_NoMemory();
        /* ...Do some I/O operation involving buf... */
        res = PyString_FromString(buf);
        PyMem_Del(buf); /* allocated with PyMem_New */
        return res;

Note that in the two examples above, the buffer is always manipulated via functions belonging to the same set. Indeed, it is required to use the same memory API family for a given memory block, so that the risk of mixing different allocators is reduced to a minimum. The following code sequence contains two errors, one of which is labeled as *fatal* because it mixes two different allocators operating on different heaps.

    char *buf1 = PyMem_New(char, BUFSIZ);
    char *buf2 = (char *) malloc(BUFSIZ);
    char *buf3 = (char *) PyMem_Malloc(BUFSIZ);
    ...
    PyMem_Del(buf3);  /* Wrong -- should be PyMem_Free() */
    free(buf2);       /* Right -- allocated via malloc() */
    free(buf1);       /* Fatal -- should be PyMem_Del()  */

In addition to the functions aimed at handling raw memory blocks from the Python heap, objects in Python are allocated and released with , and , or with their corresponding macros , and .

These will be explained in the next chapter on defining and implementing new object types in C.

# Defining New Object Types <span id="newTypes" label="newTypes"></span>

<div class="cfuncdesc">

PyObject\*\_PyObject_NewPyTypeObject \*type

</div>

<div class="cfuncdesc">

PyVarObject\*\_PyObject_NewVarPyTypeObject \*type, int size

</div>

<div class="cfuncdesc">

void\_PyObject_DelPyObject \*op

</div>

<div class="cfuncdesc">

PyObject\*PyObject_InitPyObject \*op, PyTypeObject \*type

</div>

<div class="cfuncdesc">

PyVarObject\*PyObject_InitVarPyVarObject \*op, PyTypeObject \*type, int size

</div>

<div class="cfuncdesc">

*TYPE*\*PyObject_NewTYPE, PyTypeObject \*type

</div>

<div class="cfuncdesc">

*TYPE*\*PyObject_NewVarTYPE, PyTypeObject \*type, int size

</div>

<div class="cfuncdesc">

voidPyObject_DelPyObject \*op

</div>

<div class="cfuncdesc">

*TYPE*\*PyObject_NEWTYPE, PyTypeObject \*type

</div>

<div class="cfuncdesc">

*TYPE*\*PyObject_NEW_VARTYPE, PyTypeObject \*type, int size

</div>

<div class="cfuncdesc">

voidPyObject_DELPyObject \*op

</div>

Py_InitModule (!!!)

PyArg_ParseTupleAndKeywords, PyArg_ParseTuple, PyArg_Parse

Py_BuildValue

DL_IMPORT

Py\*\_Check

\_Py_NoneStruct

## Common Object Structures <span id="common-structs" label="common-structs"></span>

PyObject, PyVarObject

PyObject_HEAD, PyObject_HEAD_INIT, PyObject_VAR_HEAD

Typedefs: unaryfunc, binaryfunc, ternaryfunc, inquiry, coercion, intargfunc, intintargfunc, intobjargproc, intintobjargproc, objobjargproc, destructor, printfunc, getattrfunc, getattrofunc, setattrfunc, setattrofunc, cmpfunc, reprfunc, hashfunc

<div class="ctypedesc">

PyCFunction Type of the functions used to implement most Python callables in C.

</div>

<div class="ctypedesc">

PyMethodDef Structure used to describe a method of an extension type. This structure has four fields:

|  |  |  |
|:---|:---|:---|
| FieldC TypeMeaning ml_name | char \* | name of the method |
| ml_meth | PyCFunction | pointer to the C implementation |
| ml_flags | int | flag bits indicating how the call should be constructed |
| ml_doc | char \* | points to the contents of the docstring |
|  |  |  |

</div>

<div class="cfuncdesc">

PyObject\*Py_FindMethodPyMethodDef\[\] table, PyObject \*ob, char \*name Return a bound method object for an extension type implemented in C. This function also handles the special attribute `__methods__`, returning a list of all the method names defined in *table*.

</div>

## Mapping Object Structures <span id="mapping-structs" label="mapping-structs"></span>

<div class="ctypedesc">

PyMappingMethods Structure used to hold pointers to the functions used to implement the mapping protocol for an extension type.

</div>

## Number Object Structures <span id="number-structs" label="number-structs"></span>

<div class="ctypedesc">

PyNumberMethods Structure used to hold pointers to the functions an extension type uses to implement the number protocol.

</div>

## Sequence Object Structures <span id="sequence-structs" label="sequence-structs"></span>

<div class="ctypedesc">

PySequenceMethods Structure used to hold pointers to the functions which an object uses to implement the sequence protocol.

</div>

## Buffer Object Structures <span id="buffer-structs" label="buffer-structs"></span>

The buffer interface exports a model where an object can expose its internal data as a set of chunks of data, where each chunk is specified as a pointer/length pair. These chunks are called *segments* and are presumed to be non-contiguous in memory.

If an object does not export the buffer interface, then its `tp_as_buffer` member in the `PyTypeObject` structure should be NULL. Otherwise, the `tp_as_buffer` will point to a `PyBufferProcs` structure.

**Note:** It is very important that your `PyTypeObject` structure uses `Py_TPFLAGS_DEFAULT` for the value of the `tp_flags` member rather than `0`. This tells the Python runtime that your `PyBufferProcs` structure contains the `bf_getcharbuffer` slot. Older versions of Python did not have this member, so a new Python interpreter using an old extension needs to be able to test for its presence before using it.

<div class="ctypedesc">

PyBufferProcs Structure used to hold the function pointers which define an implementation of the buffer protocol.

The first slot is `bf_getreadbuffer`, of type `getreadbufferproc`. If this slot is NULL, then the object does not support reading from the internal data. This is non-sensical, so implementors should fill this in, but callers should test that the slot contains a non-NULL value.

The next slot is `bf_getwritebuffer` having type `getwritebufferproc`. This slot may be NULL if the object does not allow writing into its returned buffers.

The third slot is `bf_getsegcount`, with type `getsegcountproc`. This slot must not be NULL and is used to inform the caller how many segments the object contains. Simple objects such as `PyString_Type` and `PyBuffer_Type` objects contain a single segment.

The last slot is `bf_getcharbuffer`, of type `getcharbufferproc`. This slot will only be present if the `Py_TPFLAGS_HAVE_GETCHARBUFFER` flag is present in the `tp_flags` field of the object’s `PyTypeObject`. Before using this slot, the caller should test whether it is present by using the function. If present, it may be NULL, indicating that the object’s contents cannot be used as *8-bit characters*. The slot function may also raise an error if the object’s contents cannot be interpreted as 8-bit characters. For example, if the object is an array which is configured to hold floating point values, an exception may be raised if a caller attempts to use `bf_getcharbuffer` to fetch a sequence of 8-bit characters. This notion of exporting the internal buffers as “text” is used to distinguish between objects that are binary in nature, and those which have character-based content.

**Note:** The current policy seems to state that these characters may be multi-byte characters. This implies that a buffer size of *N* does not mean there are *N* characters present.

</div>

<div class="datadesc">

Py_TPFLAGS_HAVE_GETCHARBUFFER Flag bit set in the type structure to indicate that the `bf_getcharbuffer` slot is known. This being set does not indicate that the object supports the buffer interface or that the `bf_getcharbuffer` slot is non-NULL.

</div>

<div class="ctypedesc">

int (\*getreadbufferproc) (PyObject \*self, int segment, void \*\*ptrptr) Return a pointer to a readable segment of the buffer. This function is allowed to raise an exception, in which case it must return `-1`. The *segment* which is passed must be zero or positive, and strictly less than the number of segments returned by the `bf_getsegcount` slot function. On success, returns `0` and sets `*`*`ptrptr`* to a pointer to the buffer memory.

</div>

<div class="ctypedesc">

int (\*getwritebufferproc) (PyObject \*self, int segment, void \*\*ptrptr) Return a pointer to a writable memory buffer in `*`*`ptrptr`*; the memory buffer must correspond to buffer segment *segment*. Must return `-1` and set an exception on error. `TypeError` should be raised if the object only supports read-only buffers, and `SystemError` should be raised when *segment* specifies a segment that doesn’t exist.

</div>

<div class="ctypedesc">

int (\*getsegcountproc) (PyObject \*self, int \*lenp) Return the number of memory segments which comprise the buffer. If *lenp* is not NULL, the implementation must report the sum of the sizes (in bytes) of all segments in `*`*`lenp`*. The function cannot fail.

</div>

<div class="ctypedesc">

int (\*getcharbufferproc) (PyObject \*self, int segment, const char \*\*ptrptr)

</div>

# Reporting Bugs


{{< python-copyright version="2.0b2" >}}
