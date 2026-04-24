---
title: "Library Reference"
weight: 20
---

# Standard Module `aifc`

This module provides support for reading and writing AIFF and AIFF-C files. AIFF is Audio Interchange File Format, a format for storing digital audio samples in a file. AIFF-C is a newer version of the format that includes the ability to compress the audio data.

Audio files have a number of parameters that describe the audio data. The sampling rate or frame rate is the number of times per second the sound is sampled. The number of channels indicate if the audio is mono, stereo, or quadro. Each frame consists of one sample per channel. The sample size is the size in bytes of each sample. Thus a frame consists of nchannels*framesize bytes, and a second’s worth of audio consists of nchannels*framesize*framerate bytes.

Module `aifc` defines the following function:

### `open`(file  mode)

Opens an AIFF or AIFF-C file and returns an object instance with methods that are described below. The argument file is either a string naming a file or a file object. The mode is either the string ’r’ when the file must be opened for reading, or ’w’ when the file must be opened for writing.

Objects returned by `aifc.open()` when a file is opened for reading have the following methods:

### `getnchannels`()

Return the number of audio channels (1 for mono, 2 for stereo).

### `getsampwidth`()

Return the size in bytes of individual samples.

### `getframerate`()

Return the sampling rate (number of audio frames per second).

### `getnframes`()

Return the number of audio frames in the file.

### `getcomptype`()

Return a four-character string describing the type of compression used in the audio file. For AIFF files, the returned value is `’NONE’`.

### `getcompname`()

Return a human-readable description of the type of compression used in the audio file. For AIFF files, the returned value is `’not compressed’`.

### `getparams`()

Return a tuple consisting of all of the above values in the above order.

### `getmarkers`()

Return a list of markers in the audio file. A marker consists of a tuple of three elements. The first is the mark ID (an integer), the second is the mark position in frames from the beginning of the data (an integer), the third is the name of the mark (a string).

### `getmark`(id)

Return the tuple as described in `getmarkers` for the mark with the given id.

### `readframes`(nframes)

Read and return the next nframes frames from the audio file. The returned data is a string containing for each frame the uncompressed samples of all channels.

### `rewind`()

Rewind the read pointer. The next `readframes` will start from the beginning.

### `setpos`(pos)

Seek to the specified frame number.

### `tell`()

Return the current frame number.

### `close`()

Close the AIFF file. After calling this method, the object can no longer be used.

Objects returned by `aifc.open()` when a file is opened for writing have all the above methods, except for `readframes` and `setpos`. In addition the following methods exist. The `get` methods can only be called after the corresponding `set` methods have been called. Before the first `writeframes` or `writeframesraw`, all parameters except for the number of frames must be filled in.

### `aiff`()

Create an AIFF file. The default is that an AIFF-C file is created, unless the name of the file ends in ’.aiff’ in which case the default is an AIFF file.

### `aifc`()

Create an AIFF-C file. The default is that an AIFF-C file is created, unless the name of the file ends in ’.aiff’ in which case the default is an AIFF file.

### `setnchannels`(nchannels)

Specify the number of channels in the audio file.

### `setsampwidth`(width)

Specify the size in bytes of audio samples.

### `setframerate`(rate)

Specify the sampling frequency in frames per second.

### `setnframes`(nframes)

Specify the number of frames that are to be written to the audio file. If this parameter is not set, or not set correctly, the file needs to support seeking.

### `setcomptype`(type  name)

Specify the compression type. If not specified, the audio data will not be compressed. In AIFF files, compression is not possible. The name parameter should be a human-readable description of the compression type, the type parameter should be a four-character string. Currently the following compression types are supported: NONE, ULAW, ALAW, G722.

### `setparams`((nchannels  sampwidth  framerate  comptype  compname))

Set all the above parameters at once. The argument is a tuple consisting of the various parameters. This means that it is possible to use the result of a `getparams` call as argument to `setparams`.

### `setmark`(id  pos  name)

Add a mark with the given id (larger than 0), and the given name at the given position. This method can be called at any time before `close`.

### `tell`()

Return the current write position in the output file. Useful in combination with `setmark`.

### `writeframes`(data)

Write data to the output file. This method can only be called after the audio file parameters have been set.

### `writeframesraw`(data)

Like `writeframes`, except that the header of the audio file is not updated.

### `close`()

Close the AIFF file. The header of the file is updated to reflect the actual size of the audio data After calling this method, the object can no longer be used.
# Built-in Module `al`

This module provides access to the audio facilities of the Indigo and 4D/35 workstations, described in section 3A of the IRIX 4.0 man pages (and also available as an option in IRIX 3.3). You’ll need to read those man pages to understand what these functions do! Some of the functions are not available in releases below 4.0.5. Again, see the manual to check whether a specific function is available on your platform.

Symbolic constants from the C header file `<audio.h>` are defined in the standard module `AL`, see below.

**Warning:** the current version of the audio library may dump core when bad argument values are passed rather than returning an error status. Unfortunately, since the precise circumstances under which this may happen are undocumented and hard to check, the Python interface can provide no protection against this kind of problems. (One example is specifying an excessive queue size — there is no documented upper limit.)

Module `al` defines the following functions:

### `openport`(name  direction)

Equivalent to the C function ALopenport(). The name and direction arguments are strings. The optional config argument is an opaque configuration object as returned by `al.newconfig()`. The return value is an opaque port object; methods of port objects are described below.

### `newconfig`()

Equivalent to the C function ALnewconfig(). The return value is a new opaque configuration object; methods of configuration objects are described below.

### `queryparams`(device)

Equivalent to the C function ALqueryparams(). The device argument is an integer. The return value is a list of integers containing the data returned by ALqueryparams().

### `getparams`(device  list)

Equivalent to the C function ALgetparams(). The device argument is an integer. The list argument is a list such as returned by `queryparams`; it is modified in place (!).

### `setparams`(device  list)

Equivalent to the C function ALsetparams(). The device argument is an integer.The list argument is a list such as returned by `al.queryparams`.

Configuration objects (returned by `al.newconfig()` have the following methods:

### `getqueuesize`()

Return the queue size; equivalent to the C function ALgetqueuesize().

### `setqueuesize`(size)

Set the queue size; equivalent to the C function ALsetqueuesize().

### `getwidth`()

Get the sample width; equivalent to the C function ALgetwidth().

### `getwidth`(width)

Set the sample width; equivalent to the C function ALsetwidth().

### `getchannels`()

Get the channel count; equivalent to the C function ALgetchannels().

### `setchannels`(nchannels)

Set the channel count; equivalent to the C function ALsetchannels().

### `getsampfmt`()

Get the sample format; equivalent to the C function ALgetsampfmt().

### `setsampfmt`(sampfmt)

Set the sample format; equivalent to the C function ALsetsampfmt().

### `getfloatmax`()

Get the maximum value for floating sample formats; equivalent to the C function ALgetfloatmax().

### `setfloatmax`(floatmax)

Set the maximum value for floating sample formats; equivalent to the C function ALsetfloatmax().

Port objects (returned by `al.openport()` have the following methods:

### `closeport`()

Close the port; equivalent to the C function ALcloseport().

### `getfd`()

Return the file descriptor as an int; equivalent to the C function ALgetfd().

### `getfilled`()

Return the number of filled samples; equivalent to the C function ALgetfilled().

### `getfillable`()

Return the number of fillable samples; equivalent to the C function ALgetfillable().

### `readsamps`(nsamples)

Read a number of samples from the queue, blocking if necessary; equivalent to the C function ALreadsamples. The data is returned as a string containing the raw data (e.g. 2 bytes per sample in big-endian byte order (high byte, low byte) if you have set the sample width to 2 bytes.

### `writesamps`(samples)

Write samples into the queue, blocking if necessary; equivalent to the C function ALwritesamples. The samples are encoded as described for the `readsamps` return value.

### `getfillpoint`()

Return the ‘fill point’; equivalent to the C function ALgetfillpoint().

### `setfillpoint`(fillpoint)

Set the ‘fill point’; equivalent to the C function ALsetfillpoint().

### `getconfig`()

Return a configuration object containing the current configuration of the port; equivalent to the C function ALgetconfig().

### `setconfig`(config)

Set the configuration from the argument, a configuration object; equivalent to the C function ALsetconfig().

### `getstatus`(list)

Get status information on last error equivalent to C function ALgetstatus().

# Standard Module `AL`

This module defines symbolic constants needed to use the built-in module `al` (see above); they are equivalent to those defined in the C header file `<audio.h>` except that the name prefix `AL_` is omitted. Read the module source for a complete list of the defined names. Suggested use:

    import al
    from AL import *
# AMOEBA ONLY

## Built-in Module `amoeba`

This module provides some object types and operations useful for Amoeba applications. It is only available on systems that support Amoeba operations. RPC errors and other Amoeba errors are reported as the exception `amoeba.error = ’amoeba.error’`.

The module `amoeba` defines the following items:

#### `name_append`(path  cap)

Stores a capability in the Amoeba directory tree. Arguments are the pathname (a string) and the capability (a capability object as returned by `name_lookup()`).

#### `name_delete`(path)

Deletes a capability from the Amoeba directory tree. Argument is the pathname.

#### `name_lookup`(path)

Looks up a capability. Argument is the pathname. Returns a *capability* object, to which various interesting operations apply, described below.

#### `name_replace`(path  cap)

Replaces a capability in the Amoeba directory tree. Arguments are the pathname and the new capability. (This differs from `name_append()` in the behavior when the pathname already exists: `name_append()` finds this an error while `name_replace()` allows it, as its name suggests.)

#### `capv`

A table representing the capability environment at the time the interpreter was started. (Alas, modifying this table does not affect the capability environment of the interpreter.) For example, `amoeba.capv[’ROOT’]` is the capability of your root directory, similar to `getcap("ROOT")` in C.

#### exception `error`

The exception raised when an Amoeba function returns an error. The value accompanying this exception is a pair containing the numeric error code and the corresponding string, as returned by the C function `err_why()`.

#### `timeout`(msecs)

Sets the transaction timeout, in milliseconds. Returns the previous timeout. Initially, the timeout is set to 2 seconds by the Python interpreter.

### Capability Operations

Capabilities are written in a convenient ASCII format, also used by the Amoeba utilities *c2a*(U) and *a2c*(U). For example:

    >>> amoeba.name_lookup('/profile/cap')
    aa:1c:95:52:6a:fa/14(ff)/8e:ba:5b:8:11:1a
    >>> 

The following methods are defined for capability objects.

#### `dir_list`()

Returns a list of the names of the entries in an Amoeba directory.

#### `b_read`(offset  maxsize)

Reads (at most) *maxsize* bytes from a bullet file at offset *offset.* The data is returned as a string. EOF is reported as an empty string.

#### `b_size`()

Returns the size of a bullet file.

#### `dir_append`()

   Like the corresponding `name_`* functions, but with a path relative to the capability. (For paths beginning with a slash the capability is ignored, since this is the defined semantics for Amoeba.)

#### `std_info`()

Returns the standard info string of the object.

#### `tod_gettime`()

Returns the time (in seconds since the Epoch, in UCT, as for POSIX) from a time server.

#### `tod_settime`(t)

Sets the time kept by a time server.
# Built-in module `array`

This module defines a new object type which can efficiently represent an array of basic values: characters, integers, floating point numbers. Arrays are sequence types and behave very much like lists, except that the type of objects stored in them is constrained. The type is specified at object creation time by using a *type code*, which is a single character. The following type codes are defined:

|     |                |     |
|:----|:---------------|:----|
| ’c’ | character      | 1   |
| ’b’ | signed integer | 1   |
| ’h’ | signed integer | 2   |
| ’i’ | signed integer | 2   |
| ’l’ | signed integer | 4   |
| ’f’ | floating point | 4   |
| ’d’ | floating point | 8   |

The actual representation of values is determined by the machine architecture (strictly speaking, by the C implementation). The actual size can be accessed through the *typecode* attribute.

The module defines the following function:

### `array`(typecode)

Return a new array whose items are restricted by *typecode*, and initialized from the optional *initializer* value, which must be a list or a string. The list or string is passed to the new array’s `fromlist()` or `fromstring()` method (see below) to add initial items to the array.

Array objects support the following data items and methods:

### `typecode`

The typecode character used to create the array.

### `itemsize`

The length in bytes of one array item in the internal representation.

### `append`(x)

Append a new item with value *x* to the end of the array.

### `byteswap`(x)

“Byteswap” all items of the array. This is only supported for integer values. It is useful when reading data from a file written on a machine with a different byte order.

### `fromfile`(f  n)

Read *n* items (as machine values) from the file object *f* and append them to the end of the array. If less than *n* items are available, `EOFError` is raised, but the items that were available are still inserted into the array.

### `fromlist`(list)

Appends items from the list. This is equivalent to `for x in `*`list`*`: a.append(x)` except that if there is a type error, the array is unchanged.

### `fromstring`(s)

Appends items from the string, interpreting the string as an array of machine values (i.e. as if it had been read from a file using the `fromfile()` method).

### `insert`(i  x)

Insert a new item with value *x* in the array before position *i*.

### `tofile`(f)

Write all items (as machine values) to the file object *f*.

### `tolist`()

Convert the array to an ordinary list with the same items.

### `tostring`()

Convert the array to an array of machine values and return the string representation (the same sequence of bytes that would be written to a file by the `tofile()` method.)

When an array object is printed or converted to a string, it is represented as `array(`*`typecode`*`, `*`initializer`*`)`. The *initializer* is omitted if the array is empty, otherwise it is a string if the *typecode* is `’c’`, otherwise it is a list of numbers. The string is guaranteed to be able to be converted back to an array with the same type and value using reverse quotes (`‘‘`). Examples:

    array('l')
    array('c', 'hello world')
    array('l', [1, 2, 3, 4, 5])
    array('d', [1.0, 2.0, 3.14])
# Built-in Module `audio`

**Note:** This module is obsolete, since the hardware to which it interfaces is obsolete. For audio on the Indigo or 4D/35, see built-in module `al` above.

This module provides rudimentary access to the audio I/O device `/dev/audio` on the Silicon Graphics Personal IRIS 4D/25; see *audio*(7). It supports the following operations:

### `setoutgain`(n)

Sets the output gain. `0 <= `*`n`*` < 256`. ≤ n \< 256.

### `getoutgain`()

Returns the output gain.

### `setrate`(n)

Sets the sampling rate: `1` = 32K/sec, `2` = 16K/sec, `3` = 8K/sec.

### `setduration`(n)

Sets the ‘sound duration’ in units of 1/100 seconds.

### `read`(n)

Reads a chunk of *n* sampled bytes from the audio input (line in or microphone). The chunk is returned as a string of length n. Each byte encodes one sample as a signed 8-bit quantity using linear encoding. This string can be converted to numbers using `chr2num()` described below.

### `write`(buf)

Writes a chunk of samples to the audio output (speaker).

These operations support asynchronous audio I/O:

### `start_recording`(n)

Starts a second thread (a process with shared memory) that begins reading *n* bytes from the audio device. The main thread immediately continues.

### `wait_recording`()

Waits for the second thread to finish and returns the data read.

### `stop_recording`()

Makes the second thread stop reading as soon as possible. Returns the data read so far.

### `poll_recording`()

Returns true if the second thread has finished reading (so `wait_recording()` would return the data without delay).

### `start_playing`()

Similar but for output. `stop_playing()` returns a lower bound for the number of bytes actually played (not very accurate).

The following operations do not affect the audio device but are implemented in C for efficiency:

### `amplify`(buf  f1  f2)

Amplifies a chunk of samples by a variable factor changing from *`f1`*`/256` to *`f2`*`/256.` Negative factors are allowed. Resulting values that are to large to fit in a byte are clipped.

### `reverse`(buf)

Returns a chunk of samples backwards.

### `add`(buf1  buf2)

Bytewise adds two chunks of samples. Bytes that exceed the range are clipped. If one buffer is shorter, it is assumed to be padded with zeros.

### `chr2num`(buf)

Converts a string of sampled bytes as returned by `read()` into a list containing the numeric values of the samples.

### `num2chr`(list)

Converts a list as returned by `chr2num()` back to a buffer acceptable by `write()`.
# Built-in module `audioop`

The audioop module contains some useful operations on sound fragments. It operates on sound fragments consisting of signed integer samples of 8, 16 or 32 bits wide, stored in Python strings. This is the same format as used by the `al` and `sunaudiodev` modules. All scalar items are integers, unless specified otherwise.

A few of the more complicated operations only take 16-bit samples, otherwise the sample size (in bytes) is always a parameter of the operation.

The module defines the following variables and functions:

### exception `error`

This exception is raised on all errors, such as unknown number of bytes per sample, etc.

### `add`(fragment1  fragment2  width)

This function returns a fragment that is the addition of the two samples passed as parameters. *width* is the sample width in bytes, either `1`, `2` or `4`. Both fragments should have the same length.

### `adpcm2lin`(adpcmfragment  width  state)

This routine decodes an Intel/DVI ADPCM coded fragment to a linear fragment. See the description of `lin2adpcm` for details on ADPCM coding. The routine returns a tuple `(`*`sample`*`, `*`newstate`*`)` where the sample has the width specified in *width*.

### `adpcm32lin`(adpcmfragment  width  state)

This routine decodes an alternative 3-bit ADPCM code. See `lin2adpcm3` for details.

### `avg`(fragment  width)

This function returns the average over all samples in the fragment.

### `avgpp`(fragment  width)

This function returns the average peak-peak value over all samples in the fragment. No filtering is done, so the usefulness of this routine is questionable.

### `bias`(fragment  width  bias)

This function returns a fragment that is the original fragment with a bias added to each sample.

### `cross`(fragment  width)

This function returns the number of zero crossings in the fragment passed as an argument.

### `findfactor`(fragment  reference)

This routine (which only accepts 2-byte sample fragments) calculates a factor *F* such that `rms(add(fragment, mul(reference, -F)))` is minimal, i.e. it calculates the factor with which you should multiply *reference* to make it match as good as possible to *fragment*. The fragments should be the same size.

The time taken by this routine is proportional to `len(fragment)`.

### `findfit`(fragment  reference)

This routine (which only accepts 2-byte sample fragments) tries to match *reference* as good as possible to a portion of *fragment* (which should be the longer fragment). It (conceptually) does this by taking slices out of *fragment*, using `findfactor` to compute the best match, and minimizing the result. It returns a tuple `(`*`offset`*`, `*`factor`*`)` with *offset* the (integer) offset into *fragment* where the optimal match started and *factor* the floating-point factor as per `findfactor`.

### `findmax`(fragment  length)

This routine (which only accepts 2-byte sample fragments) searches *fragment* for a slice of length *length* samples (not bytes!) with maximum energy, i.e. it returns *i* for which `rms(fragment[i*2:(i+length)*2])` is maximal.

The routine takes time proportional to `len(fragment)`.

### `getsample`(fragment  width  index)

This function returns the value of sample *index* from the fragment.

### `lin2lin`(fragment  width  newwidth)

This function converts samples between 1-, 2- and 4-byte formats.

### `lin2adpcm`(fragment  width  state)

This function converts samples to 4 bit Intel/DVI ADPCM encoding. ADPCM coding is an adaptive coding scheme, whereby each 4 bit number is the difference between one sample and the next, divided by a (varying) step. The Intel/DVI ADPCM algorithm has been selected for use by the IMA, so it may well become a standard.

`State` is a tuple containing the state of the coder. The coder returns a tuple `(`*`adpcmfrag`*`, `*`newstate`*`)`, and the *newstate* should be passed to the next call of lin2adpcm. In the initial call `None` can be passed as the state. *adpcmfrag* is the ADPCM coded fragment packed 2 4-bit values per byte.

### `lin2adpcm3`(fragment  width  state)

This is an alternative ADPCM coder that uses only 3 bits per sample. It is not compatible with the Intel/DVI ADPCM coder and its output is not packed (due to laziness on the side of the author). Its use is discouraged.

### `lin2ulaw`(fragment  width)

This function converts samples in the audio fragment to U-LAW encoding and returns this as a Python string. U-LAW is an audio encoding format whereby you get a dynamic range of about 14 bits using only 8 bit samples. It is used by the Sun audio hardware, among others.

### `minmax`(fragment  width)

This function returns a tuple consisting of the minimum and maximum values of all samples in the sound fragment.

### `max`(fragment  width)

This function returns the maximum of the *absolute value* of all samples in a fragment.

### `maxpp`(fragment  width)

This function returns the maximum peak-peak value in the sound fragment.

### `mul`(fragment  width  factor)

Mul returns a fragment that has all samples in the original framgent multiplied by the floating-point value *factor*. Overflow is silently ignored.

### `reverse`(fragment  width)

This function reverses the samples in a fragment and returns the modified fragment.

### `tomono`(fragment  width  lfactor  rfactor)

This function converts a stereo fragment to a mono fragment. The left channel is multiplied by *lfactor* and the right channel by *rfactor* before adding the two channels to give a mono signal.

### `tostereo`(fragment  width  lfactor  rfactor)

This function generates a stereo fragment from a mono fragment. Each pair of samples in the stereo fragment are computed from the mono sample, whereby left channel samples are multiplied by *lfactor* and right channel samples by *rfactor*.

### `mul`(fragment  width  factor)

Mul returns a fragment that has all samples in the original framgent multiplied by the floating-point value *factor*. Overflow is silently ignored.

### `rms`(fragment  width  factor)

Returns the root-mean-square of the fragment, i.e. the square root of the quotient of the sum of all squared sample value, divided by the sumber of samples.

√(S_i)^2n This is a measure of the power in an audio signal.

### `ulaw2lin`(fragment  width)

This function converts sound fragments in ULAW encoding to linearly encoded sound fragments. ULAW encoding always uses 8 bits samples, so *width* refers only to the sample width of the output fragment here.

Note that operations such as `mul` or `max` make no distinction between mono and stereo fragments, i.e. all samples are treated equal. If this is a problem the stereo fragment should be split into two mono fragments first and recombined later. Here is an example of how to do that:

    def mul_stereo(sample, width, lfactor, rfactor):
        lsample = audioop.tomono(sample, width, 1, 0)
        rsample = audioop.tomono(sample, width, 0, 1)
        lsample = audioop.mul(sample, width, lfactor)
        rsample = audioop.mul(sample, width, rfactor)
        lsample = audioop.tostereo(lsample, width, 1, 0)
        rsample = audioop.tostereo(rsample, width, 0, 1)
        return audioop.add(lsample, rsample, width)

If you use the ADPCM coder to build network packets and you want your protocol to be stateless (i.e. to be able to tolerate packet loss) you should not only transmit the data but also the state. Note that you should send the *initial* state (the one you passed to lin2adpcm) along to the decoder, not the final state (as returned by the coder). If you want to use `struct` to store the state in binary you can code the first element (the predicted value) in 16 bits and the second (the delta index) in 8.

The ADPCM coders have never been tried against other ADPCM coders, only against themselves. It could well be that I misinterpreted the standards in which case they will not be interoperable with the respective standards.

The `find...` routines might look a bit funny at first sight. They are primarily meant for doing echo cancellation. A reasonably fast way to do this is to pick the most energetic piece of the output sample, locate that in the input sample and subtract the whole output sample from the input sample:

    def echocancel(outputdata, inputdata):
        pos = audioop.findmax(outputdata, 800)    # one tenth second
        out_test = outputdata[pos*2:]
        in_test = inputdata[pos*2:]
        ipos, factor = audioop.findfit(in_test, out_test)
        # Optional (for better cancellation):
        # factor = audioop.findfactor(in_test[ipos*2:ipos*2+len(out_test)], 
        #              out_test)
        prefill = '\0'*(pos+ipos)*2
        postfill = '\0'*(len(inputdata)-len(prefill)-len(outputdata))
        outputdata = prefill + audioop.mul(outputdata,2,-factor) + postfill
        return audioop.add(inputdata, outputdata, 2)
# Built-in Module `__builtin__`

This module provides direct access to all ‘built-in’ identifier of Python; e.g. `__builtin__.open` is the full name for the built-in function `open`.
# CRYPTOGRAPHIC EXTENSIONS

The modules described in this chapter implement various algorithms of a cryptographic nature. They are available at the discretion of the installation.
# Built-in Module `dbm`

Dbm provides python programs with an interface to the unix `ndbm` database library. Dbm objects are of the mapping type, so they can be handled just like objects of the built-in *dictionary* type, except that keys and values are always strings, and printing a dbm object doesn’t print the keys and values.

The module defines the following constant and functions:

### exception `error`

Raised on dbm-specific errors, such as I/O errors. `KeyError` is raised for general mapping errors like specifying an incorrect key.

### `open`(filename  rwmode  filemode)

Open a dbm database and return a mapping object. *filename* is the name of the database file (without the `.dir` or `.pag` extensions), *rwmode* is `’r’`, `’w’` or `’rw’` as for `open`, and *filemode* is the unix mode of the file, used only when the database has to be created.
# Built-in Exceptions

Exceptions are string objects. Two distinct string objects with the same value are different exceptions. This is done to force programmers to use exception names rather than their string value when specifying exception handlers. The string value of all built-in exceptions is their name, but this is not a requirement for user-defined exceptions or exceptions defined by library modules.

The following exceptions can be generated by the interpreter or built-in functions. Except where mentioned, they have an ‘associated value’ indicating the detailed cause of the error. This may be a string or a tuple containing several items of information (e.g., an error code and a string explaining the code).

User code can raise built-in exceptions. This can be used to test an exception handler or to report an error condition ‘just like’ the situation in which the interpreter raises the same exception; but beware that there is nothing to prevent user code from raising an inappropriate error.

### exception `AttributeError`

Raised when an attribute reference or assignment fails. (When an object does not support attributes references or attribute assignments at all, `TypeError` is raised.)

### exception `EOFError`

Raised when one of the built-in functions (`input()` or `raw_input()`) hits an end-of-file condition (EOF) without reading any data.

(N.B.: the `read()` and `readline()` methods of file objects return an empty string when they hit EOF.) No associated value.

### exception `IOError`

Raised when an I/O operation (such as a `print` statement, the built-in `open()` function or a method of a file object) fails for an I/O-related reason, e.g., ‘file not found’, ‘disk full’.

### exception `ImportError`

Raised when an `import` statement fails to find the module definition or when a `from ``…`` import` fails to find a name that is to be imported.

### exception `IndexError`

Raised when a sequence subscript is out of range. (Slice indices are silently truncated to fall in the allowed range; if an index is not a plain integer, `TypeError` is raised.)

### exception `KeyError`

Raised when a mapping (dictionary) key is not found in the set of existing keys.

### exception `KeyboardInterrupt`

Raised when the user hits the interrupt key (normally `Control-C` or ). During execution, a check for interrupts is made regularly.

Interrupts typed when a built-in function `input()` or `raw_input()`) is waiting for input also raise this exception. No associated value.

### exception `MemoryError`

Raised when an operation runs out of memory but the situation may still be rescued (by deleting some objects). The associated value is a string indicating what kind of (internal) operation ran out of memory. Note that because of the underlying memory management architecture (C’s `malloc()` function), the interpreter may not always be able to completely recover from this situation; it nevertheless raises an exception so that a stack traceback can be printed, in case a run-away program was the cause.

### exception `NameError`

Raised when a local or global name is not found. This applies only to unqualified names. The associated value is the name that could not be found.

### exception `OverflowError`

Raised when the result of an arithmetic operation is too large to be represented. This cannot occur for long integers (which would rather raise `MemoryError` than give up). Because of the lack of standardization of floating point exception handling in C, most floating point operations also aren’t checked. For plain integers, all operations that can overflow are checked except left shift, where typical applications prefer to drop bits than raise an exception.

### exception `RuntimeError`

Raised when an error is detected that doesn’t fall in any of the other categories. The associated value is a string indicating what precisely went wrong. (This exception is a relic from a previous version of the interpreter; it is not used any more except by some extension modules that haven’t been converted to define their own exceptions yet.)

### exception `SyntaxError`

Raised when the parser encounters a syntax error. This may occur in an `import` statement, in an `exec` statement, in a call to the built-in function `eval()` or `input()`, or when reading the initial script or standard input (also interactively).

### exception `SystemError`

Raised when the interpreter finds an internal error, but the situation does not look so serious to cause it to abandon all hope. The associated value is a string indicating what went wrong (in low-level terms).

You should report this to the author or maintainer of your Python interpreter. Be sure to report the version string of the Python interpreter (`sys.version`; it is also printed at the start of an interactive Python session), the exact error message (the exception’s associated value) and if possible the source of the program that triggered the error.

### exception `SystemExit`

This exception is raised by the `sys.exit()` function. When it is not handled, the Python interpreter exits; no stack traceback is printed. If the associated value is a plain integer, it specifies the system exit status (passed to C’s `exit()` function); if it is `None`, the exit status is zero; if it has another type (such as a string), the object’s value is printed and the exit status is one.

A call to `sys.exit` is translated into an exception so that clean-up handlers (`finally` clauses of `try` statements) can be executed, and so that a debugger can execute a script without running the risk of losing control. The `posix._exit()` function can be used if it is absolutely positively necessary to exit immediately (e.g., after a `fork()` in the child process).

### exception `TypeError`

Raised when a built-in operation or function is applied to an object of inappropriate type. The associated value is a string giving details about the type mismatch.

### exception `ValueError`

Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value, and the situation is not described by a more precise exception such as `IndexError`.

### exception `ZeroDivisionError`

Raised when the second argument of a division or modulo operation is zero. The associated value is a string indicating the type of the operands and the operation.
# Built-in module `fcntl`

This module performs file control and IO control on file descriptors. It is an interface to the *fcntl()* and *ioctl()* Unixroutines. File descriptors can be obtained with the *fileno()* method of a file or socket object.

The module defines the following functions:

### `fcntl`(fd  op)

Perform the requested operation on file descriptor *`fd`*. The operation is defined by *`op`* and is operating system dependent. Typically these codes can be retrieved from the library module `FCNTL`. The argument *`arg`* is optional, and defaults to the integer value `0`. When it is present, it can either be an integer value, or a string. With the argument missing or an integer value, the return value of this function is the integer return value of the real `fcntl()` call. When the argument is a string it represents a binary structure, e.g. created by `struct.pack()`. The binary data is copied to a buffer whose address is passed to the real `fcntl()` call. The return value after a successful call is the contents of the buffer, converted to a string object. In the case the `fcntl()` fails, an `IOError` will be raised.

### `ioctl`(fd  op  arg)

This function is identical to the `fcntl()` function, except that the operations are typically defined in the library module `IOCTL`.

If the library modules `FCNTL` or `IOCTL` are missing, you can find the opcodes in the C include files `sys/fcntl` and `sys/ioctl`. You can create the modules yourself with the h2py script, found in the `Demo/scripts` directory.

Examples (all on a SVR4 compliant system):

    import struct, FCNTL

    file = open(...)
    rv = fcntl(file.fileno(), FCNTL.O_NDELAY, 1)

    lockdata = struct.pack('hhllhh', FCNTL.F_WRLCK, 0, 0, 0, 0, 0)
    rv = fcntl(file.fileno(), FCNTL.F_SETLKW, lockdata)

Note that in the first example the return value variable `rv` will hold an integer value; in the second example it will hold a string value.
# Built-in Module `fl`

This module provides an interface to the FORMS Library by Mark Overmars, version 2.0b. For more info about FORMS, write to `markov@cs.ruu.nl`.

Most functions are literal translations of their C equivalents, dropping the initial `fl_` from their name. Constants used by the library are defined in module `FL` described below.

The creation of objects is a little different in Python than in C: instead of the ‘current form’ maintained by the library to which new FORMS objects are added, all functions that add a FORMS object to a button are methods of the Python object representing the form. Consequently, there are no Python equivalents for the C functions `fl_addto_form` and `fl_end_form`, and the equivalent of `fl_bgn_form` is called `fl.make_form`.

Watch out for the somewhat confusing terminology: FORMS uses the word *object* for the buttons, sliders etc. that you can place in a form. In Python, ‘object’ means any value. The Python interface to FORMS introduces two new Python object types: form objects (representing an entire form) and FORMS objects (representing one button, slider etc.). Hopefully this isn’t too confusing...

There are no ‘free objects’ in the Python interface to FORMS, nor is there an easy way to add object classes written in Python. The FORMS interface to GL event handling is avaiable, though, so you can mix FORMS with pure GL windows.

**Please note:** importing `fl` implies a call to the GL function `foreground()` and to the FORMS routine `fl_init()`.

## Functions defined in module `fl`

Module `fl` defines the following functions. For more information about what they do, see the description of the equivalent C function in the FORMS documentation:

### `make_form`(type  width  height)

Create a form with given type, width and height. This returns a *form* object, whose methods are described below.

### `do_forms`()

The standard FORMS main loop. Returns a Python object representing the FORMS object needing interaction, or the special value `FL.EVENT`.

### `check_forms`()

Check for FORMS events. Returns what `do_forms` above returns, or `None` if there is no event that immediately needs interaction.

### `set_event_call_back`(function)

Set the event callback function.

### `set_graphics_mode`(rgbmode  doublebuffering)

Set the graphics modes.

### `get_rgbmode`()

Return the current rgb mode. This is the value of the C global variable `fl_rgbmode`.

### `show_message`(str1  str2  str3)

Show a dialog box with a three-line message and an OK button.

### `show_question`(str1  str2  str3)

Show a dialog box with a three-line message and YES and NO buttons. It returns `1` if the user pressed YES, `0` if NO.

### `show_choice`(str1  str2  str3  but1)

Show a dialog box with a three-line message and up to three buttons. It returns the number of the button clicked by the user (`1`, `2` or `3`).

### `show_input`(prompt  default)

Show a dialog box with a one-line prompt message and text field in which the user can enter a string. The second argument is the default input string. It returns the string value as edited by the user.

### `show_file_selector`(message  directory  pattern  default)

Show a dialog box inm which the user can select a file. It returns the absolute filename selected by the user, or `None` if the user presses Cancel.

### `get_directory`()

These functions return the directory, pattern and filename (the tail part only) selected by the user in the last `show_file_selector` call.

### `qdevice`(dev)

These functions are the FORMS interfaces to the corresponding GL functions. Use these if you want to handle some GL events yourself when using `fl.do_events`. When a GL event is detected that FORMS cannot handle, `fl.do_forms()` returns the special value `FL.EVENT` and you should call `fl.qread()` to read the event from the queue. Don’t use the equivalent GL functions!

### `color`()

See the description in the FORMS documentation of `fl_color`, `fl_mapcolor` and `fl_getmcolor`.

## Form object methods and data attributes

Form objects (returned by `fl.make_form()` above) have the following methods. Each method corresponds to a C function whose name is prefixed with `fl_`; and whose first argument is a form pointer; please refer to the official FORMS documentation for descriptions.

All the `add_``…` functions return a Python object representing the FORMS object. Methods of FORMS objects are described below. Most kinds of FORMS object also have some methods specific to that kind; these methods are listed here.



### `show_form`(placement  bordertype  name)

Show the form.

### `hide_form`()

Hide the form.

### `redraw_form`()

Redraw the form.

### `set_form_position`(x  y)

Set the form’s position.

### `freeze_form`()

Freeze the form.

### `unfreeze_form`()

Unfreeze the form.

### `activate_form`()

Activate the form.

### `deactivate_form`()

Deactivate the form.

### `bgn_group`()

Begin a new group of objects; return a group object.

### `end_group`()

End the current group of objects.

### `find_first`()

Find the first object in the form.

### `find_last`()

Find the last object in the form.

### `add_box`(type  x  y  w  h  name)

Add a box object to the form. No extra methods.

### `add_text`(type  x  y  w  h  name)

Add a text object to the form. No extra methods.

### `add_clock`(type  x  y  w  h  name)

Add a clock object to the form.\
Method: `get_clock`.

### `add_button`(type  x  y  w  h  name)

Add a button object to the form.\
Methods: `get_button`, `set_button`.

### `add_lightbutton`(type  x  y  w  h  name)

Add a lightbutton object to the form.\
Methods: `get_button`, `set_button`.

### `add_roundbutton`(type  x  y  w  h  name)

Add a roundbutton object to the form.\
Methods: `get_button`, `set_button`.

### `add_slider`(type  x  y  w  h  name)

Add a slider object to the form.\
Methods: `set_slider_value`, `get_slider_value`, `set_slider_bounds`, `get_slider_bounds`, `set_slider_return`, `set_slider_size`, `set_slider_precision`, `set_slider_step`.

### `add_valslider`(type  x  y  w  h  name)

Add a valslider object to the form.\
Methods: `set_slider_value`, `get_slider_value`, `set_slider_bounds`, `get_slider_bounds`, `set_slider_return`, `set_slider_size`, `set_slider_precision`, `set_slider_step`.

### `add_dial`(type  x  y  w  h  name)

Add a dial object to the form.\
Methods: `set_dial_value`, `get_dial_value`, `set_dial_bounds`, `get_dial_bounds`.

### `add_positioner`(type  x  y  w  h  name)

Add a positioner object to the form.\
Methods: `set_positioner_xvalue`, `set_positioner_yvalue`, `set_positioner_xbounds`, `set_positioner_ybounds`, `get_positioner_xvalue`, `get_positioner_yvalue`, `get_positioner_xbounds`, `get_positioner_ybounds`.

### `add_counter`(type  x  y  w  h  name)

Add a counter object to the form.\
Methods: `set_counter_value`, `get_counter_value`, `set_counter_bounds`, `set_counter_step`, `set_counter_precision`, `set_counter_return`.

### `add_input`(type  x  y  w  h  name)

Add a input object to the form.\
Methods: `set_input`, `get_input`, `set_input_color`, `set_input_return`.

### `add_menu`(type  x  y  w  h  name)

Add a menu object to the form.\
Methods: `set_menu`, `get_menu`, `addto_menu`.

### `add_choice`(type  x  y  w  h  name)

Add a choice object to the form.\
Methods: `set_choice`, `get_choice`, `clear_choice`, `addto_choice`, `replace_choice`, `delete_choice`, `get_choice_text`, `set_choice_fontsize`, `set_choice_fontstyle`.

### `add_browser`(type  x  y  w  h  name)

Add a browser object to the form.\
Methods: `set_browser_topline`, `clear_browser`, `add_browser_line`, `addto_browser`, `insert_browser_line`, `delete_browser_line`, `replace_browser_line`, `get_browser_line`, `load_browser`, `get_browser_maxline`, `select_browser_line`, `deselect_browser_line`, `deselect_browser`, `isselected_browser_line`, `get_browser`, `set_browser_fontsize`, `set_browser_fontstyle`, `set_browser_specialkey`.

### `add_timer`(type  x  y  w  h  name)

Add a timer object to the form.\
Methods: `set_timer`, `get_timer`.



Form objects have the following data attributes; see the FORMS documentation:

|             |                 |                                |
|:------------|:----------------|:-------------------------------|
| window      | int (read-only) | GL window id                   |
| w           | float           | form width                     |
| h           | float           | form height                    |
| x           | float           | form x origin                  |
| y           | float           | form y origin                  |
| deactivated | int             | nonzero if form is deactivated |
| visible     | int             | nonzero if form is visible     |
| frozen      | int             | nonzero if form is frozen      |
| doublebuf   | int             | nonzero if double buffering on |

## FORMS object methods and data attributes

Besides methods specific to particular kinds of FORMS objects, all FORMS objects also have the following methods:

### `set_call_back`(function  argument)

Set the object’s callback function and argument. When the object needs interaction, the callback function will be called with two arguments: the object, and the callback argument. (FORMS objects without a callback function are returned by `fl.do_forms()` or `fl.check_forms()` when they need interaction.) Call this method without arguments to remove the callback function.

### `delete_object`()

Delete the object.

### `show_object`()

Show the object.

### `hide_object`()

Hide the object.

### `redraw_object`()

Redraw the object.

### `freeze_object`()

Freeze the object.

### `unfreeze_object`()

Unfreeze the object.

FORMS objects have these data attributes; see the FORMS documentation:

|            |                 |                  |
|:-----------|:----------------|:-----------------|
| objclass   | int (read-only) | object class     |
| type       | int (read-only) | object type      |
| boxtype    | int             | box type         |
| x          | float           | x origin         |
| y          | float           | y origin         |
| w          | float           | width            |
| h          | float           | height           |
| col1       | int             | primary color    |
| col2       | int             | secondary color  |
| align      | int             | alignment        |
| lcol       | int             | label color      |
| lsize      | float           | label font size  |
| label      | string          | label string     |
| lstyle     | int             | label style      |
| pushed     | int (read-only) | (see FORMS docs) |
| focus      | int (read-only) | (see FORMS docs) |
| belowmouse | int (read-only) | (see FORMS docs) |
| frozen     | int (read-only) | (see FORMS docs) |
| active     | int (read-only) | (see FORMS docs) |
| input      | int (read-only) | (see FORMS docs) |
| visible    | int (read-only) | (see FORMS docs) |
| radio      | int (read-only) | (see FORMS docs) |
| automatic  | int (read-only) | (see FORMS docs) |

# Standard Module `FL`

This module defines symbolic constants needed to use the built-in module `fl` (see above); they are equivalent to those defined in the C header file `<forms.h>` except that the name prefix `FL_` is omitted. Read the module source for a complete list of the defined names. Suggested use:

    import fl
    from FL import *

# Standard Module `flp`

This module defines functions that can read form definitions created by the ‘form designer’ (`fdesign`) program that comes with the FORMS library (see module `fl` above).

For now, see the file `flp.doc` in the Python library source directory for a description.

XXX A complete description should be inserted here!
# Built-in Module `fm`

This module provides access to the IRIS *Font Manager* library. It is available only on Silicon Graphics machines. See also: 4Sight User’s Guide, Section 1, Chapter 5: Using the IRIS Font Manager.

This is not yet a full interface to the IRIS Font Manager. Among the unsupported features are: matrix operations; cache operations; character operations (use string operations instead); some details of font info; individual glyph metrics; and printer matching.

It supports the following operations:

### `init`()

Initialization function. Calls `fminit()`. It is normally not necessary to call this function, since it is called automatically the first time the `fm` module is imported.

### `findfont`(fontname)

Return a font handle object. Calls `fmfindfont(`*`fontname`*`)`.

### `enumerate`()

Returns a list of available font names. This is an interface to `fmenumerate()`.

### `prstr`(string)

Render a string using the current font (see the `setfont()` font handle method below). Calls `fmprstr(`*`string`*`)`.

### `setpath`(string)

Sets the font search path. Calls `fmsetpath(string)`. (XXX Does not work!?!)

### `fontpath`()

Returns the current font search path.

Font handle objects support the following operations:

### `scalefont`(factor)

Returns a handle for a scaled version of this font. Calls `fmscalefont(`*`fh`*`, `*`factor`*`)`.

### `setfont`()

Makes this font the current font. Note: the effect is undone silently when the font handle object is deleted. Calls `fmsetfont(`*`fh`*`)`.

### `getfontname`()

Returns this font’s name. Calls `fmgetfontname(`*`fh`*`)`.

### `getcomment`()

Returns the comment string associated with this font. Raises an exception if there is none. Calls `fmgetcomment(`*`fh`*`)`.

### `getfontinfo`()

Returns a tuple giving some pertinent data about this font. This is an interface to `fmgetfontinfo()`. The returned tuple contains the following numbers: `(`*`printermatched`*`, `*`fixed_width`*`, `*`xorig`*`, `*`yorig`*`, `*`xsize`*`, `*`ysize`*`, `*`height`*`, `*`nglyphs`*`)`.

### `getstrwidth`(string)

Returns the width, in pixels, of the string when drawn in this font. Calls `fmgetstrwidth(`*`fh`*`, `*`string`*`)`.
# Built-in Functions

The Python interpreter has a number of functions built into it that are always available. They are listed here in alphabetical order.

### `abs`(x)

Return the absolute value of a number. The argument may be a plain or long integer or a floating point number.

### `apply`(function  args)

The *function* argument must be a callable object (a user-defined or built-in function or method, or a class object) and the *args* argument must be a tuple. The *function* is called with *args* as argument list; the number of arguments is the the length of the tuple. (This is different from just calling *`func`*`(`*`args`*`)`, since in that case there is always exactly one argument.)

### `chr`(i)

Return a string of one character whose ASCII code is the integer *i*, e.g., `chr(97)` returns the string `’a’`. This is the inverse of `ord()`. The argument must be in the range [0..255], inclusive.

### `cmp`(x  y)

Compare the two objects *x* and *y* and return an integer according to the outcome. The return value is negative if *`x`*` < `*`y`*, zero if *`x`*` == `*`y`* and strictly positive if *`x`*` > `*`y`*.

### `coerce`(x  y)

Return a tuple consisting of the two numeric arguments converted to a common type, using the same rules as used by arithmetic operations.

### `compile`(string  filename  kind)

Compile the *string* into a code object. Code objects can be executed by a `exec()` statement or evaluated by a call to `eval()`. The *filename* argument should give the file from which the code was read; pass e.g. `’<string>’` if it wasn’t read from a file. The *kind* argument specifies what kind of code must be compiled; it can be `’exec’` if *string* consists of a sequence of statements, or `’eval’` if it consists of a single expression.

### `delattr`(object  name)

This is a relative of `setattr`. The arguments are an object and a string. The string must be the name of one of the object’s attributes. The function deletes the named attribute, provided the object allows it. For example, `setattr(`*`x`*`, ’`*`foobar`*`’)` is equivalent to `del `*`x`*`.`*`foobar`*.

### `dir`()

Without arguments, return the list of names in the current local symbol table. With a module, class or class instance object as argument (or anything else that has a `__dict__` attribute), returns the list of names in that object’s attribute dictionary. The resulting list is sorted. For example:

    >>> import sys
    >>> dir()
    ['sys']
    >>> dir(sys)
    ['argv', 'exit', 'modules', 'path', 'stderr', 'stdin', 'stdout']
    >>> 

### `divmod`(a  b)

Take two numbers as arguments and return a pair of integers consisting of their integer quotient and remainder. With mixed operand types, the rules for binary arithmetic operators apply. For plain and long integers, the result is the same as `(`*`a`*` / `*`b`*`, `*`a`*` % `*`b`*`)`. For floating point numbers the result is the same as `(math.floor(`*`a`*` / `*`b`*`), `*`a`*` % `*`b`*`)`.

### `eval`(s)

The arguments are a string and two optional dictionaries. The string argument is parsed and evaluated as a Python expression (technically speaking, a condition list) using the dictionaries as global and local name space. The string must not contain null bytes or newline characters. The return value is the result of the expression. If the third argument is omitted it defaults to the second. If both dictionaries are omitted, the expression is executed in the environment where `eval` is called. Syntax errors are reported as exceptions. Example:

    >>> x = 1
    >>> print eval('x+1')
    2
    >>> 

This function can also be used to execute arbitrary code objects (e.g. created by `compile()`). In this case pass a code object instead of a string. The code object must have been compiled passing `’eval’` to the *kind* argument.

Note: dynamic execution of statements is supported by the `exec` statement.

### `filter`(function  list)

Construct a list from those elements of *list* for which *function* returns true. If *list* is a string or a tuple, the result also has that type; otherwise it is always a list. If *function* is `None`, the identity function is assumed, i.e. all elements of *list* that are false (zero or empty) are removed.

### `float`(x)

Convert a number to floating point. The argument may be a plain or long integer or a floating point number.

### `getattr`(object  name)

The arguments are an object and a string. The string must be the name of one of the object’s attributes. The result is the value of that attribute. For example, `getattr(`*`x`*`, ’`*`foobar`*`’)` is equivalent to *`x`*`.`*`foobar`*.

### `hasattr`(object  name)

The arguments are an object and a string. The result is 1 if the string is the name of one of the object’s attributes, 0 if not. (This is implemented by calling `getattr(object, name)` and seeing whether it raises an exception or not.)

### `hash`(object)

Return the hash value of the object (if it has one). Hash values are 32-bit integers. They are used to quickly compare dictionary keys during a dictionary lookup. Numeric values that compare equal have the same hash value (even if they are of different types, e.g. 1 and 1.0).

### `hex`(x)

Convert a number to a hexadecimal string. The result is a valid Python expression.

### `id`(object)

Return the ‘identity’ of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. (Two objects whose lifetimes are disjunct may have the same id() value.) (Implementation note: this is the address of the object.)

### `input`()

Almost equivalent to `eval(raw_input(`*`prompt`*`))`. Like `raw_input()`, the *prompt* argument is optional. The difference is that a long input expression may be broken over multiple lines using the backslash convention.

### `int`(x)

Convert a number to a plain integer. The argument may be a plain or long integer or a floating point number.

### `len`(s)

Return the length (the number of items) of an object. The argument may be a sequence (string, tuple or list) or a mapping (dictionary).

### `long`(x)

Convert a number to a long integer. The argument may be a plain or long integer or a floating point number.

### `map`(function  list  ...)

Apply *function* to every item of *list* and return a list of the results. If additional *list* arguments are passed, *function* must take that many arguments and is applied to the items of all lists in parallel; if a list is shorter than another it is assumed to be extended with `None` items. If *function* is `None`, the identity function is assumed; if there are multiple list arguments, `map` returns a list consisting of tuples containing the corresponding items from all lists (i.e. a kind of transpose operation). The *list* arguments may be any kind of sequence; the result is always a list.

### `max`(s)

Return the largest item of a non-empty sequence (string, tuple or list).

### `min`(s)

Return the smallest item of a non-empty sequence (string, tuple or list).

### `oct`(x)

Convert a number to an octal string. The result is a valid Python expression.

### `open`(filename  )

Return a new file object (described earlier under Built-in Types). The first two arguments are the same as for `stdio`’s `fopen()`: *filename* is the file name to be opened, *mode* indicates how the file is to be opened: `’r’` for reading, `’w’` for writing (truncating an existing file), and `’a’` opens it for appending. Modes `’r+’`, `’w+’` and `’a+’` open the file for updating, provided the underlying `stdio` library understands this. On systems that differentiate between binary and text files, `’b’` appended to the mode opens the file in binary mode. If the file cannot be opened, `IOError` is raised. If *mode* is omitted, it defaults to `’r’`. The optional *bufsize* argument specifies the file’s desired buffer size: 0 means unbuffered, 1 means line buffered, any other positive value means use a buffer of (approximately) that size. A negative *bufsize* means to use the system default, which is usually line buffered for for tty devices and fully buffered for other files. [^1]

### `ord`(c)

Return the ASCII value of a string of one character. E.g., `ord(’a’)` returns the integer `97`. This is the inverse of `chr()`.

### `pow`(x  y)

Return *x* to the power *y*; if *z* is present, return *x* to the power *y*, modulo *z* (computed more efficiently that `pow(`*`x`*`, `*`y`*`) % `*`z`*). The arguments must have numeric types. With mixed operand types, the rules for binary arithmetic operators apply. The effective operand type is also the type of the result; if the result is not expressible in this type, the function raises an exception; e.g., `pow(2, -1)` or `pow(2, 35000)` is not allowed.

### `range`( end)

This is a versatile function to create lists containing arithmetic progressions. It is most often used in `for` loops. The arguments must be plain integers. If the *step* argument is omitted, it defaults to `1`. If the *start* argument is omitted, it defaults to `0`. The full form returns a list of plain integers `[`*`start`*`, `*`start`*` + `*`step`*`, `*`start`*` + 2 * `*`step`*`, …]`. If *step* is positive, the last element is the largest *`start`*` + `*`i`*` * `*`step`* less than *end*; if *step* is negative, the last element is the largest *`start`*` + `*`i`*` * `*`step`* greater than *end*. *step* must not be zero. Example:

    >>> range(10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> range(1, 11)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> range(0, 30, 5)
    [0, 5, 10, 15, 20, 25]
    >>> range(0, 10, 3)
    [0, 3, 6, 9]
    >>> range(0, -10, -1)
    [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
    >>> range(0)
    []
    >>> range(1, 0)
    []
    >>> 

### `raw_input`()

If the *prompt* argument is present, it is written to standard output without a trailing newline. The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that. When EOF is read, `EOFError` is raised. Example:

    >>> s = raw_input('--> ')
    --> Monty Python's Flying Circus
    >>> s
    'Monty Python\'s Flying Circus'
    >>> 

### `reduce`(function  list)

Apply the binary *function* to the items of *list* so as to reduce the list to a single value. E.g., `reduce(lambda x, y: x*y, `*`list`*`, 1)` returns the product of the elements of *list*. The optional *initializer* can be thought of as being prepended to *list* so as to allow reduction of an empty *list*. The *list* arguments may be any kind of sequence.

### `reload`(module)

Re-parse and re-initialize an already imported *module*. The argument must be a module object, so it must have been successfully imported before. This is useful if you have edited the module source file using an external editor and want to try out the new version without leaving the Python interpreter. Note that if a module is syntactically correct but its initialization fails, the first `import` statement for it does not import the name, but does create a (partially initialized) module object; to reload the module you must first `import` it again (this will just make the partially initialized module object available) before you can `reload()` it.

### `repr`(object)

Return a string containing a printable representation of an object. This is the same value yielded by conversions (reverse quotes). It is sometimes useful to be able to access this operation as an ordinary function. For many types, this function makes an attempt to return a string that would yield an object with the same value when passed to `eval()`.

### `round`(x  n)

Return the floating point value *x* rounded to *n* digits after the decimal point. If *n* is omitted, it defaults to zero. The result is a floating point number. Values are rounded to the closest multiple of 10 to the power minus *n*; if two multiples are equally close, rounding is done away from 0 (so e.g. `round(0.5)` is `1.0` and `round(-0.5)` is `-1.0`).

### `setattr`(object  name  value)

This is the counterpart of `getattr`. The arguments are an object, a string and an arbitrary value. The string must be the name of one of the object’s attributes. The function assigns the value to the attribute, provided the object allows it. For example, `setattr(`*`x`*`, ’`*`foobar`*`’, 123)` is equivalent to *`x`*`.`*`foobar`*` = 123`.

### `str`(object)

Return a string containing a nicely printable representation of an object. For strings, this returns the string itself. The difference with `repr(`*`object`* is that `str(`*`object`* does not always attempt to return a string that is acceptable to `eval()`; its goal is to return a printable string.

### `tuple`(object)

Return a tuple whose items are the same and in the same order as *object*’s items. If *object* is alread a tuple, it is returned unchanged. For instance, `tuple(’abc’)` returns returns `(’a’, ’b’, ’c’)` and `tuple([1, 2, 3])` returns `(1, 2, 3)`.

### `type`(object)

Return the type of an *object*. The return value is a type object. There is not much you can do with type objects except compare them to other type objects; e.g., the following checks if a variable is a string:

    >>> if type(x) == type(''): print 'It is a string'

### `vars`()

Without arguments, return a dictionary corresponding to the current local symbol table. With a module, class or class instance object as argument (or anything else that has a `__dict__` attribute), returns a dictionary corresponding to the object’s symbol table. The returned dictionary should not be modified: the effects on the corresponding symbol table are undefined. [^2]

### `xrange`( end)

This function is very similar to `range()`, but returns an “xrange object” instead of a list. This is an opaque sequence type which yields the same values as the corresponding list, without actually storing them all simultaneously. The advantage of `xrange()` over `range()` is minimal (since `xrange()` still has to create the values when asked for them) except when a very large range is used on a memory-starved machine (e.g. DOS) or when all of the range’s elements are never used (e.g. when the loop is usually terminated with `break`).

[^1]: Specifying a buffer size currently has no effect on systems that don’t have `setvbuf()`. The interface to specify the buffer size is not done using a method that calls `setvbuf()`, because that may dump core when called after any I/O has been performed, and there’s no reliable way to determine whether this is the case.

[^2]: In the current implementation, local variable bindings cannot normally be affected this way, but variables retrieved from other scopes can be. This may change.
# Built-in Module `gdbm`

Gdbm provides python programs with an interface to the GNU `gdbm` database library. Gdbm objects are of the mapping type, so they can be handled just like objects of the built-in *dictionary* type, except that keys and values are always strings, and printing a gdbm object doesn’t print the keys and values.

The module is based on the Dbm module, modified to use GDBM instead.

The module defines the following constant and functions:

### exception `error`

Raised on gdbm-specific errors, such as I/O errors. `KeyError` is raised for general mapping errors like specifying an incorrect key.

### `open`(filename  rwmode  filemode)

Open a gdbm database and return a mapping object. *filename* is the name of the database file, *rwmode* is `’r’`, `’w’`, `’c’`, or `’n’` for reader, writer (this also gives read access), create (writer, but create the database if it doesnt already exist) and newdb (which will always create a new database). Only one writer may open a gdbm file and many readers may open the file. Readers and writers can not open the gdbm file at the same time. Note that the `GDBM_FAST` mode of opening the database is not supported. *filemode* is the unix mode of the file, used only when a database is created.
# Standard Module `getopt`

This module helps scripts to parse the command line arguments in `sys.argv`. It uses the same conventions as the Unix `getopt()` function. It defines the function `getopt.getopt(args, options)` and the exception `getopt.error`.

The first argument to `getopt()` is the argument list passed to the script with its first element chopped off (i.e., `sys.argv[1:]`). The second argument is the string of option letters that the script wants to recognize, with options that require an argument followed by a colon (i.e., the same format that Unix `getopt()` uses). The return value consists of two elements: the first is a list of option-and-value pairs; the second is the list of program arguments left after the option list was stripped (this is a trailing slice of the first argument). Each option-and-value pair returned has the option as its first element, prefixed with a hyphen (e.g., `’-x’`), and the option argument as its second element, or an empty string if the option has no argument. The options occur in the list in the same order in which they were found, thus allowing multiple occurrences. Example:

    >>> import getopt, string
    >>> args = string.split('-a -b -cfoo -d bar a1 a2')
    >>> args
    ['-a', '-b', '-cfoo', '-d', 'bar', 'a1', 'a2']
    >>> optlist, args = getopt.getopt(args, 'abc:d:')
    >>> optlist
    [('-a', ''), ('-b', ''), ('-c', 'foo'), ('-d', 'bar')]
    >>> args
    ['a1', 'a2']
    >>> 

The exception `getopt.error = ’getopt error’` is raised when an unrecognized option is found in the argument list or when an option requiring an argument is given none. The argument to the exception is a string indicating the cause of the error.
# Built-in Module `gl`

This module provides access to the Silicon Graphics *Graphics Library*. It is available only on Silicon Graphics machines.

**Warning:** Some illegal calls to the GL library cause the Python interpreter to dump core. In particular, the use of most GL calls is unsafe before the first window is opened.

The module is too large to document here in its entirety, but the following should help you to get started. The parameter conventions for the C functions are translated to Python as follows:

- All (short, long, unsigned) int values are represented by Python integers.

- All float and double values are represented by Python floating point numbers. In most cases, Python integers are also allowed.

- All arrays are represented by one-dimensional Python lists. In most cases, tuples are also allowed.

- All string and character arguments are represented by Python strings, for instance, `winopen(’Hi There!’)` and `rotate(900, ’z’)`.

- All (short, long, unsigned) integer arguments or return values that are only used to specify the length of an array argument are omitted. For example, the C call

      lmdef(deftype, index, np, props)

  is translated to Python as

      lmdef(deftype, index, props)

- Output arguments are omitted from the argument list; they are transmitted as function return values instead. If more than one value must be returned, the return value is a tuple. If the C function has both a regular return value (that is not omitted because of the previous rule) and an output argument, the return value comes first in the tuple. Examples: the C call

      getmcolor(i, &red, &green, &blue)

  is translated to Python as

      red, green, blue = getmcolor(i)

The following functions are non-standard or have special argument conventions:

### `varray`(argument)

Equivalent to but faster than a number of `v3d()` calls. The *argument* is a list (or tuple) of points. Each point must be a tuple of coordinates `(`*`x`*`, `*`y`*`, `*`z`*`)` or `(`*`x`*`, `*`y`*`)`. The points may be 2- or 3-dimensional but must all have the same dimension. Float and int values may be mixed however. The points are always converted to 3D double precision points by assuming *`z`*` = 0.0` if necessary (as indicated in the man page), and for each point `v3d()` is called.

### `nvarray`()

Equivalent to but faster than a number of `n3f` and `v3f` calls. The argument is an array (list or tuple) of pairs of normals and points. Each pair is a tuple of a point and a normal for that point. Each point or normal must be a tuple of coordinates `(`*`x`*`, `*`y`*`, `*`z`*`)`. Three coordinates must be given. Float and int values may be mixed. For each pair, `n3f()` is called for the normal, and then `v3f()` is called for the point.

### `vnarray`()

Similar to `nvarray()` but the pairs have the point first and the normal second.

### `nurbssurface`(s_k  t_k  ctl  s_ord  t_ord  type)

Defines a nurbs surface. The dimensions of *`ctl`*`[][]` are computed as follows: `[len(`*`s_k`*`) - `*`s_ord`*`]`, `[len(`*`t_k`*`) - `*`t_ord`*`]`.

### `nurbscurve`(knots  ctlpoints  order  type)

Defines a nurbs curve. The length of ctlpoints is `len(`*`knots`*`) - `*`order`*.

### `pwlcurve`(points  type)

Defines a piecewise-linear curve. *points* is a list of points. *type* must be `N_ST`.

### `pick`(n)

The only argument to these functions specifies the desired size of the pick or select buffer.

### `endpick`()

These functions have no arguments. They return a list of integers representing the used part of the pick/select buffer. No method is provided to detect buffer overrun.

Here is a tiny but complete example GL program in Python:

    import gl, GL, time

    def main():
        gl.foreground()
        gl.prefposition(500, 900, 500, 900)
        w = gl.winopen('CrissCross')
        gl.ortho2(0.0, 400.0, 0.0, 400.0)
        gl.color(GL.WHITE)
        gl.clear()
        gl.color(GL.RED)
        gl.bgnline()
        gl.v2f(0.0, 0.0)
        gl.v2f(400.0, 400.0)
        gl.endline()
        gl.bgnline()
        gl.v2f(400.0, 0.0)
        gl.v2f(0.0, 400.0)
        gl.endline()
        time.sleep(5)

    main()

# Standard Modules `GL` and `DEVICE`

These modules define the constants used by the Silicon Graphics *Graphics Library* that C programmers find in the header files `<gl/gl.h>` and `<gl/device.h>`. Read the module source files for details.
# Built-in Module `grp`

This module provides access to the Unix group database. It is available on all Unix versions.

Group database entries are reported as 4-tuples containing the following items from the group database (see `<grp.h>`), in order: `gr_name`, `gr_passwd`, `gr_gid`, `gr_mem`. The gid is an integer, name and password are strings, and the member list is a list of strings. (Note that most users are not explicitly listed as members of the group(s) they are in.) An exception is raised if the entry asked for cannot be found.

It defines the following items:

### `getgrgid`(gid)

Return the group database entry for the given numeric group ID.

### `getgrnam`(name)

Return the group database entry for the given group name.

### `getgrall`()

Return a list of all available group entries entries, in arbitrary order.
# Built-in module `imageop`

The imageop module contains some useful operations on images. It operates on images consisting of 8 or 32 bit pixels stored in python strings. This is the same format as used by `gl.lrectwrite` and the `imgfile` module.

The module defines the following variables and functions:

### exception `error`

This exception is raised on all errors, such as unknown number of bits per pixel, etc.

### `crop`(image  psize  width  height  x0  y0  x1  y1)

This function takes the image in `image`, which should by `width` by `height` in size and consist of pixels of `psize` bytes, and returns the selected part of that image. `x0`, `y0`, `x1` and `y1` are like the `lrectread` parameters, i.e. the boundary is included in the new image. The new boundaries need not be inside the picture. Pixels that fall outside the old image will have their value set to zero. If `x0` is bigger than `x1` the new image is mirrored. The same holds for the y coordinates.

### `scale`(image  psize  width  height  newwidth  newheight)

This function returns a `image` scaled to size `newwidth` by `newheight`. No interpolation is done, scaling is done by simple-minded pixel duplication or removal. Therefore, computer-generated images or dithered images will not look nice after scaling.

### `tovideo`(image  psize  width  height)

This function runs a vertical low-pass filter over an image. It does so by computing each destination pixel as the average of two vertically-aligned source pixels. The main use of this routine is to forestall excessive flicker if the image is displayed on a video device that uses interlacing, hence the name.

### `grey2mono`(image  width  height  threshold)

This function converts a 8-bit deep greyscale image to a 1-bit deep image by tresholding all the pixels. The resulting image is tightly packed and is probably only useful as an argument to `mono2grey`.

### `dither2mono`(image  width  height)

This function also converts an 8-bit greyscale image to a 1-bit monochrome image but it uses a (simple-minded) dithering algorithm.

### `mono2grey`(image  width  height  p0  p1)

This function converts a 1-bit monochrome image to an 8 bit greyscale or color image. All pixels that are zero-valued on input get value `p0` on output and all one-value input pixels get value `p1` on output. To convert a monochrome black-and-white image to greyscale pass the values `0` and `255` respectively.

### `grey2grey4`(image  width  height)

Convert an 8-bit greyscale image to a 4-bit greyscale image without dithering.

### `grey2grey2`(image  width  height)

Convert an 8-bit greyscale image to a 2-bit greyscale image without dithering.

### `dither2grey2`(image  width  height)

Convert an 8-bit greyscale image to a 2-bit greyscale image with dithering. As for `dither2mono`, the dithering algorithm is currently very simple.

### `grey42grey`(image  width  height)

Convert a 4-bit greyscale image to an 8-bit greyscale image.

### `grey22grey`(image  width  height)

Convert a 2-bit greyscale image to an 8-bit greyscale image.
# Built-in module `imgfile`

The imgfile module allows python programs to access SGI imglib image files (also known as `.rgb` files). The module is far from complete, but is provided anyway since the functionality that there is is enough in some cases. Currently, colormap files are not supported.

The module defines the following variables and functions:

### exception `error`

This exception is raised on all errors, such as unsupported file type, etc.

### `getsizes`(file)

This function returns a tuple `(`*`x`*`, `*`y`*`, `*`z`*`)` where *x* and *y* are the size of the image in pixels and *z* is the number of bytes per pixel. Only 3 byte RGB pixels and 1 byte greyscale pixels are currently supported.

### `read`(file)

This function reads and decodes the image on the specified file, and returns it as a python string. The string has either 1 byte greyscale pixels or 4 byte RGBA pixels. The bottom left pixel is the first in the string. This format is suitable to pass to `gl.lrectwrite`, for instance.

### `readscaled`(file  x  y  filter)

This function is identical to read but it returns an image that is scaled to the given *x* and *y* sizes. If the *filter* and *blur* parameters are omitted scaling is done by simply dropping or duplicating pixels, so the result will be less than perfect, especially for computer-generated images.

Alternatively, you can specify a filter to use to smoothen the image after scaling. The filter forms supported are `’impulse’`, `’box’`, `’triangle’`, `’quadratic’` and `’gaussian’`. If a filter is specified *blur* is an optional parameter specifying the blurriness of the filter. It defaults to `1.0`.

`readscaled` makes no attempt to keep the aspect ratio correct, so that is the users’ responsibility.

### `ttob`(flag)

This function sets a global flag which defines whether the scan lines of the image are read or written from bottom to top (flag is zero, compatible with SGI GL) or from top to bottom(flag is one, compatible with X). The default is zero.

### `write`(file  data  x  y  z)

This function writes the RGB or greyscale data in *data* to image file *file*. *x* and *y* give the size of the image, *z* is 1 for 1 byte greyscale images or 3 for RGB images (which are stored as 4 byte values of which only the lower three bytes are used). These are the formats returned by `gl.lrectread`.
# Introduction

The Python library consists of three parts, with different levels of integration with the interpreter. Closest to the interpreter are built-in types, exceptions and functions. Next are built-in modules, which are written in C and linked statically with the interpreter. Finally there are standard modules that are implemented entirely in Python, but are always available. For efficiency, some standard modules may become built-in modules in future versions of the interpreter.
# Built-in Module `jpeg`

The module jpeg provides access to the jpeg compressor and decompressor written by the Independent JPEG Group. JPEG is a (draft?) standard for compressing pictures. For details on jpeg or the Independent JPEG Group software refer to the JPEG standard or the documentation provided with the software.

The jpeg module defines these functions:

### `compress`(data  w  h  b)

Treat data as a pixmap of width w and height h, with b bytes per pixel. The data is in SGI GL order, so the first pixel is in the lower-left corner. This means that lrectread return data can immedeately be passed to compress. Currently only 1 byte and 4 byte pixels are allowed, the former being treated as greyscale and the latter as RGB color. Compress returns a string that contains the compressed picture, in JFIF format.

### `decompress`(data)

Data is a string containing a picture in JFIF format. It returns a tuple `(`*`data`*`, `*`width`*`, `*`height`*`, `*`bytesperpixel`*`)`. Again, the data is suitable to pass to lrectwrite.

### `setoption`(name  value)

Set various options. Subsequent compress and decompress calls will use these options. The following options are available:

`’forcegray’`  
Force output to be grayscale, even if input is RGB.

`’quality’`  
Set the quality of the compressed image to a value between `0` and `100` (default is `75`). Compress only.

`’optimize’`  
Perform Huffman table optimization. Takes longer, but results in smaller compressed image. Compress only.

`’smooth’`  
Perform inter-block smoothing on uncompressed image. Only useful for low-quality images. Decompress only.

Compress and uncompress raise the error jpeg.error in case of errors.
# MACINTOSH ONLY

The following modules are available on the Apple Macintosh only.

## Built-in module `mac`

This module provides a subset of the operating system dependent functionality provided by the optional built-in module `posix`. It is best accessed through the more portable standard module `os`.

The following functions are available in this module: `chdir`, `getcwd`, `listdir`, `mkdir`, `rename`, `rmdir`, `stat`, `sync`, `unlink`, as well as the exception `error`.

## Standard module `macpath`

This module provides a subset of the pathname manipulation functions available from the optional standard module `posixpath`. It is best accessed through the more portable standard module `os`, as `os.path`.

The following functions are available in this module: `normcase`, `isabs`, `join`, `split`, `isdir`, `isfile`, `exists`.
# Built-in Module `__main__`

This module represents the (otherwise anonymous) scope in which the interpreter’s main program executes — commands read either from standard input or from a script file.
# Built-in Module `marshal`

This module contains functions that can read and write Python values in a binary format. The format is specific to Python, but independent of machine architecture issues (e.g., you can write a Python value to a file on a VAX, transport the file to a Mac, and read it back there). Details of the format not explained here; read the source if you’re interested. [^1]

Not all Python object types are supported; in general, only objects whose value is independent from a particular invocation of Python can be written and read by this module. The following types are supported: `None`, integers, long integers, floating point numbers, strings, tuples, lists, dictionaries, and code objects, where it should be understood that tuples, lists and dictionaries are only supported as long as the values contained therein are themselves supported; and recursive lists and dictionaries should not be written (they will cause an infinite loop).

There are functions that read/write files as well as functions operating on strings.

The module defines these functions:

### `dump`(value  file)

Write the value on the open file. The value must be a supported type. The file must be an open file object such as `sys.stdout` or returned by `open()` or `posix.popen()`.

If the value has an unsupported type, garbage is written which cannot be read back by `load()`.

### `load`(file)

Read one value from the open file and return it. If no valid value is read, raise `EOFError`, `ValueError` or `TypeError`. The file must be an open file object.

### `dumps`(value)

Return the string that would be written to a file by `dump(value, file)`. The value must be a supported type.

### `loads`(string)

Convert the string to a value. If no valid value is found, raise `EOFError`, `ValueError` or `TypeError`. Extra characters in the string are ignored.

[^1]: The name of this module stems from a bit of terminology used by the designers of Modula-3 (amongst others), who use the term “marshalling” for shipping of data around in a self-contained form. Strictly speaking, “to marshal” means to convert some data from internal to external form (in an RPC buffer for instance) and “unmarshalling” for the reverse process.
# Built-in Module `math`

This module is always available. It provides access to the mathematical functions defined by the C standard. They are:

### `acos`(x)

`acos()`, `asin()`, `atan()`, `atan2()`, `ceil()`, `cos()`, `cosh()`, `exp()`, `fabs()`, `floor()`, `fmod()`, `frexp()`, `ldexp()`, `log()`, `log10()`, `modf()`, `pow()`, `sin()`, `sinh()`, `sqrt()`, `tan()`, `tanh()`.

Note that `frexp` and `modf` have a different call/return pattern than their C equivalents: they take a single argument and return a pair of values, rather than returning their second return value through an ‘output parameter’ (there is no such thing in Python).

The module also defines two mathematical constants:

### `pi`

`pi` and `e`.
# Built-in module `md5`

This module implements the interface to RSA’s MD5 message digest algorithm (see also the file `md5.doc`). Its use is quite straightforward: use the function `md5` to create an *md5*-object. You can now “feed” this object with arbitrary strings.

At any time you can ask for the “final” digest of the object. Internally, a temporary copy of the object is made and the digest is computed and returned. Because of the copy, the digest operation is not destructive for the object. Before a more exact description of the module’s use, a small example will be helpful: to obtain the digest of the string `’abc’`, use …

    >>> from md5 import md5
    >>> m = md5()
    >>> m.update('abc')
    >>> m.digest()
    '\220\001P\230<\322O\260\326\226?}(\341\177r'

More condensed:

    >>> md5('abc').digest()
    '\220\001P\230<\322O\260\326\226?}(\341\177r'

### `md5`()

Create a new md5-object. If *arg* is present, an initial `update` method is called with *arg* as argument.

An md5-object has the following methods:

### `update`(arg)

Update this md5-object with the string *arg*.

### `digest`()

Return the *digest* of this md5-object. Internally, a copy is made and the C-function `MD5Final` is called. Finally the digest is returned.

### `copy`()

Return a separate copy of this md5-object. An `update` to this copy won’t affect the original object.
# MULTIMEDIA EXTENSIONS

The modules described in this chapter implement various algorithms that are mainly useful for multimedia applications. They are available at the discretion of the installation.
# Built-in Modules

The modules described in this chapter are built into the interpreter and considered part of Python’s standard environment: they are always available.[^1]

[^1]: at least in theory — it is possible to specify at build time that one or more of these modules should be excluded, but it would be antisocial to do so.
# Built-in module `mpz`

This module implements the interface to part of the GNU MP library. This library contains arbitrary precision integer and rational number arithmetic routines. Only the interfaces to the *integer* (`mpz_``…`) routines are provided. If not stated otherwise, the description in the GNU MP documentation can be applied.

In general, *mpz*-numbers can be used just like other standard Python numbers, e.g. you can use the built-in operators like `+`, `*`, etc., as well as the standard built-in functions like `abs`, `int`, …, `divmod`, `pow`. **Please note:** the *bitwise-xor* operation has been implemented as a bunch of *and*s, *invert*s and *or*s, because the library lacks an `mpz_xor` function, and I didn’t need one.

You create an mpz-number, by calling the function called `mpz` (see below for an excact description). An mpz-number is printed like this: `mpz(`*`value`*`)`.

### `mpz`(value)

Create a new mpz-number. *value* can be an integer, a long, another mpz-number, or even a string. If it is a string, it is interpreted as an array of radix-256 digits, least significant digit first, resulting in a positive number. See also the `binary` method, described below.

A number of *extra* functions are defined in this module. Non mpz-arguments are converted to mpz-values first, and the functions return mpz-numbers.

### `powm`(base  exponent  modulus)

Return `pow(`*`base`*`, `*`exponent`*`) % `*`modulus`*. If *`exponent`*` == 0`, return `mpz(1)`. In contrast to the C-library function, this version can handle negative exponents.

### `gcd`(op1  op2)

Return the greatest common divisor of *op1* and *op2*.

### `gcdext`(a  b)

Return a tuple `(`*`g`*`, `*`s`*`, `*`t`*`)`, such that *`a`*`*`*`s`*` + `*`b`*`*`*`t`*` == `*`g`*` == gcd(`*`a`*`, `*`b`*`)`.

### `sqrt`(op)

Return the square root of *op*. The result is rounded towards zero.

### `sqrtrem`(op)

Return a tuple `(`*`root`*`, `*`remainder`*`)`, such that *`root`*`*`*`root`*` + `*`remainder`*` == `*`op`*.

### `divm`(numerator  denominator  modulus)

Returns a number *q*. such that *`q`*` * `*`denominator`*` % `*`modulus`*` == `*`numerator`*. One could also implement this function in python, using `gcdext`.

An mpz-number has one method:

### `binary`()

Convert this mpz-number to a binary string, where the number has been stored as an array of radix-256 digits, least significant digit first.

The mpz-number must have a value greater than- or equal to zero, otherwise a `ValueError`-exception will be raised.
# Built-in Types, Exceptions and Functions

Names for built-in exceptions and functions are found in a separate symbol table. This table is searched last, so local and global user-defined names can override built-in names. Built-in types have no names but are created easily by constructing an object of the desired type (e.g., using a literal) and applying the built-in function `type()` to it. They are described together here for easy reference. [^1]

[^1]: Some descriptions sorely lack explanations of the exceptions that may be raised — this will be fixed in a future version of this document.
# Standard Module `os`

This module provides a more portable way of using operating system (OS) dependent functionality than importing an OS dependent built-in module like `posix`.

When the optional built-in module `posix` is available, this module exports the same functions and data as `posix`; otherwise, it searches for an OS dependent built-in module like `mac` and exports the same functions and data as found there. The design of all Python’s built-in OS dependen modules is such that as long as the same functionality is available, it uses the same interface; e.g., the function `os.stat(`*`file`*`)` returns stat info about a *file* in a format compatible with the POSIX interface.

Extensions peculiar to a particular OS are also available through the `os` module, but using them is of course a threat to portability!

Note that after the first time `os` is imported, there is *no* performance penalty in using functions from `os` instead of directly from the OS dependent built-in module, so there should be *no* reason not to use `os`!

In addition to whatever the correct OS dependent module exports, the following variables and functions are always exported by `os`:

### `name`

The name of the OS dependent module imported, e.g. `’posix’` or `’mac’`.

### `path`

The corresponding OS dependent standard module for pathname operations, e.g., `posixpath` or `macpath`. Thus, (given the proper imports), `os.path.split(`*`file`*`)` is equivalent to but more portable than `posixpath.split(`*`file`*`)`.

### `curdir`

The constant string used by the OS to refer to the current directory, e.g. `’.’` for POSIX or `’:’` for the Mac.

### `pardir`

The constant string used by the OS to refer to the parent directory, e.g. `’..’` for POSIX or `’::’` for the Mac.

### `sep`

The character used by the OS to separate pathname components, e.g. `’/’` for POSIX or `’:’` for the Mac. Note that knowing this is not sufficient to be able to parse or concatenate pathnames—better use `os.path.split()` and `os.path.join()`—but it is occasionally useful.

### `execl`(path  arg0  arg1  ...)

This is equivalent to a call to `os.execv` with an *argv* of `[`*`arg0`*`, `*`arg1`*`, ...]`.

### `execle`(path  arg0  arg1  ...  env)

This is equivalent to a call to `os.execve` with an *argv* of `[`*`arg0`*`, `*`arg1`*`, ...]`.

### `execlp`(path  arg0  arg1  ...)

This is like `execl` but duplicates the shell’s actions in searching for an executable file in a list of directories. The directory list is obtained from `environ[’PATH’]`.

### `execvp`(path  arg0  arg1  ...)

`execvp` is for `execv` what `execlp` is for `execl`.
# Standard Module `panel`

**Please note:** The FORMS library, to which the `fl` module described above interfaces, is a simpler and more accessible user interface library for use with GL than the Panel Module (besides also being by a Dutch author).

This module should be used instead of the built-in module `pnl` to interface with the *Panel Library*.

The module is too large to document here in its entirety. One interesting function:

### `defpanellist`(filename)

Parses a panel description file containing S-expressions written by the *Panel Editor* that accompanies the Panel Library and creates the described panels. It returns a list of panel objects.

**Warning:** the Python interpreter will dump core if you don’t create a GL window before calling `panel.mkpanel()` or `panel.defpanellist()`.

# Standard Module `panelparser`

This module defines a self-contained parser for S-expressions as output by the Panel Editor (which is written in Scheme so it can’t help writing S-expressions). The relevant function is `panelparser.parse_file(`*`file`*`)` which has a file object (not a filename!) as argument and returns a list of parsed S-expressions. Each S-expression is converted into a Python list, with atoms converted to Python strings and sub-expressions (recursively) to Python lists. For more details, read the module file.

# Built-in Module `pnl`

This module provides access to the *Panel Library* built by NASA Ames (to get it, send e-mail to `panel-request@nas.nasa.gov`). All access to it should be done through the standard module `panel`, which transparantly exports most functions from `pnl` but redefines `pnl.dopanel()`.

**Warning:** the Python interpreter will dump core if you don’t create a GL window before calling `pnl.mkpanel()`.

The module is too large to document here in its entirety.
# Built-in Module `posix`

This module provides access to operating system functionality that is standardized by the C Standard and the POSIX standard (a thinly diguised Unix interface). It is available in all Python versions except on the Macintosh; the MS-DOS version does not support certain functions. The descriptions below are very terse; refer to the corresponding Unix manual entry for more information.

Errors are reported as exceptions; the usual exceptions are given for type errors, while errors reported by the system calls raise `posix.error`, described below.

Module `posix` defines the following data items:

### `environ`

A dictionary representing the string environment at the time the interpreter was started. (Modifying this dictionary does not affect the string environment of the interpreter.) For example, `posix.environ[’HOME’]` is the pathname of your home directory, equivalent to `getenv("HOME")` in C.

### exception `error`

This exception is raised when an POSIX function returns a POSIX-related error (e.g., not for illegal argument types). Its string value is `’posix.error’`. The accompanying value is a pair containing the numeric error code from `errno` and the corresponding string, as would be printed by the C function `perror()`.

It defines the following functions:

### `chdir`(path)

Change the current working directory to *path*.

### `chmod`(path  mode)

Change the mode of *path* to the numeric *mode*.

### `close`(fd)

Close file descriptor *fd*.

### `dup`(fd)

Return a duplicate of file descriptor *fd*.

### `dup2`(fd  fd2)

Duplicate file descriptor *fd* to *fd2*, closing the latter first if necessary. Return `None`.

### `execv`(path  args)

Execute the executable *path* with argument list *args*, replacing the current process (i.e., the Python interpreter). The argument list may be a tuple or list of strings. (Not on MS-DOS.)

### `execve`(path  args  env)

Execute the executable *path* with argument list *args*, and environment *env*, replacing the current process (i.e., the Python interpreter). The argument list may be a tuple or list of strings. The environment must be a dictionary mapping strings to strings. (Not on MS-DOS.)

### `_exit`(n)

Exit to the system with status *n*, without calling cleanup handlers, flushing stdio buffers, etc. (Not on MS-DOS.)

Note: the standard way to exit is `sys.exit(`*`n`*`)`. `posix._exit()` should normally only be used in the child process after a `fork()`.

### `fdopen`(fd  mode)

Return an open file object connected to the file descriptor *fd*, open for reading and/or writing according to the *mode* string (which has the same meaning as the *mode* argument to the built-in `open()` function.

### `fork`()

Fork a child process. Return 0 in the child, the child’s process id in the parent. (Not on MS-DOS.)

### `fstat`(fd)

Return status for file descriptor *fd*, like `stat()`.

### `getcwd`()

Return a string representing the current working directory.

### `getegid`()

Return the current process’s effective group id. (Not on MS-DOS.)

### `geteuid`()

Return the current process’s effective user id. (Not on MS-DOS.)

### `getgid`()

Return the current process’s group id. (Not on MS-DOS.)

### `getpid`()

Return the current process id. (Not on MS-DOS.)

### `getppid`()

Return the parent’s process id. (Not on MS-DOS.)

### `getuid`()

Return the current process’s user id. (Not on MS-DOS.)

### `kill`(pid  sig)

Kill the process *pid* with signal *sig*. (Not on MS-DOS.)

### `link`(src  dst)

Create a hard link pointing to *src* named *dst*. (Not on MS-DOS.)

### `listdir`(path)

Return a list containing the names of the entries in the directory. The list is in arbitrary order. It includes the special entries `’.’` and `’..’` if they are present in the directory.

### `lseek`(fd  pos  how)

Set the current position of file descriptor *fd* to position *pos*, modified by *how*: 0 to set the position relative to the beginning of the file; 1 to set it relative to the current position; 2 to set it relative to the end of the file.

### `lstat`(path)

Like `stat()`, but do not follow symbolic links. (On systems without symbolic links, this is identical to `posix.stat`.)

### `mkdir`(path  mode)

Create a directory named *path* with numeric mode *mode*.

### `nice`(increment)

Add *incr* to the process’ “niceness”. Return the new niceness. (Not on MS-DOS.)

### `open`(file  flags  mode)

Open the file *file* and set various flags according to *flags* and possibly its mode according to *mode*. Return the file descriptor for the newly opened file.

### `pipe`()

Create a pipe. Return a pair of file descriptors `(r, w)` usable for reading and writing, respectively. (Not on MS-DOS.)

### `popen`(command  mode)

Open a pipe to or from *command*. The return value is an open file object connected to the pipe, which can be read or written depending on whether *mode* is `’r’` or `’w’`. (Not on MS-DOS.)

### `read`(fd  n)

Read at most *n* bytes from file descriptor *fd*. Return a string containing the bytes read.

### `readlink`(path)

Return a string representing the path to which the symbolic link points. (On systems without symbolic links, this always raises `posix.error`.)

### `rename`(src  dst)

Rename the file or directory *src* to *dst*.

### `rmdir`(path)

Remove the directory *path*.

### `setgid`(gid)

Set the current process’s group id. (Not on MS-DOS.)

### `setuid`(uid)

Set the current process’s user id. (Not on MS-DOS.)

### `stat`(path)

Perform a *stat* system call on the given path. The return value is a tuple of at least 10 integers giving the most important (and portable) members of the *stat* structure, in the order `st_mode`, `st_ino`, `st_dev`, `st_nlink`, `st_uid`, `st_gid`, `st_size`, `st_atime`, `st_mtime`, `st_ctime`. More items may be added at the end by some implementations. (On MS-DOS, some items are filled with dummy values.)

Note: The standard module `stat` defines functions and constants that are useful for extracting information from a stat structure.

### `symlink`(src  dst)

Create a symbolic link pointing to *src* named *dst*. (On systems without symbolic links, this always raises `posix.error`.)

### `system`(command)

Execute the command (a string) in a subshell. This is implemented by calling the Standard C function `system()`, and has the same limitations. Changes to `posix.environ`, `sys.stdin` etc. are not reflected in the environment of the executed command. The return value is the exit status of the process as returned by Standard C `system()`.

### `times`()

Return a 4-tuple of floating point numbers indicating accumulated CPU times, in seconds. The items are: user time, system time, children’s user time, and children’s system time, in that order. See the Unix manual page *times*(2). (Not on MS-DOS.)

### `umask`(mask)

Set the current numeric umask and returns the previous umask. (Not on MS-DOS.)

### `uname`()

Return a 5-tuple containing information identifying the current operating system. The tuple contains 5 strings: `(`*`sysname`*`, `*`nodename`*`, `*`release`*`, `*`version`*`, `*`machine`*`)`. Some systems truncate the nodename to 8 characters or to the leading component; an better way to get the hostname is `socket.gethostname()`. (Not on MS-DOS, nor on older Unix systems.)

### `unlink`(path)

Unlink *path*.

### `utime`(path  atime, mtime)

Set the access and modified time of the file to the given values. (The second argument is a tuple of two items.)

### `wait`()

Wait for completion of a child process, and return a tuple containing its pid and exit status indication (encoded as by Unix). (Not on MS-DOS.)

### `waitpid`(pid  options)

Wait for completion of a child process given by proces id, and return a tuple containing its pid and exit status indication (encoded as by Unix). The semantics of the call are affected by the value of the integer options, which should be 0 for normal operation. (If the system does not support waitpid(), this always raises `posix.error`. Not on MS-DOS.)

### `write`(fd  str)

Write the string *str* to file descriptor *fd*. Return the number of bytes actually written.
# Standard Module `posixfile`

This module implements some additional functionality over the built-in file objects. In particular, it implements file locking, control over the file flags, and an easy interface to duplicate the file object. The module defines a new file object, the posixfile object. It inherits all the standard file object methods and adds the methods described below.

To instantiate a posixfile object, use the `open()` function in the posixfile module. The resulting object looks and feels the same as a standard file object.

The posixfile module defines the following constants:

### `SEEK_SET`

offset is calculated from the start of the file

### `SEEK_CUR`

offset is calculated from the current position in the file

### `SEEK_END`

offset is calculated from the end of the file

The posixfile module defines the following functions:

### `open`(filename  mode)

Create a new posixfile object with the given filename and mode. The filename and mode are interpreted the same way as the `open()` builtin function.

### `openfile`(fileobject)

Create a new posixfile object with the given standard file object. The resulting object has the same filename and mode as the original file object.

The posixfile object defines the following additional methods:

### `lock`(fmt  )

Lock the specified section of the file that the file object is referring to. The format is explained below in a table. The *len* argument specifies the length of the section that should be locked. The default is `0`. *start* specifies the starting offset of the section, where the default is `0`. The *whence* argument specifies where the offset is relative to. It accepts one of the constants `SEEK_SET`, `SEEK_CUR` or `SEEK_END`. The default is `SEEK_SET`. For more information about the arguments refer to the fcntl manual page on your system.

### `flags`(fmt)

Set the specified flags for the file that the file object is referring to. The new flags are ORed with the old flags, unless specified otherwise. The format is explained below in a table. Without arguments a string indicating the current flags is returned (this is the same as the ’?’ modifier). For more information about the flags refer to the fcntl manual page on your system.

### `dup`()

Duplicate the file object and the underlying file pointer and file descriptor. The resulting object behaves as if it were newly opened.

### `dup2`(fd)

Duplicate the file object and the underlying file pointer and file descriptor. The new object will have the given file descriptor. Otherwise the resulting object behaves as if it were newly opened.

### `file`()

Return the standard file object that the posixfile object is based on. This is sometimes necessary for functions that insist on a standard file object.

All methods return `IOError` when the request fails.

Format characters for the `lock()` method have the following meaning:

|     |                                                |     |
|:----|:-----------------------------------------------|:----|
| u   | unlock the specified region                    |     |
| r   | request a read lock for the specified section  |     |
| w   | request a write lock for the specified section |     |

In addition the following modifiers can be added to the format:

|     |                                                            |       |
|:----|:-----------------------------------------------------------|:------|
| \|  | wait until the lock has been granted                       |       |
| ?   | return the first lock conflicting with the requested lock, | \(1\) |
|     |  or `None` if there is no conflict.                        |       |

Note:

\(1\) The lock returned is in the format `(mode, len, start, whence, pid)` where mode is a character representing the type of lock (’r’ or ’w’). This modifier prevents a request from being granted; it is for query purposes only.

Format character for the `flags()` method have the following meaning:

|     |                                               |     |
|:----|:----------------------------------------------|:----|
| a   | append only flag                              |     |
| c   | close on exec flag                            |     |
| n   | no delay flag (also called non-blocking flag) |     |
| s   | synchronization flag                          |     |

In addition the following modifiers can be added to the format:

|  |  |  |
|:---|:---|:---|
| ! | turn the specified flags ’off’, instead of the default ’on’ | \(1\) |
| = | replace the flags, instead of the default ’OR’ operation | \(1\) |
| ? | return a string in which the characters represent the flags that are set. | \(2\) |

Note:

\(1\) The `!` and `=` modifiers are mutually exclusive.

\(2\) This string represents the flags after they may have been altered by the same call.

Examples:

    from posixfile import *

    file = open('/tmp/test', 'w')
    file.lock('w|')
    ...
    file.lock('u')
    file.close()
# Built-in Module `pwd`

This module provides access to the Unix password database. It is available on all Unix versions.

Password database entries are reported as 7-tuples containing the following items from the password database (see `<pwd.h>`), in order: `pw_name`, `pw_passwd`, `pw_uid`, `pw_gid`, `pw_gecos`, `pw_dir`, `pw_shell`. The uid and gid items are integers, all others are strings. An exception is raised if the entry asked for cannot be found.

It defines the following items:

### `getpwuid`(uid)

Return the password database entry for the given numeric user ID.

### `getpwnam`(name)

Return the password database entry for the given user name.

### `getpwall`()

Return a list of all available password database entries, in arbitrary order.
# Standard Module `rand`

This module implements a pseudo-random number generator with an interface similar to `rand()` in C. It defines the following functions:

### `rand`()

Returns an integer random number in the range [0 ... 32768).

### `choice`(s)

Returns a random element from the sequence (string, tuple or list) *s*.

### `srand`(seed)

Initializes the random number generator with the given integral seed. When the module is first imported, the random number is initialized with the current time.
# Standard Module `regsub`

This module defines a number of functions useful for working with regular expressions (see built-in module `regex`).

### `sub`(pat  repl  str)

Replace the first occurrence of pattern *pat* in string *str* by replacement *repl*. If the pattern isn’t found, the string is returned unchanged. The pattern may be a string or an already compiled pattern. The replacement may contain references *`digit`* to subpatterns and escaped backslashes.

### `gsub`(pat  repl  str)

Replace all (non-overlapping) occurrences of pattern *pat* in string *str* by replacement *repl*. The same rules as for `sub()` apply. Empty matches for the pattern are replaced only when not adjacent to a previous match, so e.g. `gsub(’’, ’-’, ’abc’)` returns `’-a-b-c-’`.

### `split`(str  pat)

Split the string *str* in fields separated by delimiters matching the pattern *pat*, and return a list containing the fields. Only non-empty matches for the pattern are considered, so e.g. `split(’a:b’, ’:*’)` returns `[’a’, ’b’]` and `split(’abc’, ’’)` returns `[’abc’]`.
# Built-in module `rgbimg`

The rgbimg module allows python programs to access SGI imglib image files (also known as `.rgb` files). The module is far from complete, but is provided anyway since the functionality that there is is enough in some cases. Currently, colormap files are not supported.

The module defines the following variables and functions:

### exception `error`

This exception is raised on all errors, such as unsupported file type, etc.

### `sizeofimage`(file)

This function returns a tuple `(`*`x`*`, `*`y`*`)` where *x* and *y* are the size of the image in pixels. Only 4 byte RGBA pixels, 3 byte RGB pixels, and 1 byte greyscale pixels are currently supported.

### `longimagedata`(file)

This function reads and decodes the image on the specified file, and returns it as a python string. The string has 4 byte RGBA pixels. The bottom left pixel is the first in the string. This format is suitable to pass to `gl.lrectwrite`, for instance.

### `longstoimage`(data  x  y  z  file)

This function writes the RGBA data in *data* to image file *file*. *x* and *y* give the size of the image. *z* is 1 if the saved image should be 1 byte greyscale, 3 if the saved image should be 3 byte RGB data, or 4 if the saved images should be 4 byte RGBA data. The input data always contains 4 bytes per pixel. These are the formats returned by `gl.lrectread`.

### `ttob`(flag)

This function sets a global flag which defines whether the scan lines of the image are read or written from bottom to top (flag is zero, compatible with SGI GL) or from top to bottom(flag is one, compatible with X). The default is zero.
# Built-in module `rotor`

This module implements a rotor-based encryption algorithm, contributed by Lance Ellinghouse. The design is derived from the Enigma device, a machine used during World War II to encipher messages. A rotor is simply a permutation. For example, if the character ‘A’ is the origin of the rotor, then a given rotor might map ‘A’ to ‘L’, ‘B’ to ‘Z’, ‘C’ to ‘G’, and so on. To encrypt, we choose several different rotors, and set the origins of the rotors to known positions; their initial position is the ciphering key. To encipher a character, we permute the original character by the first rotor, and then apply the second rotor’s permutation to the result. We continue until we’ve applied all the rotors; the resulting character is our ciphertext. We then change the origin of the final rotor by one position, from ‘A’ to ‘B’; if the final rotor has made a complete revolution, then we rotate the next-to-last rotor by one position, and apply the same procedure recursively. In other words, after enciphering one character, we advance the rotors in the same fashion as a car’s odometer. Decoding works in the same way, except we reverse the permutations and apply them in the opposite order.

The available functions in this module are:

### `newrotor`(key)

Returns a rotor object. *key* is a string containing the encryption key for the object; it can contain arbitrary binary data. The key will be used to randomly generate the rotor permutations and their initial positions. *numrotors* is the number of rotor permutations in the returned object; if it is omitted, a default value of 6 will be used.

Rotor objects have the following methods:

### `setkey`()

Resets the rotor to its initial state.

### `encrypt`(plaintext)

Resets the rotor object to its initial state and encrypts *plaintext*, returning a string containing the ciphertext. The ciphertext is always the same length as the original plaintext.

### `encryptmore`(plaintext)

Encrypts *plaintext* without resetting the rotor object, and returns a string containing the ciphertext.

### `decrypt`(ciphertext)

Resets the rotor object to its initial state and decrypts *ciphertext*, returning a string containing the ciphertext. The plaintext string will always be the same length as the ciphertext.

### `decryptmore`(ciphertext)

Decrypts *ciphertext* without resetting the rotor object, and returns a string containing the ciphertext.

An example usage:

    >>> import rotor
    >>> rt = rotor.newrotor('key', 12)
    >>> rt.encrypt('bar')
    '\2534\363'
    >>> rt.encryptmore('bar')
    '\357\375$'
    >>> rt.encrypt('bar')
    '\2534\363'
    >>> rt.decrypt('\2534\363')
    'bar'
    >>> rt.decryptmore('\357\375$')
    'bar'
    >>> rt.decrypt('\357\375$')
    'l(\315'
    >>> del rt

The module’s code is not an exact simulation of the original Enigma device; it implements the rotor encryption scheme differently from the original. The most important difference is that in the original Enigma, there were only 5 or 6 different rotors in existence, and they were applied twice to each character; the cipher key was the order in which they were placed in the machine. The Python rotor module uses the supplied key to initialize a random number generator; the rotor permutations and their initial positions are then randomly generated. The original device only enciphered the letters of the alphabet, while this module can handle any 8-bit binary data; it also produces binary output. This module can also operate with an arbitrary number of rotors.

The original Enigma cipher was broken in 1944. The version implemented here is probably a good deal more difficult to crack (especially if you use many rotors), but it won’t be impossible for a truly skilful and determined attacker to break the cipher. So if you want to keep the NSA out of your files, this rotor cipher may well be unsafe, but for discouraging casual snooping through your files, it will probably be just fine, and may be somewhat safer than using the Unix `crypt` command.
# Built-in module `select`

This module provides access to the function `select` available in most Unix versions. It defines the following:

### exception `error`

The exception raised when an error occurs. The accompanying value is a pair containing the numeric error code from `errno` and the corresponding string, as would be printed by the C function `perror()`.

### `select`(iwtd  owtd  ewtd  timeout)

This is a straightforward interface to the Unix `select()` system call. The first three arguments are lists of ‘waitable objects’: either integers representing Unix file descriptors or objects with a parameterless method named `fileno()` returning such an integer. The three lists of waitable objects are for input, output and ‘exceptional conditions’, respectively. Empty lists are allowed. The optional last argument is a time-out specified as a floating point number in seconds. When the *timeout* argument is omitted the function blocks until at least one file descriptor is ready. A time-out value of zero specifies a poll and never blocks.

The return value is a triple of lists of objects that are ready: subsets of the first three arguments. When the time-out is reached without a file descriptor becoming ready, three empty lists are returned.

Amongst the acceptable object types in the lists are Python file objects (e.g. `sys.stdin`, or objects returned by `open()` or `posix.popen()`), socket objects returned by `socket.socket()`, and the module `stdwin` which happens to define a function `fileno()` for just this purpose. You may also define a *wrapper* class yourself, as long as it has an appropriate `fileno()` method (that really returns a Unix file descriptor, not just a random integer).
# SGI IRIX ONLY

The modules described in this chapter provide interfaces to features that are unique to SGI’s IRIX operating system (versions 4 and 5).
# Built-in Module `socket`

This module provides access to the BSD *socket* interface. It is available on Unix systems that support this interface.

For an introduction to socket programming (in C), see the following papers: *An Introductory 4.3BSD Interprocess Communication Tutorial*, by Stuart Sechrest and *An Advanced 4.3BSD Interprocess Communication Tutorial*, by Samuel J. Leffler et al, both in the Unix Programmer’s Manual, Supplementary Documents 1 (sections PS1:7 and PS1:8). The Unix manual pages for the various socket-related system calls also a valuable source of information on the details of socket semantics.

The Python interface is a straightforward transliteration of the Unix system call and library interface for sockets to Python’s object-oriented style: the `socket()` function returns a *socket object* whose methods implement the various socket system calls. Parameter types are somewhat higer-level than in the C interface: as with `read()` and `write()` operations on Python files, buffer allocation on receive operations is automatic, and buffer length is implicit on send operations.

Socket addresses are represented as a single string for the `AF_UNIX` address family and as a pair `(`*`host`*`, `*`port`*`)` for the `AF_INET` address family, where *host* is a string representing either a hostname in Internet domain notation like `’daring.cwi.nl’` or an IP address like `’100.50.200.5’`, and *port* is an integral port number. Other address families are currently not supported. The address format required by a particular socket object is automatically selected based on the address family specified when the socket object was created.

All errors raise exceptions. The normal exceptions for invalid argument types and out-of-memory conditions can be raised; errors related to socket or address semantics raise the error `socket.error`.

Non-blocking and asynchronous mode are not supported; see module `select` for a way to do non-blocking socket I/O.

The module `socket` exports the following constants and functions:

### exception `error`

This exception is raised for socket- or address-related errors. The accompanying value is either a string telling what went wrong or a pair `(`*`errno`*`, `*`string`*`)` representing an error returned by a system call, similar to the value accompanying `posix.error`.

### `AF_UNIX`

These constants represent the address (and protocol) families, used for the first argument to `socket()`. If the `AF_UNIX` constant is not defined then this protocol is unsupported.

### `SOCK_STREAM`

These constants represent the socket types, used for the second argument to `socket()`. (Only `SOCK_STREAM` and `SOCK_DGRAM` appear to be generally useful.)

### `gethostbyname`(hostname)

Translate a host name to IP address format. The IP address is returned as a string, e.g., `’100.50.200.5’`. If the host name is an IP address itself it is returned unchanged.

### `gethostname`()

Return a string containing the hostname of the machine where the Python interpreter is currently executing. If you want to know the current machine’s IP address, use `socket.gethostbyname( socket.gethostname() )` instead.

### `getservbyname`(servicename  protocolname)

Translate an Internet service name and protocol name to a port number for that service. The protocol name should be `’tcp’` or `’udp’`.

### `socket`(family  type  proto)

Create a new socket using the given address family, socket type and protocol number. The address family should be `AF_INET` or `AF_UNIX`. The socket type should be `SOCK_STREAM`, `SOCK_DGRAM` or perhaps one of the other `SOCK_` constants. The protocol number is usually zero and may be omitted in that case.

### `fromfd`(fd  family  type  proto)

Build a socket object from an existing file descriptor (an integer as returned by a file object’s `fileno` method). Address family, socket type and protocol number are as for the `socket` function above. The file descriptor should refer to a socket, but this is not checked — subsequent operations on the object may fail if the file descriptor is invalid. This function is rarely needed, but can be used to get or set socket options on a socket passed to a program as standard input or output (e.g. a server started by the Unix inet daemon).

## Socket Object Methods

Socket objects have the following methods. Except for `makefile()` these correspond to Unix system calls applicable to sockets.

### `accept`()

Accept a connection. The socket must be bound to an address and listening for connections. The return value is a pair `(`*`conn`*`, `*`address`*`)` where *conn* is a *new* socket object usable to send and receive data on the connection, and *address* is the address bound to the socket on the other end of the connection.

### `bind`(address)

Bind the socket to *address*. The socket must not already be bound. (The format of *address* depends on the address family – see above.)

### `close`()

Close the socket. All future operations on the socket object will fail. The remote end will receive no more data (after queued data is flushed). Sockets are automatically closed when they are garbage-collected.

### `connect`(address)

Connect to a remote socket at *address*. (The format of *address* depends on the address family – see above.)

### `fileno`()

Return the socket’s file descriptor (a small integer). This is useful with `select`.

### `getpeername`()

Return the remote address to which the socket is connected. This is useful to find out the port number of a remote IP socket, for instance. (The format of the address returned depends on the address family – see above.) On some systems this function is not supported.

### `getsockname`()

Return the socket’s own address. This is useful to find out the port number of an IP socket, for instance. (The format of the address returned depends on the address family – see above.)

### `getsockopt`(level  optname  buflen)

Return the value of the given socket option (see the Unix man page *getsockopt*(2)). The needed symbolic constants are defined in module SOCKET. If the optional third argument is absent, an integer option is assumed and its integer value is returned by the function. If *buflen* is present, it specifies the maximum length of the buffer used to receive the option in, and this buffer is returned as a string. It’s up to the caller to decode the contents of the buffer (see the optional built-in module `struct` for a way to decode C structures encoded as strings).

### `listen`(backlog)

Listen for connections made to the socket. The argument specifies the maximum number of queued connections and should be at least 1; the maximum value is system-dependent.

### `makefile`(mode)

Return a *file object* associated with the socket. (File objects were described earlier under Built-in Types.) The file object references a `dup`ped version of the socket file descriptor, so the file object and socket object may be closed or garbage-collected independently.

### `recv`(bufsize  flags)

Receive data from the socket. The return value is a string representing the data received. The maximum amount of data to be received at once is specified by *bufsize*. See the Unix manual page for the meaning of the optional argument *flags*; it defaults to zero.

### `recvfrom`(bufsize)

Receive data from the socket. The return value is a pair `(`*`string`*`, `*`address`*`)` where *string* is a string representing the data received and *address* is the address of the socket sending the data. (The format of *address* depends on the address family – see above.)

### `send`(string)

Send data to the socket. The socket must be connected to a remote socket. Return the number of bytes sent.

### `sendto`(string  address)

Send data to the socket. The socket should not be connected to a remote socket, since the destination socket is specified by `address`. Return the number of bytes sent. (The format of *address* depends on the address family – see above.)

### `setblocking`(flag)

Set blocking or non-blocking mode of the socket: if *flag* is 0, the socket is set to non-blocking, else to blocking mode. Initially all sockets are in blocking mode. In non-blocking mode, if a `recv` call doesn’t find any data, or if a `send` call can’t immediately dispose of the data, a `socket.error` exception is raised; in blocking mode, the calls block until they can proceed.

### `setsockopt`(level  optname  value)

Set the value of the given socket option (see the Unix man page *setsockopt*(2)). The needed symbolic constants are defined in module `SOCKET`. The value can be an integer or a string representing a buffer. In the latter case it is up to the caller to ensure that the string contains the proper bits (see the optional built-in module `struct` for a way to encode C structures as strings).

### `shutdown`(how)

Shut down one or both halves of the connection. If *how* is `0`, further receives are disallowed. If *how* is `1`, further sends are disallowed. If *how* is `2`, further sends and receives are disallowed.

Note that there are no methods `read()` or `write()`; use `recv()` and `send()` without *flags* argument instead.

## Example

Here are two minimal example programs using the TCP/IP protocol: a server that echoes all data that it receives back (servicing only one client), and a client using it. Note that a server must perform the sequence `socket`, `bind`, `listen`, `accept` (possibly repeating the `accept` to service more than one client), while a client only needs the sequence `socket`, `connect`. Also note that the server does not `send`/`receive` on the socket it is listening on but on the new socket returned by `accept`.

    # Echo server program
    from socket import *
    HOST = ''                 # Symbolic name meaning the local host
    PORT = 50007              # Arbitrary non-privileged server
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(HOST, PORT)
    s.listen(1)
    conn, addr = s.accept()
    print 'Connected by', addr
    while 1:
        data = conn.recv(1024)
        if not data: break
        conn.send(data)
    conn.close()

    # Echo client program
    from socket import *
    HOST = 'daring.cwi.nl'    # The remote host
    PORT = 50007              # The same port as used by the server
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(HOST, PORT)
    s.send('Hello, world')
    data = s.recv(1024)
    s.close()
    print 'Received', `data`
# Standard Modules

The modules described in this chapter are implemented in Python, but are considered to be a part of Python’s standard environment: they are always available.[^1]

[^1]: at least in theory — it is possible to botch the library installation or to sabotage the module search path so that these modules cannot be found.
# STDWIN ONLY

## Built-in Module `stdwin`

This module defines several new object types and functions that provide access to the functionality of the Standard Window System Interface, STDWIN [CWI report CR-R8817]. It is available on systems to which STDWIN has been ported (which is most systems). It is only available if the `DISPLAY` environment variable is set or an explicit `-display `*`displayname`* argument is passed to the interpreter.

Functions have names that usually resemble their C STDWIN counterparts with the initial ‘w’ dropped. Points are represented by pairs of integers; rectangles by pairs of points. For a complete description of STDWIN please refer to the documentation of STDWIN for C programmers (aforementioned CWI report).

### Functions Defined in Module `stdwin`

The following functions are defined in the `stdwin` module:

#### `open`(title)

Open a new window whose initial title is given by the string argument. Return a window object; window object methods are described below. [^1]

#### `getevent`()

Wait for and return the next event. An event is returned as a triple: the first element is the event type, a small integer; the second element is the window object to which the event applies, or `None` if it applies to no window in particular; the third element is type-dependent. Names for event types and command codes are defined in the standard module `stdwinevent`.

#### `pollevent`()

Return the next event, if one is immediately available. If no event is available, return `()`.

#### `getactive`()

Return the window that is currently active, or `None` if no window is currently active. (This can be emulated by monitoring WE_ACTIVATE and WE_DEACTIVATE events.)

#### `listfontnames`(pattern)

Return the list of font names in the system that match the pattern (a string). The pattern should normally be `’*’`; returns all available fonts. If the underlying window system is X11, other patterns follow the standard X11 font selection syntax (as used e.g. in resource definitions), i.e. the wildcard character `’*’` matches any sequence of characters (including none) and `’?’` matches any single character.

#### `setdefscrollbars`(hflag  vflag)

Set the flags controlling whether subsequently opened windows will have horizontal and/or vertical scroll bars.

#### `setdefwinpos`(h  v)

Set the default window position for windows opened subsequently.

#### `setdefwinsize`(width  height)

Set the default window size for windows opened subsequently.

#### `getdefscrollbars`()

Return the flags controlling whether subsequently opened windows will have horizontal and/or vertical scroll bars.

#### `getdefwinpos`()

Return the default window position for windows opened subsequently.

#### `getdefwinsize`()

Return the default window size for windows opened subsequently.

#### `getscrsize`()

Return the screen size in pixels.

#### `getscrmm`()

Return the screen size in millimeters.

#### `fetchcolor`(colorname)

Return the pixel value corresponding to the given color name. Return the default foreground color for unknown color names. Hint: the following code tests whether you are on a machine that supports more than two colors:

    if stdwin.fetchcolor('black') <> \
              stdwin.fetchcolor('red') <> \
              stdwin.fetchcolor('white'):
        print 'color machine'
    else:
        print 'monochrome machine'

#### `setfgcolor`(pixel)

Set the default foreground color. This will become the default foreground color of windows opened subsequently, including dialogs.

#### `setbgcolor`(pixel)

Set the default background color. This will become the default background color of windows opened subsequently, including dialogs.

#### `getfgcolor`()

Return the pixel value of the current default foreground color.

#### `getbgcolor`()

Return the pixel value of the current default background color.

#### `setfont`(fontname)

Set the current default font. This will become the default font for windows opened subsequently, and is also used by the text measuring functions `textwidth`, `textbreak`, `lineheight` and `baseline` below. This accepts two more optional parameters, size and style: Size is the font size (in ‘points’). Style is a single character specifying the style, as follows: `’b’` = bold, `’i’` = italic, `’o’` = bold + italic, `’u’` = underline; default style is roman. Size and style are ignored under X11 but used on the Macintosh. (Sorry for all this complexity — a more uniform interface is being designed.)

#### `menucreate`(title)

Create a menu object referring to a global menu (a menu that appears in all windows). Methods of menu objects are described below. Note: normally, menus are created locally; see the window method `menucreate` below. **Warning:** the menu only appears in a window as long as the object returned by this call exists.

#### `newbitmap`(width  height)

Create a new bitmap object of the given dimensions. Methods of bitmap objects are described below.

#### `fleep`()

Cause a beep or bell (or perhaps a ‘visual bell’ or flash, hence the name).

#### `message`(string)

Display a dialog box containing the string. The user must click OK before the function returns.

#### `askync`(prompt  default)

Display a dialog that prompts the user to answer a question with yes or no. Return 0 for no, 1 for yes. If the user hits the Return key, the default (which must be 0 or 1) is returned. If the user cancels the dialog, the `KeyboardInterrupt` exception is raised.

#### `askstr`(prompt  default)

Display a dialog that prompts the user for a string. If the user hits the Return key, the default string is returned. If the user cancels the dialog, the `KeyboardInterrupt` exception is raised.

#### `askfile`(prompt  default  new)

Ask the user to specify a filename. If *new* is zero it must be an existing file; otherwise, it must be a new file. If the user cancels the dialog, the `KeyboardInterrupt` exception is raised.

#### `setcutbuffer`(i  string)

Store the string in the system’s cut buffer number *i*, where it can be found (for pasting) by other applications. On X11, there are 8 cut buffers (numbered 0..7). Cut buffer number 0 is the ‘clipboard’ on the Macintosh.

#### `getcutbuffer`(i)

Return the contents of the system’s cut buffer number *i*.

#### `rotatecutbuffers`(n)

On X11, rotate the 8 cut buffers by *n*. Ignored on the Macintosh.

#### `getselection`(i)

Return X11 selection number *i.* Selections are not cut buffers. Selection numbers are defined in module `stdwinevents`. Selection `WS_PRIMARY` is the *primary* selection (used by xterm, for instance); selection `WS_SECONDARY` is the *secondary* selection; selection `WS_CLIPBOARD` is the *clipboard* selection (used by xclipboard). On the Macintosh, this always returns an empty string.

#### `resetselection`(i)

Reset selection number *i*, if this process owns it. (See window method `setselection()`).

#### `baseline`()

Return the baseline of the current font (defined by STDWIN as the vertical distance between the baseline and the top of the characters).

#### `lineheight`()

Return the total line height of the current font.

#### `textbreak`(str  width)

Return the number of characters of the string that fit into a space of *width* bits wide when drawn in the curent font.

#### `textwidth`(str)

Return the width in bits of the string when drawn in the current font.

#### `connectionnumber`()

(X11 under Unix only) Return the “connection number” used by the underlying X11 implementation. (This is normally the file number of the socket.) Both functions return the same value; `connectionnumber()` is named after the corresponding function in X11 and STDWIN, while `fileno()` makes it possible to use the `stdwin` module as a “file” object parameter to `select.select()`. Note that if `select()` implies that input is possible on `stdwin`, this does not guarantee that an event is ready — it may be some internal communication going on between the X server and the client library. Thus, you should call `stdwin.pollevent()` until it returns `None` to check for events if you don’t want your program to block. Because of internal buffering in X11, it is also possible that `stdwin.pollevent()` returns an event while `select()` does not find `stdwin` to be ready, so you should read any pending events with `stdwin.pollevent()` until it returns `None` before entering a blocking `select()` call.

### Window Object Methods

Window objects are created by `stdwin.open()`. They are closed by their `close()` method or when they are garbage-collected. Window objects have the following methods:

#### `begindrawing`()

Return a drawing object, whose methods (described below) allow drawing in the window.

#### `change`(rect)

Invalidate the given rectangle; this may cause a draw event.

#### `gettitle`()

Returns the window’s title string.

#### `getdocsize`()

Return a pair of integers giving the size of the document as set by `setdocsize()`.

#### `getorigin`()

Return a pair of integers giving the origin of the window with respect to the document.

#### `gettitle`()

Return the window’s title string.

#### `getwinsize`()

Return a pair of integers giving the size of the window.

#### `getwinpos`()

Return a pair of integers giving the position of the window’s upper left corner (relative to the upper left corner of the screen).

#### `menucreate`(title)

Create a menu object referring to a local menu (a menu that appears only in this window). Methods of menu objects are described below. **Warning:** the menu only appears as long as the object returned by this call exists.

#### `scroll`(rect  point)

Scroll the given rectangle by the vector given by the point.

#### `setdocsize`(point)

Set the size of the drawing document.

#### `setorigin`(point)

Move the origin of the window (its upper left corner) to the given point in the document.

#### `setselection`(i  str)

Attempt to set X11 selection number *i* to the string *str*. (See stdwin method `getselection()` for the meaning of *i*.) Return true if it succeeds. If succeeds, the window “owns” the selection until (a) another application takes ownership of the selection; or (b) the window is deleted; or (c) the application clears ownership by calling `stdwin.resetselection(`*`i`*`)`. When another application takes ownership of the selection, a `WE_LOST_SEL` event is received for no particular window and with the selection number as detail. Ignored on the Macintosh.

#### `settimer`(dsecs)

Schedule a timer event for the window in *`dsecs`*`/10` seconds.

#### `settitle`(title)

Set the window’s title string.

#### `setwincursor`(name)

Set the window cursor to a cursor of the given name. It raises the `RuntimeError` exception if no cursor of the given name exists. Suitable names include `’ibeam’`, `’arrow’`, `’cross’`, `’watch’` and `’plus’`. On X11, there are many more (see `<X11/cursorfont.h>`).

#### `setwinpos`(h  v)

Set the the position of the window’s upper left corner (relative to the upper left corner of the screen).

#### `setwinsize`(width  height)

Set the window’s size.

#### `show`(rect)

Try to ensure that the given rectangle of the document is visible in the window.

#### `textcreate`(rect)

Create a text-edit object in the document at the given rectangle. Methods of text-edit objects are described below.

#### `setactive`()

Attempt to make this window the active window. If successful, this will generate a WE_ACTIVATE event (and a WE_DEACTIVATE event in case another window in this application became inactive).

#### `close`()

Discard the window object. It should not be used again.

### Drawing Object Methods

Drawing objects are created exclusively by the window method `begindrawing()`. Only one drawing object can exist at any given time; the drawing object must be deleted to finish drawing. No drawing object may exist when `stdwin.getevent()` is called. Drawing objects have the following methods:

#### `box`(rect)

Draw a box just inside a rectangle.

#### `circle`(center  radius)

Draw a circle with given center point and radius.

#### `elarc`(center  rh, rv  a1, a2)

Draw an elliptical arc with given center point. `(`*`rh`*`, `*`rv`*`)` gives the half sizes of the horizontal and vertical radii. `(`*`a1`*`, `*`a2`*`)` gives the angles (in degrees) of the begin and end points. 0 degrees is at 3 o’clock, 90 degrees is at 12 o’clock.

#### `erase`(rect)

Erase a rectangle.

#### `fillcircle`(center  radius)

Draw a filled circle with given center point and radius.

#### `fillelarc`(center  rh, rv  a1, a2)

Draw a filled elliptical arc; arguments as for `elarc`.

#### `fillpoly`(points)

Draw a filled polygon given by a list (or tuple) of points.

#### `invert`(rect)

Invert a rectangle.

#### `line`(p1  p2)

Draw a line from point *p1* to *p2*.

#### `paint`(rect)

Fill a rectangle.

#### `poly`(points)

Draw the lines connecting the given list (or tuple) of points.

#### `shade`(rect  percent)

Fill a rectangle with a shading pattern that is about *percent* percent filled.

#### `text`(p  str)

Draw a string starting at point p (the point specifies the top left coordinate of the string).

#### `xorcircle`(center  radius)

Draw a circle, an elliptical arc, a line or a polygon, respectively, in XOR mode.

#### `setfgcolor`()

These functions are similar to the corresponding functions described above for the `stdwin` module, but affect or return the colors currently used for drawing instead of the global default colors. When a drawing object is created, its colors are set to the window’s default colors, which are in turn initialized from the global default colors when the window is created.

#### `setfont`()

These functions are similar to the corresponding functions described above for the `stdwin` module, but affect or use the current drawing font instead of the global default font. When a drawing object is created, its font is set to the window’s default font, which is in turn initialized from the global default font when the window is created.

#### `bitmap`(point  bitmap  mask)

Draw the *bitmap* with its top left corner at *point*. If the optional *mask* argument is present, it should be either the same object as *bitmap*, to draw only those bits that are set in the bitmap, in the foreground color, or `None`, to draw all bits (ones are drawn in the foreground color, zeros in the background color).

#### `cliprect`(rect)

Set the “clipping region” to a rectangle. The clipping region limits the effect of all drawing operations, until it is changed again or until the drawing object is closed. When a drawing object is created the clipping region is set to the entire window. When an object to be drawn falls partly outside the clipping region, the set of pixels drawn is the intersection of the clipping region and the set of pixels that would be drawn by the same operation in the absence of a clipping region.

#### `noclip`()

Reset the clipping region to the entire window.

#### `close`()

Discard the drawing object. It should not be used again.

### Menu Object Methods

A menu object represents a menu. The menu is destroyed when the menu object is deleted. The following methods are defined:

#### `additem`(text  shortcut)

Add a menu item with given text. The shortcut must be a string of length 1, or omitted (to specify no shortcut).

#### `setitem`(i  text)

Set the text of item number *i*.

#### `enable`(i  flag)

Enable or disables item *i*.

#### `check`(i  flag)

Set or clear the *check mark* for item *i*.

#### `close`()

Discard the menu object. It should not be used again.

### Bitmap Object Methods

A bitmap represents a rectangular array of bits. The top left bit has coordinate (0, 0). A bitmap can be drawn with the `bitmap` method of a drawing object. The following methods are defined:

#### `getsize`()

Return a tuple representing the width and height of the bitmap. (This returns the values that have been passed to the `newbitmap` function.)

#### `setbit`(point  bit)

Set the value of the bit indicated by *point* to *bit*.

#### `getbit`(point)

Return the value of the bit indicated by *point*.

#### `close`()

Discard the bitmap object. It should not be used again.

### Text-edit Object Methods

A text-edit object represents a text-edit block. For semantics, see the STDWIN documentation for C programmers. The following methods exist:

#### `arrow`(code)

Pass an arrow event to the text-edit block. The *code* must be one of `WC_LEFT`, `WC_RIGHT`, `WC_UP` or `WC_DOWN` (see module `stdwinevents`).

#### `draw`(rect)

Pass a draw event to the text-edit block. The rectangle specifies the redraw area.

#### `event`(type  window  detail)

Pass an event gotten from `stdwin.getevent()` to the text-edit block. Return true if the event was handled.

#### `getfocus`()

Return 2 integers representing the start and end positions of the focus, usable as slice indices on the string returned by `gettext()`.

#### `getfocustext`()

Return the text in the focus.

#### `getrect`()

Return a rectangle giving the actual position of the text-edit block. (The bottom coordinate may differ from the initial position because the block automatically shrinks or grows to fit.)

#### `gettext`()

Return the entire text buffer.

#### `move`(rect)

Specify a new position for the text-edit block in the document.

#### `replace`(str)

Replace the text in the focus by the given string. The new focus is an insert point at the end of the string.

#### `setfocus`(i  j)

Specify the new focus. Out-of-bounds values are silently clipped.

#### `settext`(str)

Replace the entire text buffer by the given string and set the focus to `(0, 0)`.

#### `setview`(rect)

Set the view rectangle to *rect*. If *rect* is `None`, viewing mode is reset. In viewing mode, all output from the text-edit object is clipped to the viewing rectangle. This may be useful to implement your own scrolling text subwindow.

#### `close`()

Discard the text-edit object. It should not be used again.

### Example

Here is a minimal example of using STDWIN in Python. It creates a window and draws the string “Hello world” in the top left corner of the window. The window will be correctly redrawn when covered and re-exposed. The program quits when the close icon or menu item is requested.

    import stdwin
    from stdwinevents import *

    def main():
        mywin = stdwin.open('Hello')
        #
        while 1:
            (type, win, detail) = stdwin.getevent()
            if type == WE_DRAW:
                draw = win.begindrawing()
                draw.text((0, 0), 'Hello, world')
                del draw
            elif type == WE_CLOSE:
                break

    main()

## Standard Module `stdwinevents`

This module defines constants used by STDWIN for event types (`WE_ACTIVATE` etc.), command codes (`WC_LEFT` etc.) and selection types (`WS_PRIMARY` etc.). Read the file for details. Suggested usage is

    >>> from stdwinevents import *
    >>> 

## Standard Module `rect`

This module contains useful operations on rectangles. A rectangle is defined as in module `stdwin`: a pair of points, where a point is a pair of integers. For example, the rectangle

    (10, 20), (90, 80)

is a rectangle whose left, top, right and bottom edges are 10, 20, 90 and 80, respectively. Note that the positive vertical axis points down (as in `stdwin`).

The module defines the following objects:

#### exception `error`

The exception raised by functions in this module when they detect an error. The exception argument is a string describing the problem in more detail.

#### `empty`

The rectangle returned when some operations return an empty result. This makes it possible to quickly check whether a result is empty:

    >>> import rect
    >>> r1 = (10, 20), (90, 80)
    >>> r2 = (0, 0), (10, 20)
    >>> r3 = rect.intersect([r1, r2])
    >>> if r3 is rect.empty: print 'Empty intersection'
    Empty intersection
    >>> 

#### `is_empty`(r)

Returns true if the given rectangle is empty. A rectangle `(`*`left`*`, `*`top`*`), (`*`right`*`, `*`bottom`*`)` is empty if *`left`*` >= `*`right`* or *`top`*` => `*`bottom`*. left ≥ right or top ≥ bottom.

#### `intersect`(list)

Returns the intersection of all rectangles in the list argument. It may also be called with a tuple argument. Raises `rect.error` if the list is empty. Returns `rect.empty` if the intersection of the rectangles is empty.

#### `union`(list)

Returns the smallest rectangle that contains all non-empty rectangles in the list argument. It may also be called with a tuple argument or with two or more rectangles as arguments. Returns `rect.empty` if the list is empty or all its rectangles are empty.

#### `pointinrect`(point  rect)

Returns true if the point is inside the rectangle. By definition, a point `(`*`h`*`, `*`v`*`)` is inside a rectangle `(`*`left`*`, `*`top`*`), (`*`right`*`, `*`bottom`*`)` if *`left`*` <= `*`h`*` < `*`right`* and *`top`*` <= `*`v`*` < `*`bottom`*. left ≤ h \< right and top ≤ v \< bottom.

#### `inset`(rect  dh, dv)

Returns a rectangle that lies inside the `rect` argument by *dh* pixels horizontally and *dv* pixels vertically. If *dh* or *dv* is negative, the result lies outside *rect*.

#### `rect2geom`(rect)

Converts a rectangle to geometry representation: `(`*`left`*`, `*`top`*`), (`*`width`*`, `*`height`*`)`.

#### `geom2rect`(geom)

Converts a rectangle given in geometry representation back to the standard rectangle representation `(`*`left`*`, `*`top`*`), (`*`right`*`, `*`bottom`*`)`.

[^1]: The Python version of STDWIN does not support draw procedures; all drawing requests are reported as draw events.
# Standard Module `string`

This module defines some constants useful for checking character classes, some exceptions, and some useful string functions. The constants are:

### `digits`

The string `’0123456789’`.

### `hexdigits`

The string `’0123456789abcdefABCDEF’`.

### `letters`

The concatenation of the strings `lowercase` and `uppercase` described below.

### `lowercase`

A string containing all the characters that are considered lowercase letters. On most systems this is the string `’abcdefghijklmnopqrstuvwxyz’`. Do not change its definition – the effect on the routines `upper` and `swapcase` is undefined.

### `octdigits`

The string `’01234567’`.

### `uppercase`

A string containing all the characters that are considered uppercase letters. On most systems this is the string `’ABCDEFGHIJKLMNOPQRSTUVWXYZ’`. Do not change its definition – the effect on the routines `lower` and `swapcase` is undefined.

### `whitespace`

A string containing all characters that are considered whitespace. On most systems this includes the characters space, tab, linefeed, return, formfeed, and vertical tab. Do not change its definition – the effect on the routines `strip` and `split` is undefined.

The exceptions are:

The functions are:

### `atof`(s)

Convert a string to a floating point number. The string must have the standard syntax for a floating point literal in Python, optionally preceded by a sign (`+` or `-`).

### `atoi`(s)

Convert a string to an integer. The string must consist of one or more digits, optionally preceded by a sign (`+` or `-`).

### `atol`(s)

Convert a string to a long integer. The string must consist of one or more digits, optionally preceded by a sign (`+` or `-`).

### `expandtabs`(s  tabsize)

Expand tabs in a string, i.e. replace them by one or more spaces, depending on the current column and the given tab size. The column number is reset to zero after each newline occurring in the string. This doesn’t understand other non-printing characters or escape sequences.

### `find`(s  sub)

Return the lowest index in *s* not smaller than *start* where the substring *sub* is found. Return `-1` when *sub* does not occur as a substring of *s* with index at least *start*. If *start* is omitted, it defaults to `0`. If *start* is negative, `len(`*`s`*`)` is added.

### `rfind`(s  sub)

Like `find` but finds the highest index.

### `index`(s  sub)

Like `find` but raise `ValueError` when the substring is not found.

### `rindex`(s  sub)

Like `rfind` but raise `ValueError` when the substring is not found.

### `count`(s  sub  i)

Return the number of (non-overlapping) occurrences of substring *sub* in string *s* with index at least *i*. If *i* is omitted, it defaults to `0`.

### `lower`(s)

Convert letters to lower case.

### `split`(s)

Returns a list of the whitespace-delimited words of the string *s*.

### `splitfields`(s  sep)

Returns a list containing the fields of the string *s*, using the string *sep* as a separator. The list will have one more items than the number of non-overlapping occurrences of the separator in the string. Thus, `string.splitfields(`*`s`*`, ’ ’)` is not the same as `string.split(`*`s`*`)`, as the latter only returns non-empty words. As a special case, `splitfields(`*`s`*`, ’’)` returns `[`*`s`*`]`, for any string *s*. (See also `regsub.split()`.)

### `join`(words)

Concatenate a list or tuple of words with intervening spaces.

### `joinfields`(words  sep)

Concatenate a list or tuple of words with intervening separators. It is always true that `string.joinfields(string.splitfields(`*`t`*`, `*`sep`*`), `*`sep`*`)` equals *t*.

### `strip`(s)

Removes leading and trailing whitespace from the string *s*.

### `swapcase`(s)

Converts lower case letters to upper case and vice versa.

### `upper`(s)

Convert letters to upper case.

### `ljust`(s  width)

These functions respectively left-justify, right-justify and center a string in a field of given width. They return a string that is at least *width* characters wide, created by padding the string *s* with spaces until the given width on the right, left or both sides. The string is never truncated.

### `zfill`(s  width)

Pad a numeric string on the left with zero digits until the given width is reached. Strings starting with a sign are handled correctly.
# Built-in module `struct`

This module performs conversions between Python values and C structs represented as Python strings. It uses *format strings* (explained below) as compact descriptions of the lay-out of the C structs and the intended conversion to/from Python values.

The module defines the following exception and functions:

### exception `error`

Exception raised on various occasions; argument is a string describing what is wrong.

### `pack`(fmt  v1  v2  …)

Return a string containing the values *`v1`*`, `*`v2`*`, ``…` packed according to the given format. The arguments must match the values required by the format exactly.

### `unpack`(fmt  string)

Unpack the string (presumably packed by `pack(`*`fmt`*`, ``…``)`) according to the given format. The result is a tuple even if it contains exactly one item. The string must contain exactly the amount of data required by the format (i.e. `len(`*`string`*`)` must equal `calcsize(`*`fmt`*`)`).

### `calcsize`(fmt)

Return the size of the struct (and hence of the string) corresponding to the given format.

Format characters have the following meaning; the conversion between C and Python values should be obvious given their types:

|     |             |                    |
|:----|:------------|:-------------------|
| x   | pad byte    | no value           |
| c   | char        | string of length 1 |
| b   | signed char | integer            |
| h   | short       | integer            |
| i   | int         | integer            |
| l   | long        | integer            |
| f   | float       | float              |
| d   | double      | float              |

A format character may be preceded by an integral repeat count; e.g. the format string `’4h’` means exactly the same as `’hhhh’`.

C numbers are represented in the machine’s native format and byte order, and properly aligned by skipping pad bytes if necessary (according to the rules used by the C compiler).

Examples (all on a big-endian machine):

    pack('hhl', 1, 2, 3) == '\000\001\000\002\000\000\000\003'
    unpack('hhl', '\000\001\000\002\000\000\000\003') == (1, 2, 3)
    calcsize('hhl') == 8

Hint: to align the end of a structure to the alignment requirement of a particular type, end the format with the code for that type with a repeat count of zero, e.g. the format `’llh0l’` specifies two pad bytes at the end, assuming longs are aligned on 4-byte boundaries.

(More format characters are planned, e.g. `’s’` for character arrays, upper case for unsigned variants, and a way to specify the byte order, which is useful for [de]constructing network packets and reading/writing portable binary file formats like TIFF and AIFF.)
# SUNOS ONLY

The modules described in this chapter provide interfaces to features that are unique to the SunOS operating system (versions 4 and 5; the latter is also known as SOLARIS version 2).

## Built-in module `sunaudiodev`

This module allows you to access the sun audio interface. The sun audio hardware is capable of recording and playing back audio data in U-LAW format with a sample rate of 8K per second. A full description can be gotten with `man audio`.

The module defines the following variables and functions:

#### exception `error`

This exception is raised on all errors. The argument is a string describing what went wrong.

#### `open`(mode)

This function opens the audio device and returns a sun audio device object. This object can then be used to do I/O on. The *mode* parameter is one of `’r’` for record-only access, `’w’` for play-only access, `’rw’` for both and `’control’` for access to the control device. Since only one process is allowed to have the recorder or player open at the same time it is a good idea to open the device only for the activity needed. See the audio manpage for details.

### Audio device object methods

The audio device objects are returned by `open` define the following methods (except `control` objects which only provide getinfo, setinfo and drain):

#### `close`()

This method explicitly closes the device. It is useful in situations where deleting the object does not immediately close it since there are other references to it. A closed device should not be used again.

#### `drain`()

This method waits until all pending output is processed and then returns. Calling this method is often not necessary: destroying the object will automatically close the audio device and this will do an implicit drain.

#### `flush`()

This method discards all pending output. It can be used avoid the slow response to a user’s stop request (due to buffering of up to one second of sound).

#### `getinfo`()

This method retrieves status information like input and output volume, etc. and returns it in the form of an audio status object. This object has no methods but it contains a number of attributes describing the current device status. The names and meanings of the attributes are described in `/usr/include/sun/audioio.h` and in the audio man page. Member names are slightly different from their C counterparts: a status object is only a single structure. Members of the `play` substructure have `o_` prepended to their name and members of the `record` structure have `i_`. So, the C member `play.sample_rate` is accessed as `o_sample_rate`, `record.gain` as `i_gain` and `monitor_gain` plainly as `monitor_gain`.

#### `ibufcount`()

This method returns the number of samples that are buffered on the recording side, i.e. the program will not block on a `read` call of so many samples.

#### `obufcount`()

This method returns the number of samples buffered on the playback side. Unfortunately, this number cannot be used to determine a number of samples that can be written without blocking since the kernel output queue length seems to be variable.

#### `read`(size)

This method reads *size* samples from the audio input and returns them as a python string. The function blocks until enough data is available.

#### `setinfo`(status)

This method sets the audio device status parameters. The *status* parameter is an device status object as returned by `getinfo` and possibly modified by the program.

#### `write`(samples)

Write is passed a python string containing audio samples to be played. If there is enough buffer space free it will immedeately return, otherwise it will block.

There is a companion module, `SUNAUDIODEV`, which defines useful symbolic constants like `MIN_GAIN`, `MAX_GAIN`, `SPEAKER`, etc. The names of the constants are the same names as used in the C include file `<sun/audioio.h>`, with the leading string `AUDIO_` stripped.

Useability of the control device is limited at the moment, since there is no way to use the ’wait for something to happen’ feature the device provides. This is because that feature makes heavy use of signals, and these do not map too well onto Python.
# Built-in Module `sys`

This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.

### `argv`

The list of command line arguments passed to a Python script. `sys.argv[0]` is the script name. If no script name was passed to the Python interpreter, `sys.argv` is empty.

### `builtin_module_names`

A list of strings giving the names of all modules that are compiled into this Python interpreter. (This information is not available in any other way — `sys.modules.keys()` only lists the imported modules.)

### `check_interval`

When this variable is set to an integer value, it determines how often the interpreter checks for periodic things such as thread switches and signal handlers. The default is 10, meaning the check is performed every 10 Python virtual instructions. Setting this to a large value may increase performance for programs using threads. Setting it to a value \<= 0 checks every virtual instruction, maximizing responsiveness as well as overhead.

### `exc_type`

These three variables are not always defined; they are set when an exception handler (an `except` clause of a `try` statement) is invoked. Their meaning is: `exc_type` gets the exception type of the exception being handled; `exc_value` gets the exception parameter (its *associated value* or the second argument to `raise`); `exc_traceback` gets a traceback object which encapsulates the call stack at the point where the exception originally occurred.

### `exit`(n)

Exit from Python with numeric exit status *n*. This is implemented by raising the `SystemExit` exception, so cleanup actions specified by `finally` clauses of `try` statements are honored, and it is possible to catch the exit attempt at an outer level.

### `exitfunc`

This value is not actually defined by the module, but can be set by the user (or by a program) to specify a clean-up action at program exit. When set, it should be a parameterless function. This function will be called when the interpreter exits in any way (but not when a fatal error occurs: in that case the interpreter’s internal state cannot be trusted).

### `last_type`

These three variables are not always defined; they are set when an exception is not handled and the interpreter prints an error message and a stack traceback. Their intended use is to allow an interactive user to import a debugger module and engage in post-mortem debugging without having to re-execute the command that caused the error (which may be hard to reproduce). The meaning of the variables is the same as that of `exc_type`, `exc_value` and `exc_tracaback`, respectively.

### `modules`

Gives the list of modules that have already been loaded. This can be manipulated to force reloading of modules and other tricks.

### `path`

A list of strings that specifies the search path for modules. Initialized from the environment variable `PYTHONPATH`, or an installation-dependent default.

### `ps1`

Strings specifying the primary and secondary prompt of the interpreter. These are only defined if the interpreter is in interactive mode. Their initial values in this case are `’>>> ’` and `’... ’`.

### `settrace`(tracefunc)

Set the system’s trace function, which allows you to implement a Python source code debugger in Python. The standard modules `pdb` and `wdb` are such debuggers; the difference is that `wdb` uses windows and needs STDWIN, while `pdb` has a line-oriented interface not unlike dbx. See the file `pdb.doc` in the Python library source directory for more documentation (both about `pdb` and `sys.trace`).

### `setprofile`(profilefunc)

Set the system’s profile function, which allows you to implement a Python source code profiler in Python. The system’s profile function is called similarly to the system’s trace function (see `sys.settrace`), but it isn’t called for each executed line of code (only on call and return and when an exception occurs). Also, its return value is not used, so it can just return `None`.

### `stdin`

File objects corresponding to the interpreter’s standard input, output and error streams. `sys.stdin` is used for all interpreter input except for scripts but including calls to `input()` and `raw_input()`. `sys.stdout` is used for the output of `print` and expression statements and for the prompts of `input()` and `raw_input()`. The interpreter’s own prompts and (almost all of) its error messages go to `sys.stderr`. `sys.stdout` and `sys.stderr` needn’t be built-in file objects: any object is acceptable as long as it has a `write` method that takes a string argument.

### `tracebacklimit`

When this variable is set to an integer value, it determines the maximum number of levels of traceback information printed when an unhandled exception occurs. The default is 1000. When set to 0 or less, all traceback information is suppressed and only the exception type and value are printed.
# Built-in module `YOUR-MODULE-NAME`

# Standard module `YOUR-MODULE-NAME`

PUT A SHORT INTRODUCTION AND DESCRIPTION OF THE MODULE HERE.

The module defines the following variables and functions:



DESCRIPTION OF THE EXCEPTION GOES HERE.

DESCRIPTION OF THE VARIABLE/CONSTANT GOES HERE.

DESCRIPTION OF THE FUNCTION GOES HERE.



ADDITIONAL HINTS FOR USING THE MODULE MAY GO HERE.
# Built-in Module `thread`

This module provides low-level primitives for working with multiple threads (a.k.a. *light-weight processes* or *tasks*) — multiple threads of control sharing their global data space. For synchronization, simple locks (a.k.a. *mutexes* or *binary semaphores*) are provided.

The module is optional and supported on SGI IRIX 4.x and 5.x and Sun Solaris 2.x systems, as well as on systems that have a PTHREAD implementation (e.g. KSR).

It defines the following constant and functions:

### exception `error`

Raised on thread-specific errors.

### `start_new_thread`(func  arg)

Start a new thread. The thread executes the function *func* with the argument list *arg* (which must be a tuple). When the function returns, the thread silently exits. When the function raises terminates with an unhandled exception, a stack trace is printed and then the thread exits (but other threads continue to run).

### `exit_thread`()

Exit the current thread silently. Other threads continue to run. **Caveat:** code in pending `finally` clauses is not executed.

### `exit_prog`(status)

Exit all threads and report the value of the integer argument *status* as the exit status of the entire program. **Caveat:** code in pending `finally` clauses, in this thread or in other threads, is not executed.

### `allocate_lock`()

Return a new lock object. Methods of locks are described below. The lock is initially unlocked.

### `get_ident`()

Return the ‘thread identifier’ of the current thread. This is a nonzero integer. Its value has no direct meaning; it is intended as a magic cookie to be used e.g. to index a dictionary of thread-specific data. Thread identifiers may be recycled when a thread exits and another thread is created.

Lock objects have the following methods:

### `acquire`(waitflag)

Without the optional argument, this method acquires the lock unconditionally, if necessary waiting until it is released by another thread (only one thread at a time can acquire a lock — that’s their reason for existence), and returns `None`. If the integer *waitflag* argument is present, the action depends on its value: if it is zero, the lock is only acquired if it can be acquired immediately without waiting, while if it is nonzero, the lock is acquired unconditionally as before. If an argument is present, the return value is 1 if the lock is acquired successfully, 0 if not.

### `release`()

Releases the lock. The lock must have been acquired earlier, but not necessarily by the same thread.

### `locked`()

Return the status of the lock: 1 if it has been acquired by some thread, 0 if not.

**Caveats:**

- Threads interact strangely with interrupts: the `KeyboardInterrupt` exception will be received by an arbitrary thread.

- Calling `sys.exit(`*`status`*`)` or executing `raise SystemExit, `*`status`* is almost equivalent to calling `thread.exit_prog(`*`status`*`)`, except that the former ways of exiting the entire program do honor `finally` clauses in the current thread (but not in other threads).

- Not all built-in functions that may block waiting for I/O allow other threads to run, although the most popular ones (`sleep`, `read`, `select`) work as expected.
# Built-in Module `time`

This module provides various time-related functions. It is always available.

An explanation of some terminology and conventions is in order.

- The “epoch” is the point where the time starts. On January 1st of that year, at 0 hours, the “time since the epoch” is zero. For UNIX, the epoch is 1970. To find out what the epoch is, look at the first element of `gmtime(0)`.

- UTC is Coordinated Universal Time (formerly known as Greenwich Mean Time). The acronym UTC is not a mistake but a compromise between English and French.

- DST is Daylight Saving Time, an adjustment of the timezone by (usually) one hour during part of the year. DST rules are magic (determined by local law) and can change from year to year. The C library has a table containing the local rules (often it is read from a system file for flexibility) and is the only source of True Wisdom in this respect.

- The precision of the various real-time functions may be less than suggested by the units in which their value or argument is expressed. E.g. on most UNIX systems, the clock “ticks” only every 1/50th or 1/100th of a second, and on the Mac, it ticks 60 times a second.

Functions and data items are:

### `altzone`

The offset of the local DST timezone, in seconds west of the 0th meridian, if one is defined. Only use this if `daylight` is nonzero.

### `asctime`(tuple)

Convert a tuple representing a time as returned by `gmtime()` or `localtime()` to a 24-character string of the following form: `’Sun Jun 20 23:21:05 1993’`. Note: unlike the C function of the same name, there is no trailing newline.

### `clock`()

Return the current CPU time as a floating point number expressed in seconds. The precision depends on that of the C function by the same name.

### `ctime`(secs)

Convert a time expressed in seconds since the epoch to a string representing local time. `ctime(t)` is equivalent to `asctime(localtime(t))`.

### `daylight`

Nonzero if a DST timezone is defined.

### `gmtime`(secs)

Convert a time expressed in seconds since the epoch to a tuple of 9 integers, in UTC: year (e.g. 1993), month (1-12), day (1-31), hour (0-23), minute (0-59), second (0-59), weekday (0-6, monday is 0), julian day (1-366), dst flag (always zero). Fractions of a second are ignored. Note subtle differences with the C function of this name.

### `localtime`(secs)

Like `gmtime` but converts to local time. The dst flag is set to 1 when DST applies to the given time.

### `mktime`(tuple)

This is the inverse function of `localtime`. Its argument is the full 9-tuple (since the dst flag is needed). It returns an integer.

### `sleep`(secs)

Suspend execution for the given number of seconds. The argument may be a floating point number to indicate a more precise sleep time.

### `time`()

Return the time as a floating point number expressed in seconds since the epoch, in UTC. Note that even though the time is always returned as a floating point number, not all systems provide time with a better precision than 1 second.

### `timezone`

The offset of the local (non-DST) timezone, in seconds west of the 0th meridian (i.e. negative in most of Western Europe, positive in the US, zero in the UK).

### `tzname`

A tuple of two strings: the first is the name of the local non-DST timezone, the second is the name of the local DST timezone. If no DST timezone is defined, the second string should not be used.
# Built-in Types

The following sections describe the standard types that are built into the interpreter. These are the numeric types, sequence types, and several others, including types themselves. There is no explicit Boolean type; use integers instead.

Some operations are supported by several object types; in particular, all objects can be compared, tested for truth value, and converted to a string (with the `‘``…``‘` notation). The latter conversion is implicitly used when an object is written by the `print` statement.

## Truth Value Testing

Any object can be tested for truth value, for use in an `if` or `while` condition or as operand of the Boolean operations below. The following values are false:

- `None`

- zero of any numeric type, e.g., `0`, `0L`, `0.0`.

- any empty sequence, e.g., `’’`, `()`, `[]`.

- any empty mapping, e.g., `{}`.

*All* other values are true — so objects of many types are always true.

## Boolean Operations

These are the Boolean operations:

|             |                                     |       |
|:------------|:------------------------------------|:------|
| *x* or *y*  | if *x* is false, then *y*, else *x* | \(1\) |
| *x* and *y* | if *x* is false, then *x*, else *y* | \(1\) |
| not *x*     | if *x* is false, then `1`, else `0` |       |

Notes:

\(1\)  
These only evaluate their second argument if needed for their outcome.

## Comparisons

Comparison operations are supported by all objects:

|        |                         |       |
|:-------|:------------------------|:------|
| \<     | strictly less than      |       |
| \<=    | less than or equal      |       |
| \>     | strictly greater than   |       |
| \>=    | greater than or equal   |       |
| ==     | equal                   |       |
| \<\>   | not equal               | \(1\) |
| !=     | not equal               | \(1\) |
| is     | object identity         |       |
| is not | negated object identity |       |

Notes:

\(1\)  
`<>` and `!=` are alternate spellings for the same operator. (I couldn’t choose between ABC and C! :-)

Objects of different types, except different numeric types, never compare equal; such objects are ordered consistently but arbitrarily (so that sorting a heterogeneous array yields a consistent result). Furthermore, some types (e.g., windows) support only a degenerate notion of comparison where any two objects of that type are unequal. Again, such objects are ordered arbitrarily but consistently.

(Implementation note: objects of different types except numbers are ordered by their type names; objects of the same types that don’t support proper comparison are ordered by their address.)

Two more operations with the same syntactic priority, `in` and `not in`, are supported only by sequence types (below).

## Numeric Types

There are three numeric types: *plain integers*, *long integers*, and *floating point numbers*. Plain integers (also just called *integers*) are implemented using `long` in C, which gives them at least 32 bits of precision. Long integers have unlimited precision. Floating point numbers are implemented using `double` in C. All bets on their precision are off unless you happen to know the machine you are working with.

Numbers are created by numeric literals or as the result of built-in functions and operators. Unadorned integer literals (including hex and octal numbers) yield plain integers. Integer literals with an `L` or `l` suffix yield long integers (`L` is preferred because `1l` looks too much like eleven!). Numeric literals containing a decimal point or an exponent sign yield floating point numbers.

Python fully supports mixed arithmetic: when a binary arithmetic operator has operands of different numeric types, the operand with the “smaller” type is converted to that of the other, where plain integer is smaller than long integer is smaller than floating point. Comparisons between numbers of mixed type use the same rule. [^1] The functions `int()`, `long()` and `float()` can be used to coerce numbers to a specific type.

All numeric types support the following operations:

|                  |                                                   |       |
|:-----------------|:--------------------------------------------------|:------|
| abs(*x*)         | absolute value of *x*                             |       |
| int(*x*)         | *x* converted to integer                          | \(1\) |
| long(*x*)        | *x* converted to long integer                     | \(1\) |
| float(*x*)       | *x* converted to floating point                   |       |
| \-*x*            | *x* negated                                       |       |
| \+*x*            | *x* unchanged                                     |       |
| *x* + *y*        | sum of *x* and *y*                                |       |
| *x* - *y*        | difference of *x* and *y*                         |       |
| *x* * *y*       | product of *x* and *y*                            |       |
| *x* / *y*        | quotient of *x* and *y*                           | \(2\) |
| *x* % *y*        | remainder of *`x`*` / `*`y`*                      |       |
| divmod(*x*, *y*) | the pair `(`*`x`*` / `*`y`*`, `*`x`*` % `*`y`*`)` | \(3\) |
| pow(*x*, *y*)    | *x* to the power *y*                              |       |

Notes:

\(1\)  
Conversion from floating point to (long or plain) integer may round or

truncate as in C; see functions `floor` and `ceil` in module `math` for well-defined conversions.

\(2\)  
For (plain or long) integer division, the result is an integer; it always truncates towards zero.

\(3\)  
See the section on built-in functions for an exact definition.

### Bit-string Operations on Integer Types.

Plain and long integer types support additional operations that make sense only for bit-strings. Negative numbers are treated as their 2’s complement value:

|              |                                       |     |
|:-------------|:--------------------------------------|:----|
| *x*          | the bits of *x* inverted              |     |
| *x* ^ *y*    | bitwise *exclusive or* of *x* and *y* |     |
| *x* & *y*    | bitwise *and* of *x* and *y*          |     |
| *x* \| *y*   | bitwise *or* of *x* and *y*           |     |
| *x* \<\< *n* | *x* shifted left by *n* bits          |     |
| *x* \>\> *n* | *x* shifted right by *n* bits         |     |

## Sequence Types

There are three sequence types: strings, lists and tuples. Strings literals are written in single quotes: `’xyzzy’`. Lists are constructed with square brackets, separating items with commas: `[a, b, c]`. Tuples are constructed by the comma operator (not within square brackets), with or without enclosing parentheses, but an empty tuple must have the enclosing parentheses, e.g., `a, b, c` or `()`. A single item tuple must have a trailing comma, e.g., `(d,)`.

Sequence types support the following operations (*s* and *t* are sequences of the same type; *n*, *i* and *j* are integers):

|  |  |  |
|:---|:---|:---|
| len(*s*) | length of *s* |  |
| min(*s*) | smallest item of *s* |  |
| max(*s*) | largest item of *s* |  |
| *x* in *s* | `1` if an item of *s* is equal to *x*, else `0` |  |
| *x* not in *s* | `0` if an item of *s* is equal to *x*, else `1` |  |
| *s* + *t* | the concatenation of *s* and *t* |  |
| *s* * *n*, *n* * *s* | *n* copies of *s* concatenated |  |
| *s*[*i*] | *i*’th item of *s*, origin 0 | \(1\) |
| *s*[*i*:*j*] | slice of *s* from *i* to *j* | (1), (2) |

Notes:

\(1\)  
If *i* or *j* is negative, the index is relative to the end of the string, i.e., `len(`*`s`*`) + `*`i`* or `len(`*`s`*`) + `*`j`* is substituted. But note that `-0` is still `0`.

\(2\)  
The slice of *s* from *i* to *j* is defined as the sequence of items with index *k* such that *`i`*` <= `*`k`*` < `*`j`*. If *i* or *j* is greater than `len(`*`s`*`)`, use `len(`*`s`*`)`. If *i* is omitted, use `0`. If *j* is omitted, use `len(`*`s`*`)`. If *i* is greater than or equal to *j*, the slice is empty.

### More String Operations.

String objects have one unique built-in operation: the `%` operator (modulo) with a string left argument interprets this string as a C sprintf format string to be applied to the right argument, and returns the string resulting from this formatting operation.

The right argument should be a tuple with one item for each argument required by the format string; if the string requires a single argument, the right argument may also be a single non-tuple object. [^2] The following format characters are understood: %, c, s, i, d, u, o, x, X, e, E, f, g, G. Width and precision may be a * to specify that an integer argument specifies the actual width or precision. The flag characters -, +, blank, \# and 0 are understood. The size specifiers h, l or L may be present but are ignored. The `%s` conversion takes any Python object and converts it to a string using `str()` before formatting it. The ANSI features `%p` and `%n` are not supported. Since Python strings have an explicit length, `%s` conversions don’t assume that `’`\
`0’` is the end of the string.

For safety reasons, floating point precisions are clipped to 50; `%f` conversions for numbers whose absolute value is over 1e25 are replaced by `%g` conversions. [^3] All other errors raise exceptions.

If the right argument is a dictionary (or any kind of mapping), then the formats in the string must have a parenthesized key into that dictionary inserted immediately after the `%` character, and each format formats the corresponding entry from the mapping. E.g.

        >>> count = 2
        >>> language = 'Python'
        >>> print '%(language)s has %(count)03d quote types.' % vars()
        Python has 002 quote types.
        >>> 

In this case no * specifiers may occur in a format.

Additional string operations are defined in standard module `string` and in built-in module `regex`.

### Mutable Sequence Types.

List objects support additional operations that allow in-place modification of the object. These operations would be supported by other mutable sequence types (when added to the language) as well. Strings and tuples are immutable sequence types and such objects cannot be modified once created. The following operations are defined on mutable sequence types (where *x* is an arbitrary object):

|  |  |  |
|:---|:---|:---|
| *s*[*i*] = *x* | item *i* of *s* is replaced by *x* |  |
| *s*[*i*:*j*] = *t* | slice of *s* from *i* to *j* is replaced by *t* |  |
| del *s*[*i*:*j*] | same as *`s`*`[`*`i`*`:`*`j`*`] = []` |  |
| *s*.append(*x*) | same as *`s`*`[len(`*`s`*`):len(`*`s`*`)] = [`*`x`*`]` |  |
| *s*.count(*x*) | return number of *i*’s for which *`s`*`[`*`i`*`] == `*`x`* |  |
| *s*.index(*x*) | return smallest *i* such that *`s`*`[`*`i`*`] == `*`x`* | \(1\) |
| *s*.insert(*i*, *x*) | same as *`s`*`[`*`i`*`:`*`i`*`] = [`*`x`*`]` |  |
| *s*.remove(*x*) | same as `del `*`s`*`[`*`s`*`.index(`*`x`*`)]` | \(1\) |
| *s*.reverse() | reverses the items of *s* in place |  |
| *s*.sort() | permutes the items of *s* to satisfy *`s`*`[`*`i`*`] <= `*`s`*`[`*`j`*`]`, for *`i`*` < `*`j`* | \(2\) |

Notes:

\(1\)  
Raises an exception when *x* is not found in *s*.

\(2\)  
The `sort()` method takes an optional argument specifying a comparison function of two arguments (list items) which should return `-1`, `0` or `1` depending on whether the first argument is considered smaller than, equal to, or larger than the second argument. Note that this slows the sorting process down considerably; e.g. to sort an array in reverse order it is much faster to use calls to `sort()` and `reverse()` than to use `sort()` with a comparison function that reverses the ordering of the elements.

## Mapping Types

A *mapping* object maps values of one type (the key type) to arbitrary objects. Mappings are mutable objects. There is currently only one mapping type, the *dictionary*. A dictionary’s keys are almost arbitrary values. The only types of values not acceptable as keys are values containing lists or dictionaries or other mutable types that are compared by value rather than by object identity. Numeric types used for keys obey the normal rules for numeric comparison: if two numbers compare equal (e.g. 1 and 1.0) then they can be used interchangeably to index the same dictionary entry.

Dictionaries are created by placing a comma-separated list of *`key`*`: `*`value`* pairs within braces, for example: `{’jack’: 4098, ’sjoerd: 4127}` or `{4098: ’jack’, 4127: ’sjoerd}`.

The following operations are defined on mappings (where *a* is a mapping, *k* is a key and *x* is an arbitrary object):

|                  |                                           |       |
|:-----------------|:------------------------------------------|:------|
| len(*a*)         | the number of items in *a*                |       |
| *a*[*k*]       | the item of *a* with key *k*              | \(1\) |
| *a*[*k*] = *x* | set *`a`*`[`*`k`*`]` to *x*               |       |
| del *a*[*k*]   | remove *`a`*`[`*`k`*`]` from *a*          | \(1\) |
| *a*.items()      | a copy of *a*’s list of (key, item) pairs | \(2\) |
| *a*.keys()       | a copy of *a*’s list of keys              | \(2\) |
| *a*.values()     | a copy of *a*’s list of values            | \(2\) |
| *a*.has_key(*k*) | `1` if *a* has a key *k*, else `0`        |       |

Notes:

\(1\)  
Raises an exception if *k* is not in the map.

\(2\)  
Keys and values are listed in random order, but at any moment the ordering of the `keys()`, `values()` and `items()` lists is the consistent with each other.

## Other Built-in Types

The interpreter supports several other kinds of objects. Most of these support only one or two operations.

### Modules.

The only special operation on a module is attribute access: *`m`*`.`*`name`*, where *m* is a module and *name* accesses a name defined in *m*’s symbol table. Module attributes can be assigned to. (Note that the `import` statement is not, strictly spoken, an operation on a module object; `import `*`foo`* does not require a module object named *foo* to exist, rather it requires an (external) *definition* for a module named *foo* somewhere.)

A special member of every module is `__dict__`. This is the dictionary containing the module’s symbol table. Modifying this dictionary will actually change the module’s symbol table, but direct assignment to the `__dict__` attribute is not possible (i.e., you can write *`m`*`.__dict__[’a’] = 1`, which defines *`m`*`.a` to be `1`, but you can’t write *`m`*`.__dict__ = {}`.

Modules are written like this: `<module ’sys’>`.

### Classes and Class Instances.

(See the Python Reference Manual for these.)

### Functions.

Function objects are created by function definitions. The only operation on a function object is to call it: *`func`*`(`*`argument-list`*`)`.

There are really two flavors of function objects: built-in functions and user-defined functions. Both support the same operation (to call the function), but the implementation is different, hence the different object types.

The implementation adds two special read-only attributes: *`f`*`.func_code` is a function’s *code object* (see below) and *`f`*`.func_globals` is the dictionary used as the function’s global name space (this is the same as *`m`*`.__dict__` where *m* is the module in which the function *f* was defined).

### Methods.

Methods are functions that are called using the attribute notation. There are two flavors: built-in methods (such as `append()` on lists) and class instance methods. Built-in methods are described with the types that support them.

The implementation adds two special read-only attributes to class instance methods: *`m`*`.im_self` is the object whose method this is, and *`m`*`.im_func` is the function implementing the method. Calling *`m`*`(`*`arg-1`*`, `*`arg-2`*`, ``…``, `*`arg-n`*`)` is completely equivalent to calling *`m`*`.im_func(`*`m`*`.im_self, `*`arg-1`*`, `*`arg-2`*`, `` …``, `*`arg-n`*`)`.

(See the Python Reference Manual for more info.)

### Type Objects.

Type objects represent the various object types. An object’s type is

accessed by the built-in function `type()`. There are no special operations on types.

Types are written like this: `<type ’int’>`.

### The Null Object.

This object is returned by functions that don’t explicitly return a value. It supports no special operations. There is exactly one null object, named `None` (a built-in name).

It is written as `None`.

### File Objects.

File objects are implemented using C’s `stdio` package and can be

created with the built-in function `open()` described under Built-in Functions below.

When a file operation fails for an I/O-related reason, the exception `IOError` is raised. This includes situations where the operation is not defined for some reason, like `seek()` on a tty device or writing a file opened for reading.

Files have the following methods:

### `close`()

Close the file. A closed file cannot be read or written anymore.

### `flush`()

Flush the internal buffer, like `stdio`’s `fflush()`.

### `isatty`()

Return `1` if the file is connected to a tty(-like) device, else `0`.

### `read`(size)

Read at most *size* bytes from the file (less if the read hits EOF or no more data is immediately available on a pipe, tty or similar device). If the *size* argument is omitted, read all data until EOF is reached. The bytes are returned as a string object. An empty string is returned when EOF is encountered immediately. (For certain files, like ttys, it makes sense to continue reading after an EOF is hit.)

### `readline`()

Read one entire line from the file. A trailing newline character is kept in the string (but may be absent when a file ends with an incomplete line). An empty string is returned when EOF is hit immediately. Note: unlike `stdio`’s `fgets()`, the returned string contains null characters (`’’`) if they occurred in the input.

### `readlines`()

Read until EOF using `readline()` and return a list containing the lines thus read.

### `seek`(offset  whence)

Set the file’s current position, like `stdio`’s `fseek()`. The *whence* argument is optional and defaults to `0` (absolute file positioning); other values are `1` (seek relative to the current position) and `2` (seek relative to the file’s end). There is no return value.

### `tell`()

Return the file’s current position, like `stdio`’s `ftell()`.

### `write`(str)

Write a string to the file. There is no return value.

### `writelines`(list)

Write a list of strings to the file. There is no return value. (The name is intended to match `readlines`; `writelines` does not add line separators.)

### Internal Objects.

(See the Python Reference Manual for these.)

## Special Attributes

The implementation adds a few special read-only attributes to several object types, where they are relevant:

- *`x`*`.__dict__` is a dictionary of some sort used to store an object’s (writable) attributes;

- *`x`*`.__methods__` lists the methods of many built-in object types, e.g., `[].__methods__` is

  `[’append’, ’count’, ’index’, ’insert’, ’remove’, ’reverse’, ’sort’]`;

- *`x`*`.__members__` lists data attributes;

- *`x`*`.__class__` is the class to which a class instance belongs;

- *`x`*`.__bases__` is the tuple of base classes of a class object.

[^1]: As a consequence, the list `[1, 2]` is considered equal to `[1.0, 2.0]`, and similar for tuples.

[^2]: A tuple object in this case should be a singleton.

[^3]: These numbers are fairly arbitrary. They are intended to avoid printing endless strings of meaningless digits without hampering correct use and without having to know the exact precision of floating point values on a particular machine.
# UNIX ONLY

The modules described in this chapter provide interfaces to features that are unique to the UNIX operating system, or in some cases to some or many variants of it.
# Standard Module `whrandom`

This module implements a Wichmann-Hill pseudo-random number generator. It defines the following functions:

### `random`()

Returns the next random floating point number in the range [0.0 ... 1.0).

### `seed`(x  y  z)

Initializes the random number generator from the integers *x*, *y* and *z*. When the module is first imported, the random number is initialized using values derived from the current time.


{{< python-copyright version="1.1" >}}
