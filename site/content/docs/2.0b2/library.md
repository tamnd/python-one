---
title: "Library Reference"
weight: 20
---

# `aifc` — Read and write AIFF and AIFC files

*Read and write audio files in AIFF or AIFC format.*\
This module provides support for reading and writing AIFF and AIFF-C files. AIFF is Audio Interchange File Format, a format for storing digital audio samples in a file. AIFF-C is a newer version of the format that includes the ability to compress the audio data. **Caveat:** Some operations may only work under IRIX; these will raise `ImportError` when attempting to import the `cl` module, which is only available on IRIX.

Audio files have a number of parameters that describe the audio data. The sampling rate or frame rate is the number of times per second the sound is sampled. The number of channels indicate if the audio is mono, stereo, or quadro. Each frame consists of one sample per channel. The sample size is the size in bytes of each sample. Thus a frame consists of *nchannels*\**samplesize* bytes, and a second’s worth of audio consists of *nchannels*\**samplesize*\**framerate* bytes.

For example, CD quality audio has a sample size of two bytes (16 bits), uses two channels (stereo) and has a frame rate of 44,100 frames/second. This gives a frame size of 4 bytes (2\*2), and a second’s worth occupies 2\*2\*44100 bytes, i.e. 176,400 bytes.

Module `aifc` defines the following function:

<div class="funcdesc">

openfile Open an AIFF or AIFF-C file and return an object instance with methods that are described below. The argument *file* is either a string naming a file or a file object. *mode* must be `’r’` or `’rb’` when the file must be opened for reading, or `’w’` or `’wb’` when the file must be opened for writing. If omitted, *`file`*`.mode` is used if it exists, otherwise `’rb’` is used. When used for writing, the file object should be seekable, unless you know ahead of time how many samples you are going to write in total and use `writeframesraw()` and `setnframes()`.

</div>

Objects returned by `open()` when a file is opened for reading have the following methods:

<div class="methoddesc">

getnchannels Return the number of audio channels (1 for mono, 2 for stereo).

</div>

<div class="methoddesc">

getsampwidth Return the size in bytes of individual samples.

</div>

<div class="methoddesc">

getframerate Return the sampling rate (number of audio frames per second).

</div>

<div class="methoddesc">

getnframes Return the number of audio frames in the file.

</div>

<div class="methoddesc">

getcomptype Return a four-character string describing the type of compression used in the audio file. For AIFF files, the returned value is `’NONE’`.

</div>

<div class="methoddesc">

getcompname Return a human-readable description of the type of compression used in the audio file. For AIFF files, the returned value is `’not compressed’`.

</div>

<div class="methoddesc">

getparams Return a tuple consisting of all of the above values in the above order.

</div>

<div class="methoddesc">

getmarkers Return a list of markers in the audio file. A marker consists of a tuple of three elements. The first is the mark ID (an integer), the second is the mark position in frames from the beginning of the data (an integer), the third is the name of the mark (a string).

</div>

<div class="methoddesc">

getmarkid Return the tuple as described in `getmarkers()` for the mark with the given *id*.

</div>

<div class="methoddesc">

readframesnframes Read and return the next *nframes* frames from the audio file. The returned data is a string containing for each frame the uncompressed samples of all channels.

</div>

<div class="methoddesc">

rewind Rewind the read pointer. The next `readframes()` will start from the beginning.

</div>

<div class="methoddesc">

setpospos Seek to the specified frame number.

</div>

<div class="methoddesc">

tell Return the current frame number.

</div>

<div class="methoddesc">

close Close the AIFF file. After calling this method, the object can no longer be used.

</div>

Objects returned by `open()` when a file is opened for writing have all the above methods, except for `readframes()` and `setpos()`. In addition the following methods exist. The `get*()` methods can only be called after the corresponding `set*()` methods have been called. Before the first `writeframes()` or `writeframesraw()`, all parameters except for the number of frames must be filled in.

<div class="methoddesc">

aiff Create an AIFF file. The default is that an AIFF-C file is created, unless the name of the file ends in `’.aiff’` in which case the default is an AIFF file.

</div>

<div class="methoddesc">

aifc Create an AIFF-C file. The default is that an AIFF-C file is created, unless the name of the file ends in `’.aiff’` in which case the default is an AIFF file.

</div>

<div class="methoddesc">

setnchannelsnchannels Specify the number of channels in the audio file.

</div>

<div class="methoddesc">

setsampwidthwidth Specify the size in bytes of audio samples.

</div>

<div class="methoddesc">

setframeraterate Specify the sampling frequency in frames per second.

</div>

<div class="methoddesc">

setnframesnframes Specify the number of frames that are to be written to the audio file. If this parameter is not set, or not set correctly, the file needs to support seeking.

</div>

<div class="methoddesc">

setcomptypetype, name Specify the compression type. If not specified, the audio data will not be compressed. In AIFF files, compression is not possible. The name parameter should be a human-readable description of the compression type, the type parameter should be a four-character string. Currently the following compression types are supported: NONE, ULAW, ALAW, G722.

</div>

<div class="methoddesc">

setparamsnchannels, sampwidth, framerate, comptype, compname Set all the above parameters at once. The argument is a tuple consisting of the various parameters. This means that it is possible to use the result of a `getparams()` call as argument to `setparams()`.

</div>

<div class="methoddesc">

setmarkid, pos, name Add a mark with the given id (larger than 0), and the given name at the given position. This method can be called at any time before `close()`.

</div>

<div class="methoddesc">

tell Return the current write position in the output file. Useful in combination with `setmark()`.

</div>

<div class="methoddesc">

writeframesdata Write data to the output file. This method can only be called after the audio file parameters have been set.

</div>

<div class="methoddesc">

writeframesrawdata Like `writeframes()`, except that the header of the audio file is not updated.

</div>

<div class="methoddesc">

close Close the AIFF file. The header of the file is updated to reflect the actual size of the audio data. After calling this method, the object can no longer be used.

</div>
# `al` — Audio functions on the SGI

*Audio functions on the SGI.*\
This module provides access to the audio facilities of the SGI Indy and Indigo workstations. See section 3A of the IRIX man pages for details. You’ll need to read those man pages to understand what these functions do! Some of the functions are not available in IRIX releases before 4.0.5. Again, see the manual to check whether a specific function is available on your platform.

All functions and methods defined in this module are equivalent to the C functions with `AL` prefixed to their name.

Symbolic constants from the C header file `<audio.h>` are defined in the standard module `AL`, see below.

**Warning:** the current version of the audio library may dump core when bad argument values are passed rather than returning an error status. Unfortunately, since the precise circumstances under which this may happen are undocumented and hard to check, the Python interface can provide no protection against this kind of problems. (One example is specifying an excessive queue size — there is no documented upper limit.)

The module defines the following functions:

<div class="funcdesc">

openportname, direction The name and direction arguments are strings. The optional *config* argument is a configuration object as returned by `newconfig()`. The return value is an *audio port object*; methods of audio port objects are described below.

</div>

<div class="funcdesc">

newconfig The return value is a new *audio configuration object*; methods of audio configuration objects are described below.

</div>

<div class="funcdesc">

queryparamsdevice The device argument is an integer. The return value is a list of integers containing the data returned by .

</div>

<div class="funcdesc">

getparamsdevice, list The *device* argument is an integer. The list argument is a list such as returned by `queryparams()`; it is modified in place (!).

</div>

<div class="funcdesc">

setparamsdevice, list The *device* argument is an integer. The *list* argument is a list such as returned by `queryparams()`.

</div>

## Configuration Objects <span id="al-config-objects" label="al-config-objects"></span>

Configuration objects (returned by `newconfig()` have the following methods:

<div class="methoddesc">

getqueuesize Return the queue size.

</div>

<div class="methoddesc">

setqueuesizesize Set the queue size.

</div>

<div class="methoddesc">

getwidth Get the sample width.

</div>

<div class="methoddesc">

setwidthwidth Set the sample width.

</div>

<div class="methoddesc">

getchannels Get the channel count.

</div>

<div class="methoddesc">

setchannelsnchannels Set the channel count.

</div>

<div class="methoddesc">

getsampfmt Get the sample format.

</div>

<div class="methoddesc">

setsampfmtsampfmt Set the sample format.

</div>

<div class="methoddesc">

getfloatmax Get the maximum value for floating sample formats.

</div>

<div class="methoddesc">

setfloatmaxfloatmax Set the maximum value for floating sample formats.

</div>

## Port Objects <span id="al-port-objects" label="al-port-objects"></span>

Port objects, as returned by `openport()`, have the following methods:

<div class="methoddesc">

closeport Close the port.

</div>

<div class="methoddesc">

getfd Return the file descriptor as an int.

</div>

<div class="methoddesc">

getfilled Return the number of filled samples.

</div>

<div class="methoddesc">

getfillable Return the number of fillable samples.

</div>

<div class="methoddesc">

readsampsnsamples Read a number of samples from the queue, blocking if necessary. Return the data as a string containing the raw data, (e.g., 2 bytes per sample in big-endian byte order (high byte, low byte) if you have set the sample width to 2 bytes).

</div>

<div class="methoddesc">

writesampssamples Write samples into the queue, blocking if necessary. The samples are encoded as described for the `readsamps()` return value.

</div>

<div class="methoddesc">

getfillpoint Return the ‘fill point’.

</div>

<div class="methoddesc">

setfillpointfillpoint Set the ‘fill point’.

</div>

<div class="methoddesc">

getconfig Return a configuration object containing the current configuration of the port.

</div>

<div class="methoddesc">

setconfigconfig Set the configuration from the argument, a configuration object.

</div>

<div class="methoddesc">

getstatuslist Get status information on last error.

</div>

# `AL` — Constants used with the `al` module

*Constants used with the `al` module.*\
This module defines symbolic constants needed to use the built-in module `al` (see above); they are equivalent to those defined in the C header file `<audio.h>` except that the name prefix `AL_` is omitted. Read the module source for a complete list of the defined names. Suggested use:

    import al
    from AL import *
# Generic Operating System Services <span id="allos" label="allos"></span>

The modules described in this chapter provide interfaces to operating system features that are available on (almost) all operating systems, such as files and a clock. The interfaces are generally modeled after the Unix or C interfaces, but they are available on most other systems as well. Here’s an overview:
# Amoeba Specific Services

## `amoeba` — Amoeba system support

*Functions for the Amoeba operating system.*\
This module provides some object types and operations useful for Amoeba applications. It is only available on systems that support Amoeba operations. RPC errors and other Amoeba errors are reported as the exception `amoeba.error = ’amoeba.error’`.

The module `amoeba` defines the following items:

<div class="funcdesc">

name_appendpath, cap Stores a capability in the Amoeba directory tree. Arguments are the pathname (a string) and the capability (a capability object as returned by `name_lookup()`).

</div>

<div class="funcdesc">

name_deletepath Deletes a capability from the Amoeba directory tree. Argument is the pathname.

</div>

<div class="funcdesc">

name_lookuppath Looks up a capability. Argument is the pathname. Returns a *capability* object, to which various interesting operations apply, described below.

</div>

<div class="funcdesc">

name_replacepath, cap Replaces a capability in the Amoeba directory tree. Arguments are the pathname and the new capability. (This differs from `name_append()` in the behavior when the pathname already exists: `name_append()` finds this an error while `name_replace()` allows it, as its name suggests.)

</div>

<div class="datadesc">

capv A table representing the capability environment at the time the interpreter was started. (Alas, modifying this table does not affect the capability environment of the interpreter.) For example, `amoeba.capv[’ROOT’]` is the capability of your root directory, similar to `getcap("ROOT")` in C.

</div>

<div class="excdesc">

error The exception raised when an Amoeba function returns an error. The value accompanying this exception is a pair containing the numeric error code and the corresponding string, as returned by the C function .

</div>

<div class="funcdesc">

timeoutmsecs Sets the transaction timeout, in milliseconds. Returns the previous timeout. Initially, the timeout is set to 2 seconds by the Python interpreter.

</div>

### Capability Operations

Capabilities are written in a convenient format, also used by the Amoeba utilities *c2a*(U) and *a2c*(U). For example:

    >>> amoeba.name_lookup('/profile/cap')
    aa:1c:95:52:6a:fa/14(ff)/8e:ba:5b:8:11:1a
    >>> 

The following methods are defined for capability objects.

<div class="funcdesc">

dir_list Returns a list of the names of the entries in an Amoeba directory.

</div>

<div class="funcdesc">

b_readoffset, maxsize Reads (at most) *maxsize* bytes from a bullet file at offset *offset.* The data is returned as a string. EOF is reported as an empty string.

</div>

<div class="funcdesc">

b_size Returns the size of a bullet file.

</div>

<div class="funcdesc">

dir_append Like the corresponding `name_`\* functions, but with a path relative to the capability. (For paths beginning with a slash the capability is ignored, since this is the defined semantics for Amoeba.)

</div>

<div class="funcdesc">

std_info Returns the standard info string of the object.

</div>

<div class="funcdesc">

tod_gettime Returns the time (in seconds since the Epoch, in UCT, as for ) from a time server.

</div>

<div class="funcdesc">

tod_settimet Sets the time kept by a time server.

</div>
# `curses.ascii` — Utilities for ASCII characters

*Constants and set-membership functions for characters.*\
*New in version 1.6.*

The `curses.ascii` module supplies name constants for characters and functions to test membership in various character classes. The constants supplied are names for control characters as follows:

|                    |                                           |
|:-------------------|:------------------------------------------|
| NameMeaning NUL    |                                           |
| SOH                | Start of heading, console interrupt       |
| STX                | Start of text                             |
| ETX                | End of text                               |
| EOT                | End of transmission                       |
| ENQ                | Enquiry, goes with                        |
| flow control       | Acknowledgement                           |
| BEL                | Bell                                      |
| BS                 | Backspace                                 |
| TAB                | Tab                                       |
| HT                 | Alias for                                 |
| : “Horizontal tab” | Line feed                                 |
| NL                 | Alias for                                 |
| : “New line”       | Vertical tab                              |
| FF                 | Form feed                                 |
| CR                 | Carriage return                           |
| SO                 | Shift-out, begin alternate character set  |
| SI                 | Shift-in, resume default character set    |
| DLE                | Data-link escape                          |
| DC1                | XON, for flow control                     |
| DC2                | Device control 2, block-mode flow control |
| DC3                | XOFF, for flow control                    |
| DC4                | Device control 4                          |
| NAK                | Negative acknowledgement                  |
| SYN                | Synchronous idle                          |
| ETB                | End transmission block                    |
| CAN                | Cancel                                    |
| EM                 | End of medium                             |
| SUB                | Substitute                                |
| ESC                | Escape                                    |
| FS                 | File separator                            |
| GS                 | Group separator                           |
| RS                 | Record separator, block-mode terminator   |
| US                 | Unit separator                            |
| SP                 | Space                                     |
| DEL                | Delete                                    |
|                    |                                           |

Note that many of these have little practical use in modern usage.

The module supplies the following functions, patterned on those in the standard C library:

<div class="funcdesc">

isalnumc Checks for an alphanumeric character; it is equivalent to `isalpha(`*`c`*`) or isdigit(`*`c`*`)`.

</div>

<div class="funcdesc">

isalphac Checks for an alphabetic character; it is equivalent to `isupper(`*`c`*`) or islower(`*`c`*`)`.

</div>

<div class="funcdesc">

isasciic Checks for a character value that fits in the 7-bit set.

</div>

<div class="funcdesc">

isblankc Checks for an whitespace character.

</div>

<div class="funcdesc">

iscntrlc Checks for an control character (in the range 0x00 to 0x1f).

</div>

<div class="funcdesc">

isdigitc Checks for an decimal digit, through . This is equivalent to *`c`*` in string.digits`.

</div>

<div class="funcdesc">

isgraphc Checks for any printable character except space.

</div>

<div class="funcdesc">

islowerc Checks for an lower-case character.

</div>

<div class="funcdesc">

isprintc Checks for any printable character including space.

</div>

<div class="funcdesc">

ispunctc Checks for any printable character which is not a space or an alphanumeric character.

</div>

<div class="funcdesc">

isspacec Checks for white-space characters; space, tab, line feed, carriage return, form feed, horizontal tab, vertical tab.

</div>

<div class="funcdesc">

isupperc Checks for an uppercase letter.

</div>

<div class="funcdesc">

isxdigitc Checks for an hexadecimal digit. This is equivalent to *`c`*` in string.hexdigits`.

</div>

<div class="funcdesc">

isctrlc Checks for an control character (ordinal values 0 to 31).

</div>

<div class="funcdesc">

ismetac Checks for a non- character (ordinal values 0x80 and above).

</div>

These functions accept either integers or strings; when the argument is a string, it is first converted using the built-in function `ord()`.

Note that all these functions check ordinal bit values derived from the first character of the string you pass in; they do not actually know anything about the host machine’s character encoding. For functions that know about the character encoding (and handle internationalization properly) see the `string` module.

The following two functions take either a single-character string or integer byte value; they return a value of the same type.

<div class="funcdesc">

asciic Return the ASCII value corresponding to the low 7 bits of *c*.

</div>

<div class="funcdesc">

ctrlc Return the control character corresponding to the given character (the character bit value is bitwise-anded with 0x1f).

</div>

<div class="funcdesc">

altc Return the 8-bit character corresponding to the given ASCII character (the character bit value is bitwise-ored with 0x80).

</div>

The following function takes either a single-character string or integer value; it returns a string.

<div class="funcdesc">

unctrlc Return a string representation of the character *c*. If *c* is printable, this string is the character itself. If the character is a control character (0x00-0x1f) the string consists of a caret () followed by the corresponding uppercase letter. If the character is an delete (0x7f) the string is `’^?’`. If the character has its meta bit (0x80) set, the meta bit is stripped, the preceding rules applied, and prepended to the result.

</div>

<div class="datadesc">

controlnames A 33-element string array that contains the mnemonics for the thirty-two control characters from 0 (NUL) to 0x1f (US), in order, plus the mnemonic `SP` for the space character.

</div>
# `asyncore` — Asynchronous socket handler

*A base class for developing asynchronous socket handling services.*\
This module provides the basic infrastructure for writing asynchronous socket service clients and servers.

There are only two ways to have a program on a single processor do “more than one thing at a time.” Multi-threaded programming is the simplest and most popular way to do it, but there is another very different technique, that lets you have nearly all the advantages of multi-threading, without actually using multiple threads. It’s really only practical if your program is largely I/O bound. If your program is CPU bound, then pre-emptive scheduled threads are probably what you really need. Network servers are rarely CPU-bound, however.

If your operating system supports the system call in its I/O library (and nearly all do), then you can use it to juggle multiple communication channels at once; doing other work while your I/O is taking place in the “background.” Although this strategy can seem strange and complex, especially at first, it is in many ways easier to understand and control than multi-threaded programming. The module documented here solves many of the difficult problems for you, making the task of building sophisticated high-performance network servers and clients a snap.

<div class="classdesc">

dispatcher The first class we will introduce is the `dispatcher` class. This is a thin wrapper around a low-level socket object. To make it more useful, it has a few methods for event-handling on it. Otherwise, it can be treated as a normal non-blocking socket object.

The direct interface between the select loop and the socket object are the `handle_read_event()` and `handle_write_event()` methods. These are called whenever an object ‘fires’ that event.

The firing of these low-level events can tell us whether certain higher-level events have taken place, depending on the timing and the state of the connection. For example, if we have asked for a socket to connect to another host, we know that the connection has been made when the socket fires a write event (at this point you know that you may write to it with the expectation of success). The implied higher-level events are:

|  |  |
|:---|:---|
| EventDescription handle_connect() | Implied by a write event |
| handle_close() | Implied by a read event with no data available |
| handle_accept() | Implied by a read event on a listening socket |
|  |  |

</div>

This set of user-level events is larger than the basics. The full set of methods that can be overridden in your subclass are:

<div class="methoddesc">

handle_read Called when there is new data to be read from a socket.

</div>

<div class="methoddesc">

handle_write Called when there is an attempt to write data to the object. Often this method will implement the necessary buffering for performance. For example:

    def handle_write(self):
        sent = self.send(self.buffer)
        self.buffer = self.buffer[sent:]

</div>

<div class="methoddesc">

handle_expt Called when there is out of band (OOB) data for a socket connection. This will almost never happen, as OOB is tenuously supported and rarely used.

</div>

<div class="methoddesc">

handle_connect Called when the socket actually makes a connection. This might be used to send a “welcome” banner, or something similar.

</div>

<div class="methoddesc">

handle_close Called when the socket is closed.

</div>

<div class="methoddesc">

handle_accept Called on listening sockets when they actually accept a new connection.

</div>

<div class="methoddesc">

readable Each time through the `select()` loop, the set of sockets is scanned, and this method is called to see if there is any interest in reading. The default method simply returns `1`, indicating that by default, all channels will be interested.

</div>

<div class="methoddesc">

writeable Each time through the `select()` loop, the set of sockets is scanned, and this method is called to see if there is any interest in writing. The default method simply returns `1`, indicating that by default, all channels will be interested.

</div>

In addition, there are the basic methods needed to construct and manipulate “channels,” which are what we will call the socket connections in this context. Note that most of these are nearly identical to their socket partners.

<div class="methoddesc">

create_socketfamily, type This is identical to the creation of a normal socket, and will use the same options for creation. Refer to the `socket` documentation for information on creating sockets.

</div>

<div class="methoddesc">

connectaddress As with the normal socket object, *address* is a tuple with the first element the host to connect to, and the second the port.

</div>

<div class="methoddesc">

senddata Send *data* out the socket.

</div>

<div class="methoddesc">

recvbuffer_size Read at most *buffer_size* bytes from the socket.

</div>

<div class="methoddesc">

listen Listen for connections made to the socket. The *backlog* argument specifies the maximum number of queued connections and should be at least 1; the maximum value is system-dependent (usually 5).

</div>

<div class="methoddesc">

bindaddress Bind the socket to *address*. The socket must not already be bound. (The format of *address* depends on the address family — see above.)

</div>

<div class="methoddesc">

accept Accept a connection. The socket must be bound to an address and listening for connections. The return value is a pair `(`*`conn`*`, `*`address`*`)` where *conn* is a *new* socket object usable to send and receive data on the connection, and *address* is the address bound to the socket on the other end of the connection.

</div>

<div class="methoddesc">

close Close the socket. All future operations on the socket object will fail. The remote end will receive no more data (after queued data is flushed). Sockets are automatically closed when they are garbage-collected.

</div>

## Example basic HTTP client <span id="asyncore-example" label="asyncore-example"></span>

As a basic example, below is a very basic HTTP client that uses the `dispatcher` class to implement its socket handling:

    class http_client(asyncore.dispatcher):
        def __init__(self, host,path):
            asyncore.dispatcher.__init__(self)
            self.path = path
            self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connect( (host, 80) )
            self.buffer = 'GET %s HTTP/1.0\r\b\r\n' % self.path
            
        def handle_connect(self):
            pass
            
        def handle_read(self):
            data = self.recv(8192)
            print data
            
        def writeable(self):
            return (len(self.buffer) > 0)
        
        def handle_write(self):
            sent = self.send(self.buffer)
            self.buffer = self.buffer[sent:]
# `audioop` — Manipulate raw audio data

*Manipulate raw audio data.*\
The `audioop` module contains some useful operations on sound fragments. It operates on sound fragments consisting of signed integer samples 8, 16 or 32 bits wide, stored in Python strings. This is the same format as used by the `al` and `sunaudiodev` modules. All scalar items are integers, unless specified otherwise.

This module provides support for u-LAW and Intel/DVI ADPCM encodings. A few of the more complicated operations only take 16-bit samples, otherwise the sample size (in bytes) is always a parameter of the operation.

The module defines the following variables and functions:

<div class="excdesc">

error This exception is raised on all errors, such as unknown number of bytes per sample, etc.

</div>

<div class="funcdesc">

addfragment1, fragment2, width Return a fragment which is the addition of the two samples passed as parameters. *width* is the sample width in bytes, either `1`, `2` or `4`. Both fragments should have the same length.

</div>

<div class="funcdesc">

adpcm2linadpcmfragment, width, state Decode an Intel/DVI ADPCM coded fragment to a linear fragment. See the description of `lin2adpcm()` for details on ADPCM coding. Return a tuple `(`*`sample`*`, `*`newstate`*`)` where the sample has the width specified in *width*.

</div>

<div class="funcdesc">

adpcm32linadpcmfragment, width, state Decode an alternative 3-bit ADPCM code. See `lin2adpcm3()` for details.

</div>

<div class="funcdesc">

avgfragment, width Return the average over all samples in the fragment.

</div>

<div class="funcdesc">

avgppfragment, width Return the average peak-peak value over all samples in the fragment. No filtering is done, so the usefulness of this routine is questionable.

</div>

<div class="funcdesc">

biasfragment, width, bias Return a fragment that is the original fragment with a bias added to each sample.

</div>

<div class="funcdesc">

crossfragment, width Return the number of zero crossings in the fragment passed as an argument.

</div>

<div class="funcdesc">

findfactorfragment, reference Return a factor *F* such that `rms(add(`*`fragment`*`, mul(`*`reference`*`, -`*`F`*`)))` is minimal, i.e., return the factor with which you should multiply *reference* to make it match as well as possible to *fragment*. The fragments should both contain 2-byte samples.

The time taken by this routine is proportional to `len(`*`fragment`*`)`.

</div>

<div class="funcdesc">

findfitfragment, reference Try to match *reference* as well as possible to a portion of *fragment* (which should be the longer fragment). This is (conceptually) done by taking slices out of *fragment*, using `findfactor()` to compute the best match, and minimizing the result. The fragments should both contain 2-byte samples. Return a tuple `(`*`offset`*`, `*`factor`*`)` where *offset* is the (integer) offset into *fragment* where the optimal match started and *factor* is the (floating-point) factor as per `findfactor()`.

</div>

<div class="funcdesc">

findmaxfragment, length Search *fragment* for a slice of length *length* samples (not bytes!) with maximum energy, i.e., return *i* for which `rms(fragment[i*2:(i+length)*2])` is maximal. The fragments should both contain 2-byte samples.

The routine takes time proportional to `len(`*`fragment`*`)`.

</div>

<div class="funcdesc">

getsamplefragment, width, index Return the value of sample *index* from the fragment.

</div>

<div class="funcdesc">

lin2linfragment, width, newwidth Convert samples between 1-, 2- and 4-byte formats.

</div>

<div class="funcdesc">

lin2adpcmfragment, width, state Convert samples to 4 bit Intel/DVI ADPCM encoding. ADPCM coding is an adaptive coding scheme, whereby each 4 bit number is the difference between one sample and the next, divided by a (varying) step. The Intel/DVI ADPCM algorithm has been selected for use by the IMA, so it may well become a standard.

*state* is a tuple containing the state of the coder. The coder returns a tuple `(`*`adpcmfrag`*`, `*`newstate`*`)`, and the *newstate* should be passed to the next call of `lin2adpcm()`. In the initial call, `None` can be passed as the state. *adpcmfrag* is the ADPCM coded fragment packed 2 4-bit values per byte.

</div>

<div class="funcdesc">

lin2adpcm3fragment, width, state This is an alternative ADPCM coder that uses only 3 bits per sample. It is not compatible with the Intel/DVI ADPCM coder and its output is not packed (due to laziness on the side of the author). Its use is discouraged.

</div>

<div class="funcdesc">

lin2ulawfragment, width Convert samples in the audio fragment to u-LAW encoding and return this as a Python string. u-LAW is an audio encoding format whereby you get a dynamic range of about 14 bits using only 8 bit samples. It is used by the Sun audio hardware, among others.

</div>

<div class="funcdesc">

minmaxfragment, width Return a tuple consisting of the minimum and maximum values of all samples in the sound fragment.

</div>

<div class="funcdesc">

maxfragment, width Return the maximum of the *absolute value* of all samples in a fragment.

</div>

<div class="funcdesc">

maxppfragment, width Return the maximum peak-peak value in the sound fragment.

</div>

<div class="funcdesc">

mulfragment, width, factor Return a fragment that has all samples in the original fragment multiplied by the floating-point value *factor*. Overflow is silently ignored.

</div>

<div class="funcdesc">

ratecvfragment, width, nchannels, inrate, outrate, state Convert the frame rate of the input fragment.

*state* is a tuple containing the state of the converter. The converter returns a tuple `(`*`newfragment`*`, `*`newstate`*`)`, and *newstate* should be passed to the next call of `ratecv()`.

The *weightA* and *weightB* arguments are parameters for a simple digital filter and default to `1` and `0` respectively.

</div>

<div class="funcdesc">

reversefragment, width Reverse the samples in a fragment and returns the modified fragment.

</div>

<div class="funcdesc">

rmsfragment, width Return the root-mean-square of the fragment, i.e.
``` math
\catcode`_=8
\sqrt{\frac{\sum{{S_{i}}^{2}}}{n}}
```
This is a measure of the power in an audio signal.

</div>

<div class="funcdesc">

tomonofragment, width, lfactor, rfactor Convert a stereo fragment to a mono fragment. The left channel is multiplied by *lfactor* and the right channel by *rfactor* before adding the two channels to give a mono signal.

</div>

<div class="funcdesc">

tostereofragment, width, lfactor, rfactor Generate a stereo fragment from a mono fragment. Each pair of samples in the stereo fragment are computed from the mono sample, whereby left channel samples are multiplied by *lfactor* and right channel samples by *rfactor*.

</div>

<div class="funcdesc">

ulaw2linfragment, width Convert sound fragments in u-LAW encoding to linearly encoded sound fragments. u-LAW encoding always uses 8 bits samples, so *width* refers only to the sample width of the output fragment here.

</div>

Note that operations such as `mul()` or `max()` make no distinction between mono and stereo fragments, i.e. all samples are treated equal. If this is a problem the stereo fragment should be split into two mono fragments first and recombined later. Here is an example of how to do that:

    def mul_stereo(sample, width, lfactor, rfactor):
        lsample = audioop.tomono(sample, width, 1, 0)
        rsample = audioop.tomono(sample, width, 0, 1)
        lsample = audioop.mul(sample, width, lfactor)
        rsample = audioop.mul(sample, width, rfactor)
        lsample = audioop.tostereo(lsample, width, 1, 0)
        rsample = audioop.tostereo(rsample, width, 0, 1)
        return audioop.add(lsample, rsample, width)

If you use the ADPCM coder to build network packets and you want your protocol to be stateless (i.e. to be able to tolerate packet loss) you should not only transmit the data but also the state. Note that you should send the *initial* state (the one you passed to `lin2adpcm()`) along to the decoder, not the final state (as returned by the coder). If you want to use `struct.struct()` to store the state in binary you can code the first element (the predicted value) in 16 bits and the second (the delta index) in 8.

The ADPCM coders have never been tried against other ADPCM coders, only against themselves. It could well be that I misinterpreted the standards in which case they will not be interoperable with the respective standards.

The `find*()` routines might look a bit funny at first sight. They are primarily meant to do echo cancellation. A reasonably fast way to do this is to pick the most energetic piece of the output sample, locate that in the input sample and subtract the whole output sample from the input sample:

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
# `Bastion` — Restricting access to objects

*Providing restricted access to objects.*\
According to the dictionary, a bastion is “a fortified area or position”, or “something that is considered a stronghold.” It’s a suitable name for this module, which provides a way to forbid access to certain attributes of an object. It must always be used with the `rexec` module, in order to allow restricted-mode programs access to certain safe attributes of an object, while denying access to other, unsafe attributes.

<div class="funcdesc">

Bastionobject Protect the object *object*, returning a bastion for the object. Any attempt to access one of the object’s attributes will have to be approved by the *filter* function; if the access is denied an `AttributeError` exception will be raised.

If present, *filter* must be a function that accepts a string containing an attribute name, and returns true if access to that attribute will be permitted; if *filter* returns false, the access is denied. The default filter denies access to any function beginning with an underscore (). The bastion’s string representation will be `<Bastion for `*`name`*`>` if a value for *name* is provided; otherwise, `repr(`*`object`*`)` will be used.

*class*, if present, should be a subclass of `BastionClass`; see the code in `bastion.py` for the details. Overriding the default `BastionClass` will rarely be required.

</div>

<div class="classdesc">

BastionClassgetfunc, name Class which actually implements bastion objects. This is the default class used by `Bastion()`. The *getfunc* parameter is a function which returns the value of an attribute which should be exposed to the restricted execution environment when called with the name of the attribute as the only parameter. *name* is used to construct the `repr()` of the `BastionClass` instance.

</div>
# `bisect` — Array bisection algorithm

*Array bisection algorithms for binary searching.*\
This module provides support for maintaining a list in sorted order without having to sort the list after each insertion. For long lists of items with expensive comparison operations, this can be an improvement over the more common approach. The module is called `bisect` because it uses a basic bisection algorithm to do its work. The source code may be most useful as a working example of the algorithm (i.e., the boundary conditions are already right!).

The following functions are provided:

<div class="funcdesc">

bisectlist, item Locate the proper insertion point for *item* in *list* to maintain sorted order. The parameters *lo* and *hi* may be used to specify a subset of the list which should be considered. The return value is suitable for use as the first parameter to *`list`*`.insert()`.

</div>

<div class="funcdesc">

insortlist, item Insert *item* in *list* in sorted order. This is equivalent to *`list`*`.insert(bisect.bisect(`*`list`*`, `*`item`*`, `*`lo`*`, `*`hi`*`), `*`item`*`)`.

</div>

## Example

The `bisect()` function is generally useful for categorizing numeric data. This example uses `bisect()` to look up a letter grade for an exam total (say) based on a set of ordered numeric breakpoints: 85 and up is an ‘A’, 75..84 is a ‘B’, etc.

    >>> grades = "FEDCBA"
    >>> breakpoints = [30, 44, 66, 75, 85]
    >>> from bisect import bisect
    >>> def grade(total):
    ...           return grades[bisect(breakpoints, total)]
    ...
    >>> grade(66)
    'C'
    >>> map(grade, [33, 99, 77, 44, 12, 88])
    ['E', 'A', 'B', 'D', 'F', 'A']
# `__builtin__` — Built-in functions

*The set of built-in functions.*\
This module provides direct access to all ‘built-in’ identifiers of Python; e.g. `__builtin__.open` is the full name for the built-in function `open()`. See section <a href="#built-in-funcs" data-reference-type="ref" data-reference="built-in-funcs">[built-in-funcs]</a>, “Built-in Functions.”
# `cd` — CD-ROM access on SGI systems

*Interface to the CD-ROM on Silicon Graphics systems.*\
This module provides an interface to the Silicon Graphics CD library. It is available only on Silicon Graphics systems.

The way the library works is as follows. A program opens the CD-ROM device with `open()` and creates a parser to parse the data from the CD with `createparser()`. The object returned by `open()` can be used to read data from the CD, but also to get status information for the CD-ROM device, and to get information about the CD, such as the table of contents. Data from the CD is passed to the parser, which parses the frames, and calls any callback functions that have previously been added.

An audio CD is divided into *tracks* or *programs* (the terms are used interchangeably). Tracks can be subdivided into *indices*. An audio CD contains a *table of contents* which gives the starts of the tracks on the CD. Index 0 is usually the pause before the start of a track. The start of the track as given by the table of contents is normally the start of index 1.

Positions on a CD can be represented in two ways. Either a frame number or a tuple of three values, minutes, seconds and frames. Most functions use the latter representation. Positions can be both relative to the beginning of the CD, and to the beginning of the track.

Module `cd` defines the following functions and constants:

<div class="funcdesc">

createparser Create and return an opaque parser object. The methods of the parser object are described below.

</div>

<div class="funcdesc">

msftoframeminutes, seconds, frames Converts a `(`*`minutes`*`, `*`seconds`*`, `*`frames`*`)` triple representing time in absolute time code into the corresponding CD frame number.

</div>

<div class="funcdesc">

open Open the CD-ROM device. The return value is an opaque player object; methods of the player object are described below. The device is the name of the SCSI device file, e.g. `’/dev/scsi/sc0d4l0’`, or `None`. If omitted or `None`, the hardware inventory is consulted to locate a CD-ROM drive. The *mode*, if not omited, should be the string `’r’`.

</div>

The module defines the following variables:

<div class="excdesc">

error Exception raised on various errors.

</div>

<div class="datadesc">

DATASIZE The size of one frame’s worth of audio data. This is the size of the audio data as passed to the callback of type `audio`.

</div>

<div class="datadesc">

BLOCKSIZE The size of one uninterpreted frame of audio data.

</div>

The following variables are states as returned by `getstatus()`:

<div class="datadesc">

READY The drive is ready for operation loaded with an audio CD.

</div>

<div class="datadesc">

NODISC The drive does not have a CD loaded.

</div>

<div class="datadesc">

CDROM The drive is loaded with a CD-ROM. Subsequent play or read operations will return I/O errors.

</div>

<div class="datadesc">

ERROR An error occurred while trying to read the disc or its table of contents.

</div>

<div class="datadesc">

PLAYING The drive is in CD player mode playing an audio CD through its audio jacks.

</div>

<div class="datadesc">

PAUSED The drive is in CD layer mode with play paused.

</div>

<div class="datadesc">

STILL The equivalent of on older (non 3301) model Toshiba CD-ROM drives. Such drives have never been shipped by SGI.

</div>

<div class="datadesc">

audio Integer constants describing the various types of parser callbacks that can be set by the `addcallback()` method of CD parser objects (see below).

</div>

## Player Objects

Player objects (returned by `open()`) have the following methods:

<div class="methoddesc">

allowremoval Unlocks the eject button on the CD-ROM drive permitting the user to eject the caddy if desired.

</div>

<div class="methoddesc">

bestreadsize Returns the best value to use for the *num_frames* parameter of the `readda()` method. Best is defined as the value that permits a continuous flow of data from the CD-ROM drive.

</div>

<div class="methoddesc">

close Frees the resources associated with the player object. After calling `close()`, the methods of the object should no longer be used.

</div>

<div class="methoddesc">

eject Ejects the caddy from the CD-ROM drive.

</div>

<div class="methoddesc">

getstatus Returns information pertaining to the current state of the CD-ROM drive. The returned information is a tuple with the following values: *state*, *track*, *rtime*, *atime*, *ttime*, *first*, *last*, *scsi_audio*, *cur_block*. *rtime* is the time relative to the start of the current track; *atime* is the time relative to the beginning of the disc; *ttime* is the total time on the disc. For more information on the meaning of the values, see the man page . The value of *state* is one of the following: , , , , , , or .

</div>

<div class="methoddesc">

gettrackinfotrack Returns information about the specified track. The returned information is a tuple consisting of two elements, the start time of the track and the duration of the track.

</div>

<div class="methoddesc">

msftoblockmin, sec, frame Converts a minutes, seconds, frames triple representing a time in absolute time code into the corresponding logical block number for the given CD-ROM drive. You should use `msftoframe()` rather than `msftoblock()` for comparing times. The logical block number differs from the frame number by an offset required by certain CD-ROM drives.

</div>

<div class="methoddesc">

playstart, play Starts playback of an audio CD in the CD-ROM drive at the specified track. The audio output appears on the CD-ROM drive’s headphone and audio jacks (if fitted). Play stops at the end of the disc. *start* is the number of the track at which to start playing the CD; if *play* is 0, the CD will be set to an initial paused state. The method `togglepause()` can then be used to commence play.

</div>

<div class="methoddesc">

playabsminutes, seconds, frames, play Like `play()`, except that the start is given in minutes, seconds, and frames instead of a track number.

</div>

<div class="methoddesc">

playtrackstart, play Like `play()`, except that playing stops at the end of the track.

</div>

<div class="methoddesc">

playtrackabstrack, minutes, seconds, frames, play Like `play()`, except that playing begins at the specified absolute time and ends at the end of the specified track.

</div>

<div class="methoddesc">

preventremoval Locks the eject button on the CD-ROM drive thus preventing the user from arbitrarily ejecting the caddy.

</div>

<div class="methoddesc">

readdanum_frames Reads the specified number of frames from an audio CD mounted in the CD-ROM drive. The return value is a string representing the audio frames. This string can be passed unaltered to the `parseframe()` method of the parser object.

</div>

<div class="methoddesc">

seekminutes, seconds, frames Sets the pointer that indicates the starting point of the next read of digital audio data from a CD-ROM. The pointer is set to an absolute time code location specified in *minutes*, *seconds*, and *frames*. The return value is the logical block number to which the pointer has been set.

</div>

<div class="methoddesc">

seekblockblock Sets the pointer that indicates the starting point of the next read of digital audio data from a CD-ROM. The pointer is set to the specified logical block number. The return value is the logical block number to which the pointer has been set.

</div>

<div class="methoddesc">

seektracktrack Sets the pointer that indicates the starting point of the next read of digital audio data from a CD-ROM. The pointer is set to the specified track. The return value is the logical block number to which the pointer has been set.

</div>

<div class="methoddesc">

stop Stops the current playing operation.

</div>

<div class="methoddesc">

togglepause Pauses the CD if it is playing, and makes it play if it is paused.

</div>

## Parser Objects

Parser objects (returned by `createparser()`) have the following methods:

<div class="methoddesc">

addcallbacktype, func, arg Adds a callback for the parser. The parser has callbacks for eight different types of data in the digital audio data stream. Constants for these types are defined at the `cd` module level (see above). The callback is called as follows: *`func`*`(`*`arg`*`, type, data)`, where *arg* is the user supplied argument, *type* is the particular type of callback, and *data* is the data returned for this *type* of callback. The type of the data depends on the *type* of callback as follows:

<div class="tableii">

l\|p4incodeTypeValue

</div>

</div>

<div class="methoddesc">

deleteparser Deletes the parser and frees the memory it was using. The object should not be used after this call. This call is done automatically when the last reference to the object is removed.

</div>

<div class="methoddesc">

parseframeframe Parses one or more frames of digital audio data from a CD such as returned by `readda()`. It determines which subcodes are present in the data. If these subcodes have changed since the last frame, then `parseframe()` executes a callback of the appropriate type passing to it the subcode data found in the frame. Unlike the C function, more than one frame of digital audio data can be passed to this method.

</div>

<div class="methoddesc">

removecallbacktype Removes the callback for the given *type*.

</div>

<div class="methoddesc">

resetparser Resets the fields of the parser used for tracking subcodes to an initial state. `resetparser()` should be called after the disc has been changed.

</div>
# `cgi` — Common Gateway Interface support.

*Common Gateway Interface support, used to interpret forms in server-side scripts.*\
Support module for CGI (Common Gateway Interface) scripts. This module defines a number of utilities for use by CGI scripts written in Python.

## Introduction

A CGI script is invoked by an HTTP server, usually to process user input submitted through an HTML `<FORM>` or `<ISINDEX>` element.

Most often, CGI scripts live in the server’s special `cgi-bin` directory. The HTTP server places all sorts of information about the request (such as the client’s hostname, the requested URL, the query string, and lots of other goodies) in the script’s shell environment, executes the script, and sends the script’s output back to the client.

The script’s input is connected to the client too, and sometimes the form data is read this way; at other times the form data is passed via the “query string” part of the URL. This module is intended to take care of the different cases and provide a simpler interface to the Python script. It also provides a number of utilities that help in debugging scripts, and the latest addition is support for file uploads from a form (if your browser supports it — Grail 0.3 and Netscape 2.0 do).

The output of a CGI script should consist of two sections, separated by a blank line. The first section contains a number of headers, telling the client what kind of data is following. Python code to generate a minimal header section looks like this:

    print "Content-Type: text/html"     # HTML is following
    print                               # blank line, end of headers

The second section is usually HTML, which allows the client software to display nicely formatted text with header, in-line images, etc. Here’s Python code that prints a simple piece of HTML:

    print "<TITLE>CGI script output</TITLE>"
    print "<H1>This is my first CGI script</H1>"
    print "Hello, world!"

## Using the cgi module

Begin by writing `import cgi`. Do not use `from cgi import *` — the module defines all sorts of names for its own use or for backward compatibility that you don’t want in your namespace.

It’s best to use the `FieldStorage` class. The other classes defined in this module are provided mostly for backward compatibility. Instantiate it exactly once, without arguments. This reads the form contents from standard input or the environment (depending on the value of various environment variables set according to the CGI standard). Since it may consume standard input, it should be instantiated only once.

The `FieldStorage` instance can be indexed like a Python dictionary, and also supports the standard dictionary methods `has_key()` and `keys()`. Form fields containing empty strings are ignored and do not appear in the dictionary; to keep such values, provide the optional `keep_blank_values` argument when creating the `FieldStorage` instance.

For instance, the following code (which assumes that the `Content-Type` header and blank line have already been printed) checks that the fields `name` and `addr` are both set to a non-empty string:

    form = cgi.FieldStorage()
    form_ok = 0
    if form.has_key("name") and form.has_key("addr"):
        form_ok = 1
    if not form_ok:
        print "<H1>Error</H1>"
        print "Please fill in the name and addr fields."
        return
    print "<p>name:", form["name"].value
    print "<p>addr:", form["addr"].value
    ...further form processing here...

Here the fields, accessed through `form[`*`key`*`]`, are themselves instances of `FieldStorage` (or `MiniFieldStorage`, depending on the form encoding). The `value` attribute of the instance yields the string value of the field. The `getvalue()` method returns this string value directly; it also accepts an optional second argument as a default to return if the requested key is not present.

If the submitted form data contains more than one field with the same name, the object retrieved by `form[`*`key`*`]` is not a `FieldStorage` or `MiniFieldStorage` instance but a list of such instances. Similarly, in this situation, `form.getvalue(`*`key`*`)` would return a list of strings. If you expect this possibility (i.e., when your HTML form contains multiple fields with the same name), use the `type()` function to determine whether you have a single instance or a list of instances. For example, here’s code that concatenates any number of username fields, separated by commas:

    value = form.getvalue("username", "")
    if type(value) is type([]):
        # Multiple username fields specified
        usernames = ",".join(value)
    else:
        # Single or no username field specified
        usernames = value

If a field represents an uploaded file, accessing the value via the `value` attribute or the `getvalue()` method reads the entire file in memory as a string. This may not be what you want. You can test for an uploaded file by testing either the `filename` attribute or the `file` attribute. You can then read the data at leisure from the `file` attribute:

    fileitem = form["userfile"]
    if fileitem.file:
        # It's an uploaded file; count lines
        linecount = 0
        while 1:
            line = fileitem.file.readline()
            if not line: break
            linecount = linecount + 1

The file upload draft standard entertains the possibility of uploading multiple files from one field (using a recursive encoding). When this occurs, the item will be a dictionary-like `FieldStorage` item. This can be determined by testing its `type` attribute, which should be (or perhaps another MIME type matching ). In this case, it can be iterated over recursively just like the top-level form object.

When a form is submitted in the “old” format (as the query string or as a single data part of type ), the items will actually be instances of the class `MiniFieldStorage`. In this case, the `list`, `file`, and `filename` attributes are always `None`.

## Old classes

These classes, present in earlier versions of the `cgi` module, are still supported for backward compatibility. New applications should use the `FieldStorage` class.

`SvFormContentDict` stores single value form content as dictionary; it assumes each field name occurs in the form only once.

`FormContentDict` stores multiple value form content as a dictionary (the form items are lists of values). Useful if your form contains multiple fields with the same name.

Other classes (`FormContent`, `InterpFormContentDict`) are present for backwards compatibility with really old applications only. If you still use these and would be inconvenienced when they disappeared from a next version of this module, drop me a note.

## Functions

These are useful if you want more control, or if you want to employ some of the algorithms implemented in this module in other circumstances.

<div class="funcdesc">

parsefp Parse a query in the environment or from a file (default `sys.stdin`).

</div>

<div class="funcdesc">

parse_qsqs Parse a query string given as a string argument (data of type ). Data are returned as a dictionary. The dictionary keys are the unique query variable names and the values are lists of values for each name.

The optional argument *keep_blank_values* is a flag indicating whether blank values in URL encoded queries should be treated as blank strings. A true value indicates that blanks should be retained as blank strings. The default false value indicates that blank values are to be ignored and treated as if they were not included.

The optional argument *strict_parsing* is a flag indicating what to do with parsing errors. If false (the default), errors are silently ignored. If true, errors raise a ValueError exception.

</div>

<div class="funcdesc">

parse_qslqs Parse a query string given as a string argument (data of type ). Data are returned as a list of name, value pairs.

The optional argument *keep_blank_values* is a flag indicating whether blank values in URL encoded queries should be treated as blank strings. A true value indicates that blanks should be retained as blank strings. The default false value indicates that blank values are to be ignored and treated as if they were not included.

The optional argument *strict_parsing* is a flag indicating what to do with parsing errors. If false (the default), errors are silently ignored. If true, errors raise a ValueError exception.

</div>

<div class="funcdesc">

parse_multipartfp, pdict Parse input of type (for file uploads). Arguments are *fp* for the input file and *pdict* for a dictionary containing other parameters in the `Content-Type` header.

Returns a dictionary just like `parse_qs()` keys are the field names, each value is a list of values for that field. This is easy to use but not much good if you are expecting megabytes to be uploaded — in that case, use the `FieldStorage` class instead which is much more flexible.

Note that this does not parse nested multipart parts — use `FieldStorage` for that.

</div>

<div class="funcdesc">

parse_headerstring Parse a MIME header (such as `Content-Type`) into a main value and a dictionary of parameters.

</div>

<div class="funcdesc">

test Robust test CGI script, usable as main program. Writes minimal HTTP headers and formats all information provided to the script in HTML form.

</div>

<div class="funcdesc">

print_environ Format the shell environment in HTML.

</div>

<div class="funcdesc">

print_formform Format a form in HTML.

</div>

<div class="funcdesc">

print_directory Format the current directory in HTML.

</div>

<div class="funcdesc">

print_environ_usage Print a list of useful (used by CGI) environment variables in HTML.

</div>

<div class="funcdesc">

escapes Convert the characters , and in string *s* to HTML-safe sequences. Use this if you need to display text that might contain such characters in HTML. If the optional flag *quote* is true, the double quote character () is also translated; this helps for inclusion in an HTML attribute value, e.g. in `<A HREF="...">`.

</div>

## Caring about security

There’s one important rule: if you invoke an external program (e.g. via the `os.system()` or `os.popen()` functions), make very sure you don’t pass arbitrary strings received from the client to the shell. This is a well-known security hole whereby clever hackers anywhere on the web can exploit a gullible CGI script to invoke arbitrary shell commands. Even parts of the URL or field names cannot be trusted, since the request doesn’t have to come from your form!

To be on the safe side, if you must pass a string gotten from a form to a shell command, you should make sure the string contains only alphanumeric characters, dashes, underscores, and periods.

## Installing your CGI script on a Unix system

Read the documentation for your HTTP server and check with your local system administrator to find the directory where CGI scripts should be installed; usually this is in a directory `cgi-bin` in the server tree.

Make sure that your script is readable and executable by “others”; the Unix file mode should be `0755` octal (use `chmod 0755 `*`filename`*). Make sure that the first line of the script contains `#!` starting in column 1 followed by the pathname of the Python interpreter, for instance:

    #!/usr/local/bin/python

Make sure the Python interpreter exists and is executable by “others”.

Make sure that any files your script needs to read or write are readable or writable, respectively, by “others” — their mode should be `0644` for readable and `0666` for writable. This is because, for security reasons, the HTTP server executes your script as user “nobody”, without any special privileges. It can only read (write, execute) files that everybody can read (write, execute). The current directory at execution time is also different (it is usually the server’s cgi-bin directory) and the set of environment variables is also different from what you get at login. In particular, don’t count on the shell’s search path for executables () or the Python module search path () to be set to anything interesting.

If you need to load modules from a directory which is not on Python’s default module search path, you can change the path in your script, before importing other modules, e.g.:

    import sys
    sys.path.insert(0, "/usr/home/joe/lib/python")
    sys.path.insert(0, "/usr/local/lib/python")

(This way, the directory inserted last will be searched first!)

Instructions for non-Unix systems will vary; check your HTTP server’s documentation (it will usually have a section on CGI scripts).

## Testing your CGI script

Unfortunately, a CGI script will generally not run when you try it from the command line, and a script that works perfectly from the command line may fail mysteriously when run from the server. There’s one reason why you should still test your script from the command line: if it contains a syntax error, the Python interpreter won’t execute it at all, and the HTTP server will most likely send a cryptic error to the client.

Assuming your script has no syntax errors, yet it does not work, you have no choice but to read the next section.

## Debugging CGI scripts

First of all, check for trivial installation errors — reading the section above on installing your CGI script carefully can save you a lot of time. If you wonder whether you have understood the installation procedure correctly, try installing a copy of this module file (`cgi.py`) as a CGI script. When invoked as a script, the file will dump its environment and the contents of the form in HTML form. Give it the right mode etc, and send it a request. If it’s installed in the standard `cgi-bin` directory, it should be possible to send it a request by entering a URL into your browser of the form:

    http://yourhostname/cgi-bin/cgi.py?name=Joe+Blow&addr=At+Home

If this gives an error of type 404, the server cannot find the script – perhaps you need to install it in a different directory. If it gives another error (e.g. 500), there’s an installation problem that you should fix before trying to go any further. If you get a nicely formatted listing of the environment and form content (in this example, the fields should be listed as “addr” with value “At Home” and “name” with value “Joe Blow”), the `cgi.py` script has been installed correctly. If you follow the same procedure for your own script, you should now be able to debug it.

The next step could be to call the `cgi` module’s `test()` function from your script: replace its main code with the single statement

    cgi.test()

This should produce the same results as those gotten from installing the `cgi.py` file itself.

When an ordinary Python script raises an unhandled exception (e.g. because of a typo in a module name, a file that can’t be opened, etc.), the Python interpreter prints a nice traceback and exits. While the Python interpreter will still do this when your CGI script raises an exception, most likely the traceback will end up in one of the HTTP server’s log file, or be discarded altogether.

Fortunately, once you have managed to get your script to execute *some* code, it is easy to catch exceptions and cause a traceback to be printed. The `test()` function below in this module is an example. Here are the rules:

1.  Import the traceback module before entering the ... statement

2.  Assign `sys.stderr` to be `sys.stdout`

3.  Make sure you finish printing the headers and the blank line early

4.  Wrap all remaining code in a ... statement

5.  In the except clause, call `traceback.print_exc()`

For example:

    import sys
    import traceback
    print "Content-Type: text/html"
    print
    sys.stderr = sys.stdout
    try:
        ...your code here...
    except:
        print "\n\n<PRE>"
        traceback.print_exc()

Notes: The assignment to `sys.stderr` is needed because the traceback prints to `sys.stderr`. The `print "nn<PRE>"` statement is necessary to disable the word wrapping in HTML.

If you suspect that there may be a problem in importing the traceback module, you can use an even more robust approach (which only uses built-in modules):

    import sys
    sys.stderr = sys.stdout
    print "Content-Type: text/plain"
    print
    ...your code here...

This relies on the Python interpreter to print the traceback. The content type of the output is set to plain text, which disables all HTML processing. If your script works, the raw HTML will be displayed by your client. If it raises an exception, most likely after the first two lines have been printed, a traceback will be displayed. Because no HTML interpretation is going on, the traceback will readable.

## Common problems and solutions

- Most HTTP servers buffer the output from CGI scripts until the script is completed. This means that it is not possible to display a progress report on the client’s display while the script is running.

- Check the installation instructions above.

- Check the HTTP server’s log files. (`tail -f logfile` in a separate window may be useful!)

- Always check a script for syntax errors first, by doing something like `python script.py`.

- When using any of the debugging techniques, don’t forget to add `import sys` to the top of the script.

- When invoking external programs, make sure they can be found. Usually, this means using absolute path names — is usually not set to a very useful value in a CGI script.

- When reading or writing external files, make sure they can be read or written by every user on the system.

- Don’t try to give a CGI script a set-uid mode. This doesn’t work on most systems, and is a security liability as well.
# `chunk` — Read IFF chunked data

*Module to read IFF chunks.*\
This module provides an interface for reading files that use EA IFF 85 chunks.[^1] This format is used in at least the AudioInterchange File Format (AIFF/AIFF-C) and the RealMedia File Format(RMFF). The WAVE audio file format is closely related and can also be read using this module.

A chunk has the following structure:

|  |  |  |
|:---|:---|:---|
| OffsetLengthContents 0 | 4 | Chunk ID |
| 4 | 4 | Size of chunk in big-endian byte order, not including the header |
| 8 |  |  |
|  |  |  |
|  |  |  |

The ID is a 4-byte string which identifies the type of chunk.

The size field (a 32-bit value, encoded using big-endian byte order) gives the size of the chunk data, not including the 8-byte header.

Usually an IFF-type file consists of one or more chunks. The proposed usage of the `Chunk` class defined here is to instantiate an instance at the start of each chunk and read from the instance until it reaches the end, after which a new instance can be instantiated. At the end of the file, creating a new instance will fail with a `EOFError` exception.

<div class="classdesc">

Chunkfile Class which represents a chunk. The *file* argument is expected to be a file-like object. An instance of this class is specifically allowed. The only method that is needed is `read()`. If the methods `seek()` and `tell()` are present and don’t raise an exception, they are also used. If these methods are present and raise an exception, they are expected to not have altered the object. If the optional argument *align* is true, chunks are assumed to be aligned on 2-byte boundaries. If *align* is false, no alignment is assumed. The default value is true. If the optional argument *bigendian* is false, the chunk size is assumed to be in little-endian order. This is needed for WAVE audio files. The default value is true. If the optional argument *inclheader* is true, the size given in the chunk header includes the size of the header. The default value is false.

</div>

A `Chunk` object supports the following methods:

<div class="methoddesc">

getname Returns the name (ID) of the chunk. This is the first 4 bytes of the chunk.

</div>

<div class="methoddesc">

getsize Returns the size of the chunk.

</div>

<div class="methoddesc">

close Close and skip to the end of the chunk. This does not close the underlying file.

</div>

The remaining methods will raise `IOError` if called after the `close()` method has been called.

<div class="methoddesc">

isatty Returns `0`.

</div>

<div class="methoddesc">

seekpos Set the chunk’s current position. The *whence* argument is optional and defaults to `0` (absolute file positioning); other values are `1` (seek relative to the current position) and `2` (seek relative to the file’s end). There is no return value. If the underlying file does not allow seek, only forward seeks are allowed.

</div>

<div class="methoddesc">

tell Return the current position into the chunk.

</div>

<div class="methoddesc">

read Read at most *size* bytes from the chunk (less if the read hits the end of the chunk before obtaining *size* bytes). If the *size* argument is negative or omitted, read all data until the end of the chunk. The bytes are returned as a string object. An empty string is returned when the end of the chunk is encountered immediately.

</div>

<div class="methoddesc">

skip Skip to the end of the chunk. All further calls to `read()` for the chunk will return `’’`. If you are not interested in the contents of the chunk, this method should be called so that the file points to the start of the next chunk.

</div>

[^1]: “EA IFF 85” Standard for Interchange Format Files, Jerry Morrison, Electronic Arts, January 1985.
# `cmath` — Mathematical functions for complex numbers

*Mathematical functions for complex numbers.*\
This module is always available. It provides access to mathematical functions for complex numbers. The functions are:

<div class="funcdesc">

acosx Return the arc cosine of *x*.

</div>

<div class="funcdesc">

acoshx Return the hyperbolic arc cosine of *x*.

</div>

<div class="funcdesc">

asinx Return the arc sine of *x*.

</div>

<div class="funcdesc">

asinhx Return the hyperbolic arc sine of *x*.

</div>

<div class="funcdesc">

atanx Return the arc tangent of *x*.

</div>

<div class="funcdesc">

atanhx Return the hyperbolic arc tangent of *x*.

</div>

<div class="funcdesc">

cosx Return the cosine of *x*.

</div>

<div class="funcdesc">

coshx Return the hyperbolic cosine of *x*.

</div>

<div class="funcdesc">

expx Return the exponential value `e**`*`x`*.

</div>

<div class="funcdesc">

logx Return the natural logarithm of *x*.

</div>

<div class="funcdesc">

log10x Return the base-10 logarithm of *x*.

</div>

<div class="funcdesc">

sinx Return the sine of *x*.

</div>

<div class="funcdesc">

sinhx Return the hyperbolic sine of *x*.

</div>

<div class="funcdesc">

sqrtx Return the square root of *x*.

</div>

<div class="funcdesc">

tanx Return the tangent of *x*.

</div>

<div class="funcdesc">

tanhx Return the hyperbolic tangent of *x*.

</div>

The module also defines two mathematical constants:

<div class="datadesc">

pi The mathematical constant *pi*, as a real.

</div>

<div class="datadesc">

e The mathematical constant *e*, as a real.

</div>

Note that the selection of functions is similar, but not identical, to that in module `math`. The reason for having two modules is that some users aren’t interested in complex numbers, and perhaps don’t even know what they are. They would rather have `math.sqrt(-1)` raise an exception than return a complex number. Also note that the functions defined in `cmath` always return a complex number, even if the answer can be expressed as a real number (in which case the complex number has an imaginary part of zero).
# `cmd` — Build line-oriented command interpreters.

*Build line-oriented command interpreters; this is used by module `pdb`.*\
The `Cmd` class provides a simple framework for writing line-oriented command interpreters. These are often useful for test harnesses, administrative tools, and prototypes that will later be wrapped in a more sophisticated interface.

<div class="classdesc">

Cmd A `Cmd` instance or subclass instance is a line-oriented interpreter framework. There is no good reason to instantiate `Cmd` itself; rather, it’s useful as a superclass of an interpreter class you define yourself in order to inherit `Cmd`’s methods and encapsulate action methods.

</div>

## Cmd Objects

A `Cmd` instance has the following methods:

<div class="methoddesc">

cmdloop Repeatedly issue a prompt, accept input, parse an initial prefix off the received input, and dispatch to action methods, passing them the remainder of the line as argument.

The optional argument is a banner or intro string to be issued before the first prompt (this overrides the `intro` class member).

If the `readline` module is loaded, input will automatically inherit -like history-list editing (e.g. `Ctrl-P` scrolls back to the last command, `Ctrl-N` forward to the next one, `Ctrl-F` moves the cursor to the right non-destructively, `Ctrl-B` moves the cursor to the left non-destructively, etc.).

An end-of-file on input is passed back as the string `’EOF’`.

An interpreter instance will recognize a command name `foo` if and only if it has a method `do_foo()`. As a special case, a line beginning with the character is dispatched to the method `do_help()`. As another special case, a line beginning with the character is dispatched to the method `do_shell` (if such a method is defined).

All subclasses of `Cmd` inherit a predefined `do_help`. This method, called with an argument `bar`, invokes the corresponding method `help_bar()`. With no argument, `do_help()` lists all available help topics (that is, all commands with corresponding `help_*()` methods), and also lists any undocumented commands.

</div>

<div class="methoddesc">

onecmdstr Interpret the argument as though it had been typed in in response to the prompt.

</div>

<div class="methoddesc">

emptyline Method called when an empty line is entered in response to the prompt. If this method is not overridden, it repeats the last nonempty command entered.

</div>

<div class="methoddesc">

defaultline Method called on an input line when the command prefix is not recognized. If this method is not overridden, it prints an error message and returns.

</div>

<div class="methoddesc">

precmd Hook method executed just before the input prompt is issued. This method is a stub in `Cmd`; it exists to be overridden by subclasses.

</div>

<div class="methoddesc">

postcmd Hook method executed just after a command dispatch is finished. This method is a stub in `Cmd`; it exists to be overridden by subclasses.

</div>

<div class="methoddesc">

preloop Hook method executed once when `cmdloop()` is called. This method is a stub in `Cmd`; it exists to be overridden by subclasses.

</div>

<div class="methoddesc">

postloop Hook method executed once when `cmdloop()` is about to return. This method is a stub in `Cmd`; it exists to be overridden by subclasses.

</div>

Instances of `Cmd` subclasses have some public instance variables:

<div class="memberdesc">

prompt The prompt issued to solicit input.

</div>

<div class="memberdesc">

identchars The string of characters accepted for the command prefix.

</div>

<div class="memberdesc">

lastcmd The last nonempty command prefix seen.

</div>

<div class="memberdesc">

intro A string to issue as an intro or banner. May be overridden by giving the `cmdloop()` method an argument.

</div>

<div class="memberdesc">

doc_header The header to issue if the help output has a section for documented commands.

</div>

<div class="memberdesc">

misc_header The header to issue if the help output has a section for miscellaneous help topics (that is, there are `help_*()` methods without corresponding `do_*()` methods).

</div>

<div class="memberdesc">

undoc_header The header to issue if the help output has a section for undocumented commands (that is, there are `do_*()` methods without corresponding `help_*()` methods).

</div>

<div class="memberdesc">

ruler The character used to draw separator lines under the help-message headers. If empty, no ruler line is drawn. It defaults to .

</div>
# `cmp` — File comparisons

*Compare files very efficiently.*\
*Deprecated since version 1.5.3: Use the `filecmp` module instead.*

The `cmp` module defines a function to compare files, taking all sort of short-cuts to make it a highly efficient operation.

The `cmp` module defines the following function:

<div class="funcdesc">

cmpf1, f2 Compare two files given as names. The following tricks are used to optimize the comparisons:

- Files with identical type, size and mtime are assumed equal.

- Files with different type or size are never equal.

- The module only compares files it already compared if their signature (type, size and mtime) changed.

- No external programs are called.

</div>

Example:

    >>> import cmp
    >>> cmp.cmp('libundoc.tex', 'libundoc.tex')
    1
    >>> cmp.cmp('libundoc.tex', 'lib.tex')
    0
# `cmpcache` — Efficient file comparisons

*Compare files very efficiently.*\
*Deprecated since version 1.5.3: Use the `filecmp` module instead.*

The `cmpcache` module provides an identical interface and similar functionality as the `cmp` module, but can be a bit more efficient as it uses `statcache.stat()` instead of `os.stat()` (see the `statcache` module for information on the difference).

**Note:** Using the `statcache` module to provide `stat()` information results in trashing the cache invalidation mechanism: results are not as reliable. To ensure “current” results, use `cmp.cmp()` instead of the version defined in this module, or use `statcache.forget()` to invalidate the appropriate entries.
# `code` — Interpreter base classes

*Base classes for interactive Python interpreters.*\
The `code` module provides facilities to implement read-eval-print loops in Python. Two classes and convenience functions are included which can be used to build applications which provide an interactive interpreter prompt.

<div class="classdesc">

InteractiveInterpreter This class deals with parsing and interpreter state (the user’s namespace); it does not deal with input buffering or prompting or input file naming (the filename is always passed in explicitly). The optional *locals* argument specifies the dictionary in which code will be executed; it defaults to a newly created dictionary with key `’__name__’` set to `’__console__’` and key `’__doc__’` set to `None`.

</div>

<div class="classdesc">

InteractiveConsole Closely emulate the behavior of the interactive Python interpreter. This class builds on `InteractiveInterpreter` and adds prompting using the familiar `sys.ps1` and `sys.ps2`, and input buffering.

</div>

<div class="funcdesc">

interact Convenience function to run a read-eval-print loop. This creates a new instance of `InteractiveConsole` and sets *readfunc* to be used as the `raw_input()` method, if provided. If *local* is provided, it is passed to the `InteractiveConsole` constructor for use as the default namespace for the interpreter loop. The `interact()` method of the instance is then run with *banner* passed as the banner to use, if provided. The console object is discarded after use.

</div>

<div class="funcdesc">

compile_commandsource This function is useful for programs that want to emulate Python’s interpreter main loop (a.k.a. the read-eval-print loop). The tricky part is to determine when the user has entered an incomplete command that can be completed by entering more text (as opposed to a complete command or a syntax error). This function *almost* always makes the same decision as the real interpreter main loop.

*source* is the source string; *filename* is the optional filename from which source was read, defaulting to `’<input>’`; and *symbol* is the optional grammar start symbol, which should be either `’single’` (the default) or `’eval’`.

Returns a code object (the same as `compile(`*`source`*`, `*`filename`*`, `*`symbol`*`)`) if the command is complete and valid; `None` if the command is incomplete; raises `SyntaxError` if the command is complete and contains a syntax error, or raises `OverflowError` if the command includes a numeric constant which exceeds the range of the appropriate numeric type.

</div>

## Interactive Interpreter Objects <span id="interpreter-objects" label="interpreter-objects"></span>

<div class="methoddesc">

runsourcesource Compile and run some source in the interpreter. Arguments are the same as for `compile_command()`; the default for *filename* is `’<input>’`, and for *symbol* is `’single’`. One several things can happen:

- The input is incorrect; `compile_command()` raised an exception (`SyntaxError` or `OverflowError`). A syntax traceback will be printed by calling the `showsyntaxerror()` method. `runsource()` returns `0`.

- The input is incomplete, and more input is required; `compile_command()` returned `None`. `runsource()` returns `1`.

- The input is complete; `compile_command()` returned a code object. The code is executed by calling the `runcode()` (which also handles run-time exceptions, except for `SystemExit`). `runsource()` returns `0`.

The return value can be used to decide whether to use `sys.ps1` or `sys.ps2` to prompt the next line.

</div>

<div class="methoddesc">

runcodecode Execute a code object. When an exception occurs, `showtraceback()` is called to display a traceback. All exceptions are caught except `SystemExit`, which is allowed to propagate.

A note about `KeyboardInterrupt`: this exception may occur elsewhere in this code, and may not always be caught. The caller should be prepared to deal with it.

</div>

<div class="methoddesc">

showsyntaxerror Display the syntax error that just occurred. This does not display a stack trace because there isn’t one for syntax errors. If *filename* is given, it is stuffed into the exception instead of the default filename provided by Python’s parser, because it always uses `’<string>’` when reading from a string. The output is written by the `write()` method.

</div>

<div class="methoddesc">

showtraceback Display the exception that just occurred. We remove the first stack item because it is within the interpreter object implementation. The output is written by the `write()` method.

</div>

<div class="methoddesc">

writedata Write a string to the standard error stream (`sys.stderr`). Derived classes should override this to provide the appropriate output handling as needed.

</div>

## Interactive Console Objects <span id="console-objects" label="console-objects"></span>

The `InteractiveConsole` class is a subclass of `InteractiveInterpreter`, and so offers all the methods of the interpreter objects as well as the following additions.

<div class="methoddesc">

interact Closely emulate the interactive Python console. The optional banner argument specify the banner to print before the first interaction; by default it prints a banner similar to the one printed by the standard Python interpreter, followed by the class name of the console object in parentheses (so as not to confuse this with the real interpreter – since it’s so close!).

</div>

<div class="methoddesc">

pushline Push a line of source text to the interpreter. The line should not have a trailing newline; it may have internal newlines. The line is appended to a buffer and the interpreter’s `runsource()` method is called with the concatenated contents of the buffer as source. If this indicates that the command was executed or invalid, the buffer is reset; otherwise, the command is incomplete, and the buffer is left as it was after the line was appended. The return value is `1` if more input is required, `0` if the line was dealt with in some way (this is the same as `runsource()`).

</div>

<div class="methoddesc">

resetbuffer Remove any unhandled source text from the input buffer.

</div>

<div class="methoddesc">

raw_input Write a prompt and read a line. The returned line does not include the trailing newline. When the user enters the EOF key sequence, `EOFError` is raised. The base implementation uses the built-in function `raw_input()`; a subclass may replace this with a different implementation.

</div>
# `codecs` — Codec registry and base classes

*Encode and decode data and streams.*\
This module defines base classes for standard Python codecs (encoders and decoders) and provides access to the internal Python codec registry which manages the codec lookup process.

It defines the following functions:

<div class="funcdesc">

registersearch_function Register a codec search function. Search functions are expected to take one argument, the encoding name in all lower case letters, and return a tuple of functions `(`*`encoder`*`, `*`decoder`*`, `*`stream_reader`*`, `*`stream_writer`*`)` taking the following arguments:

*encoder* and *decoder*: These must be functions or methods which have the same interface as the .encode/.decode methods of Codec instances (see Codec Interface). The functions/methods are expected to work in a stateless mode.

*stream_reader* and *stream_writer*: These have to be factory functions providing the following interface:

`factory(`*`stream`*`, `*`errors`*`=’strict’)`

The factory functions must return objects providing the interfaces defined by the base classes `StreamWriter` and `StreamReader`, respectively. Stream codecs can maintain state.

Possible values for errors are `’strict’` (raise an exception in case of an encoding error), `’replace’` (replace malformed data with a suitable replacement marker, such as ) and `’ignore’` (ignore malformed data and continue without further notice).

In case a search function cannot find a given encoding, it should return `None`.

</div>

<div class="funcdesc">

lookupencoding Looks up a codec tuple in the Python codec registry and returns the function tuple as defined above.

Encodings are first looked up in the registry’s cache. If not found, the list of registered search functions is scanned. If no codecs tuple is found, a `LookupError` is raised. Otherwise, the codecs tuple is stored in the cache and returned to the caller.

</div>

To simplify working with encoded files or stream, the module also defines these utility functions:

<div class="funcdesc">

openfilename, mode Open an encoded file using the given *mode* and return a wrapped version providing transparent encoding/decoding.

**Note:** The wrapped version will only accept the object format defined by the codecs, i.e. Unicode objects for most built-in codecs. Output is also codec-dependent and will usually be Unicode as well.

*encoding* specifies the encoding which is to be used for the the file.

*errors* may be given to define the error handling. It defaults to `’strict’` which causes a `ValueError` to be raised in case an encoding error occurs.

*buffering* has the same meaning as for the built-in `open()` function. It defaults to line buffered.

</div>

<div class="funcdesc">

EncodedFilefile, input Return a wrapped version of file which provides transparent encoding translation.

Strings written to the wrapped file are interpreted according to the given *input* encoding and then written to the original file as strings using the *output* encoding. The intermediate encoding will usually be Unicode but depends on the specified codecs.

If *output* is not given, it defaults to *input*.

*errors* may be given to define the error handling. It defaults to `’strict’`, which causes `ValueError` to be raised in case an encoding error occurs.

</div>

...XXX document codec base classes...

The module also provides the following constants which are useful for reading and writing to platform dependent files:

<div class="datadesc">

BOM These constants define the byte order marks (BOM) used in data streams to indicate the byte order used in the stream or file. is either or depending on the platform’s native byte order, while the others represent big endian (`_BE` suffix) and little endian (`_LE` suffix) byte order using 32-bit and 64-bit encodings.

</div>
# `codeop` — Compile Python code

*Compile (possibly incomplete) Python code.*\
The `codeop` module provides a function to compile Python code with hints on whether it is certainly complete, possibly complete or definitely incomplete. This is used by the `code` module and should not normally be used directly.

The `codeop` module defines the following function:

<div class="funcdesc">

compile_command source Tries to compile *source*, which should be a string of Python code and return a code object if *source* is valid Python code. In that case, the filename attribute of the code object will be *filename*, which defaults to `’<input>’`. Returns `None` if *source* is *not* valid Python code, but is a prefix of valid Python code.

If there is a problem with *source*, an exception will be raised. `SyntaxError` is raised if there is invalid Python syntax, and `OverflowError` if there is an invalid numeric constant.

The *symbol* argument determines whether *source* is compiled as a statement (`’single’`, the default) or as an expression (`’eval’`). Any other value will cause `ValueError` to be raised.

**Caveat:** It is possible (but not likely) that the parser stops parsing with a successful outcome before reaching the end of the source; in this case, trailing symbols may be ignored instead of causing an error. For example, a backslash followed by two newlines may be followed by arbitrary garbage. This will be fixed once the API for the parser is better.

</div>
# `colorsys` — Conversions between color systems

*Conversion functions between RGB and other color systems.*\
The `colorsys` module defines bidirectional conversions of color values between colors expressed in the RGB (Red Green Blue) color space used in computer monitors and three other coordinate systems: YIQ, HLS (Hue Lightness Saturation) and HSV (Hue Saturation Value). Coordinates in all of these color spaces are floating point values. In the YIQ space, the Y coordinate is between 0 and 1, but the I and Q coordinates can be positive or negative. In all other spaces, the coordinates are all between 0 and 1.

More information about color spaces can be found at `http://www.inforamp.net/%7epoynton/ColorFAQ.html`.

The `colorsys` module defines the following functions:

<div class="funcdesc">

rgb_to_yiqr, g, b Convert the color from RGB coordinates to YIQ coordinates.

</div>

<div class="funcdesc">

yiq_to_rgby, i, q Convert the color from YIQ coordinates to RGB coordinates.

</div>

<div class="funcdesc">

rgb_to_hlsr, g, b Convert the color from RGB coordinates to HLS coordinates.

</div>

<div class="funcdesc">

hls_to_rgbh, l, s Convert the color from HLS coordinates to RGB coordinates.

</div>

<div class="funcdesc">

rgb_to_hsvr, g, b Convert the color from RGB coordinates to HSV coordinates.

</div>

<div class="funcdesc">

hsv_to_rgbh, s, v Convert the color from HSV coordinates to RGB coordinates.

</div>

Example:

    >>> import colorsys
    >>> colorsys.rgb_to_hsv(.3, .4, .2)
    (0.25, 0.5, 0.4)
    >>> colorsys.hsv_to_rgb(0.25, 0.5, 0.4)
    (0.3, 0.4, 0.2)
# `commands` — Utilities for running commands

*Utility functions for running external commands.*\
The `commands` module contains wrapper functions for `os.popen()` which take a system command as a string and return any output generated by the command and, optionally, the exit status.

The `commands` module defines the following functions:

<div class="funcdesc">

getstatusoutputcmd Execute the string *cmd* in a shell with `os.popen()` and return a 2-tuple `(`*`status`*`, `*`output`*`)`. *cmd* is actually run as `{ `*`cmd`*` ; } 2>&1`, so that the returned output will contain output or error messages. A trailing newline is stripped from the output. The exit status for the command can be interpreted according to the rules for the C function .

</div>

<div class="funcdesc">

getoutputcmd Like `getstatusoutput()`, except the exit status is ignored and the return value is a string containing the command’s output.

</div>

<div class="funcdesc">

getstatusfile Return the output of `ls -ld `*`file`* as a string. This function uses the `getoutput()` function, and properly escapes backslashes and dollar signs in the argument.

</div>

Example:

    >>> import commands
    >>> commands.getstatusoutput('ls /bin/ls')
    (0, '/bin/ls')
    >>> commands.getstatusoutput('cat /bin/junk')
    (256, 'cat: /bin/junk: No such file or directory')
    >>> commands.getstatusoutput('/bin/junk')
    (256, 'sh: /bin/junk: not found')
    >>> commands.getoutput('ls /bin/ls')
    '/bin/ls'
    >>> commands.getstatus('/bin/ls')
    '-rwxr-xr-x  1 root        13352 Oct 14  1994 /bin/ls'
# `copy_reg` — Register `pickle` support functions

*Register `pickle` support functions.*\
The `copy_reg` module provides support for the `pickle`and `cPickle`modules. The `copy`module is likely to use this in the future as well. It provides configuration information about object constructors which are not classes. Such constructors may be factory functions or class instances.

<div class="funcdesc">

constructorobject Declares *object* to be a valid constructor.

</div>

<div class="funcdesc">

pickletype, function Declares that *function* should be used as a “reduction” function for objects of type or class *type*. *function* should return either a string or a tuple. The optional *constructor* parameter, if provided, is a callable object which can be used to reconstruct the object when called with the tuple of arguments returned by *function* at pickling time.

</div>
# `crypt` — Function to check Unix passwords

*The function used to check Unix passwords.*\
This module implements an interface to the routine, which is a one-way hash function based upon a modified DESalgorithm; see the Unix man page for further details. Possible uses include allowing Python scripts to accept typed passwords from the user, or attempting to crack Unix passwords with a dictionary.

<div class="funcdesc">

cryptword, salt *word* will usually be a user’s password as typed at a prompt or in a graphical interface. *salt* is usually a random two-character string which will be used to perturb the DES algorithm in one of 4096 ways. The characters in *salt* must be in the set . Returns the hashed password as a string, which will be composed of characters from the same alphabet as the salt (the first two characters represent the salt itself).

</div>

A simple example illustrating typical use:

    import crypt, getpass, pwd

    def login():
        username = raw_input('Python login:')
        cryptedpasswd = pwd.getpwnam(username)[1]
        if cryptedpasswd:
            if cryptedpasswd == 'x' or cryptedpasswd == '*': 
                raise "Sorry, currently no support for shadow passwords"
            cleartext = getpass.getpass()
            return crypt.crypt(cleartext, cryptedpasswd[:2]) == cryptedpasswd
        else:
            return 1
# Cryptographic Services

The modules described in this chapter implement various algorithms of a cryptographic nature. They are available at the discretion of the installation. Here’s an overview:

Hardcore cypherpunks will probably find the cryptographic modules written by Andrew Kuchling of further interest; the package adds built-in modules for DES and IDEA encryption, provides a Python module for reading and decrypting PGP files, and then some. These modules are not distributed with Python but available separately. See the URL `http://starship.python.net/crew/amk/python/code/crypto.html` or send email to `amk1@bigfoot.com` for more information.
# `dircache` — Cached directory listings

*Return directory listing, with cache mechanism.*\
The `dircache` module defines a function for reading directory listing using a cache, and cache invalidation using the *mtime* of the directory. Additionally, it defines a function to annotate directories by appending a slash.

The `dircache` module defines the following functions:

<div class="funcdesc">

listdirpath Return a directory listing of *path*, as gotten from `os.listdir()`. Note that unless *path* changes, further call to `listdir()` will not re-read the directory structure.

Note that the list returned should be regarded as read-only. (Perhaps a future version should change it to return a tuple?)

</div>

<div class="funcdesc">

opendirpath Same as `listdir()`. Defined for backwards compatibility.

</div>

<div class="funcdesc">

annotatehead, list Assume *list* is a list of paths relative to *head*, and append, in place, a to each path which points to a directory.

</div>

    >>> import dircache
    >>> a=dircache.listdir('/')
    >>> a=a[:] # Copy the return value so we can change 'a'
    >>> a
    ['bin', 'boot', 'cdrom', 'dev', 'etc', 'floppy', 'home', 'initrd', 'lib', 'lost+
    found', 'mnt', 'proc', 'root', 'sbin', 'tmp', 'usr', 'var', 'vmlinuz']
    >>> dircache.annotate('/', a)
    >>> a
    ['bin/', 'boot/', 'cdrom/', 'dev/', 'etc/', 'floppy/', 'home/', 'initrd/', 'lib/
    ', 'lost+found/', 'mnt/', 'proc/', 'root/', 'sbin/', 'tmp/', 'usr/', 'var/', 'vm
    linuz']
# `dis` — Disassembler.

*Disassembler.*\
The `dis` module supports the analysis of Python byte code by disassembling it. Since there is no Python assembler, this module defines the Python assembly language. The Python byte code which this module takes as an input is defined in the file `Include/opcode.h` and used by the compiler and the interpreter.

Example: Given the function `myfunc`:

    def myfunc(alist):
        return len(alist)

the following command can be used to get the disassembly of `myfunc()`:

    >>> dis.dis(myfunc)
              0 SET_LINENO          1

              3 SET_LINENO          2
              6 LOAD_GLOBAL         0 (len)
              9 LOAD_FAST           0 (alist)
             12 CALL_FUNCTION       1
             15 RETURN_VALUE   
             16 LOAD_CONST          0 (None)
             19 RETURN_VALUE   

The `dis` module defines the following functions:

<div class="funcdesc">

dis Disassemble the *bytesource* object. *bytesource* can denote either a class, a method, a function, or a code object. For a class, it disassembles all methods. For a single code sequence, it prints one line per byte code instruction. If no object is provided, it disassembles the last traceback.

</div>

<div class="funcdesc">

distb Disassembles the top-of-stack function of a traceback, using the last traceback if none was passed. The instruction causing the exception is indicated.

</div>

<div class="funcdesc">

disassemblecode Disassembles a code object, indicating the last instruction if *lasti* was provided. The output is divided in the following columns:

1.  the current instruction, indicated as `-->`,

2.  a labelled instruction, indicated with `>>`,

3.  the address of the instruction,

4.  the operation code name,

5.  operation parameters, and

6.  interpretation of the parameters in parentheses.

The parameter interpretation recognizes local and global variable names, constant values, branch targets, and compare operators.

</div>

<div class="funcdesc">

discocode A synonym for disassemble. It is more convenient to type, and kept for compatibility with earlier Python releases.

</div>

<div class="datadesc">

opname Sequence of a operation names, indexable using the byte code.

</div>

<div class="datadesc">

cmp_op Sequence of all compare operation names.

</div>

<div class="datadesc">

hasconst Sequence of byte codes that have a constant parameter.

</div>

<div class="datadesc">

hasname Sequence of byte codes that access a attribute by name.

</div>

<div class="datadesc">

hasjrel Sequence of byte codes that have a relative jump target.

</div>

<div class="datadesc">

hasjabs Sequence of byte codes that have an absolute jump target.

</div>

<div class="datadesc">

haslocal Sequence of byte codes that access a a local variable.

</div>

<div class="datadesc">

hascompare Sequence of byte codes of boolean operations.

</div>

## Python Byte Code Instructions

The Python compiler currently generates the following byte code instructions.

<div class="opcodedesc">

STOP_CODE Indicates end-of-code to the compiler, not used by the interpreter.

</div>

<div class="opcodedesc">

POP_TOP Removes the top-of-stack (TOS) item.

</div>

<div class="opcodedesc">

ROT_TWO Swaps the two top-most stack items.

</div>

<div class="opcodedesc">

ROT_THREE Lifts second and third stack item one position up, moves top down to position three.

</div>

<div class="opcodedesc">

ROT_FOUR Lifts second, third and forth stack item one position up, moves top down to position four.

</div>

<div class="opcodedesc">

DUP_TOP Duplicates the reference on top of the stack.

</div>

Unary Operations take the top of the stack, apply the operation, and push the result back on the stack.

<div class="opcodedesc">

UNARY_POSITIVE Implements `TOS = +TOS`.

</div>

<div class="opcodedesc">

UNARY_NEGATIVE Implements `TOS = -TOS`.

</div>

<div class="opcodedesc">

UNARY_NOT Implements `TOS = not TOS`.

</div>

<div class="opcodedesc">

UNARY_CONVERT Implements `TOS = ‘TOS‘`.

</div>

<div class="opcodedesc">

UNARY_INVERT Implements `TOS = ~TOS`.

</div>

Binary operations remove the top of the stack (TOS) and the second top-most stack item (TOS1) from the stack. They perform the operation, and put the result back on the stack.

<div class="opcodedesc">

BINARY_POWER Implements `TOS = TOS1 ** TOS`.

</div>

<div class="opcodedesc">

BINARY_MULTIPLY Implements `TOS = TOS1 * TOS`.

</div>

<div class="opcodedesc">

BINARY_DIVIDE Implements `TOS = TOS1 / TOS`.

</div>

<div class="opcodedesc">

BINARY_MODULO Implements `TOS = TOS1 % TOS`.

</div>

<div class="opcodedesc">

BINARY_ADD Implements `TOS = TOS1 + TOS`.

</div>

<div class="opcodedesc">

BINARY_SUBTRACT Implements `TOS = TOS1 - TOS`.

</div>

<div class="opcodedesc">

BINARY_SUBSCR Implements `TOS = TOS1[TOS]`.

</div>

<div class="opcodedesc">

BINARY_LSHIFT Implements `TOS = TOS1 << TOS`.

</div>

<div class="opcodedesc">

BINARY_RSHIFT Implements `TOS = TOS1 >> TOS`.

</div>

<div class="opcodedesc">

BINARY_AND Implements `TOS = TOS1 & TOS`.

</div>

<div class="opcodedesc">

BINARY_XOR Implements `TOS = TOS1  ̂TOS`.

</div>

<div class="opcodedesc">

BINARY_OR Implements `TOS = TOS1 | TOS`.

</div>

In-place operations are like binary operations, in that they remove TOS and TOS1, and push the result back on the stack, but the operation is done in-place when TOS1 supports it, and the resulting TOS may be (but does not have to be) the original TOS1.

<div class="opcodedesc">

INPLACE_POWER Implements in-place `TOS = TOS1 ** TOS`.

</div>

<div class="opcodedesc">

INPLACE_MULTIPLY Implements in-place `TOS = TOS1 * TOS`.

</div>

<div class="opcodedesc">

INPLACE_DIVIDE Implements in-place `TOS = TOS1 / TOS`.

</div>

<div class="opcodedesc">

INPLACE_MODULO Implements in-place `TOS = TOS1 % TOS`.

</div>

<div class="opcodedesc">

INPLACE_ADD Implements in-place `TOS = TOS1 + TOS`.

</div>

<div class="opcodedesc">

INPLACE_SUBTRACT Implements in-place `TOS = TOS1 - TOS`.

</div>

<div class="opcodedesc">

INPLACE_LSHIFT Implements in-place `TOS = TOS1 << TOS`.

</div>

<div class="opcodedesc">

INPLACE_RSHIFT Implements in-place `TOS = TOS1 >> TOS`.

</div>

<div class="opcodedesc">

INPLACE_AND Implements in-place `TOS = TOS1 & TOS`.

</div>

<div class="opcodedesc">

INPLACE_XOR Implements in-place `TOS = TOS1  ̂TOS`.

</div>

<div class="opcodedesc">

INPLACE_OR Implements in-place `TOS = TOS1 | TOS`.

</div>

The slice opcodes take up to three parameters.

<div class="opcodedesc">

SLICE+0 Implements `TOS = TOS[:]`.

</div>

<div class="opcodedesc">

SLICE+1 Implements `TOS = TOS1[TOS:]`.

</div>

<div class="opcodedesc">

SLICE+2 Implements `TOS = TOS1[:TOS1]`.

</div>

<div class="opcodedesc">

SLICE+3 Implements `TOS = TOS2[TOS1:TOS]`.

</div>

Slice assignment needs even an additional parameter. As any statement, they put nothing on the stack.

<div class="opcodedesc">

STORE_SLICE+0 Implements `TOS[:] = TOS1`.

</div>

<div class="opcodedesc">

STORE_SLICE+1 Implements `TOS1[TOS:] = TOS2`.

</div>

<div class="opcodedesc">

STORE_SLICE+2 Implements `TOS1[:TOS] = TOS2`.

</div>

<div class="opcodedesc">

STORE_SLICE+3 Implements `TOS2[TOS1:TOS] = TOS3`.

</div>

<div class="opcodedesc">

DELETE_SLICE+0 Implements `del TOS[:]`.

</div>

<div class="opcodedesc">

DELETE_SLICE+1 Implements `del TOS1[TOS:]`.

</div>

<div class="opcodedesc">

DELETE_SLICE+2 Implements `del TOS1[:TOS]`.

</div>

<div class="opcodedesc">

DELETE_SLICE+3 Implements `del TOS2[TOS1:TOS]`.

</div>

<div class="opcodedesc">

STORE_SUBSCR Implements `TOS1[TOS] = TOS2`.

</div>

<div class="opcodedesc">

DELETE_SUBSCR Implements `del TOS1[TOS]`.

</div>

<div class="opcodedesc">

PRINT_EXPR Implements the expression statement for the interactive mode. TOS is removed from the stack and printed. In non-interactive mode, an expression statement is terminated with `POP_STACK`.

</div>

<div class="opcodedesc">

PRINT_ITEM Prints TOS to the file-like object bound to `sys.stdout`. There is one such instruction for each item in the statement.

</div>

<div class="opcodedesc">

PRINT_ITEM_TO Like `PRINT_ITEM`, but prints the item second from TOS to the file-like object at TOS. This is used by the extended print statement.

</div>

<div class="opcodedesc">

PRINT_NEWLINE Prints a new line on `sys.stdout`. This is generated as the last operation of a statement, unless the statement ends with a comma.

</div>

<div class="opcodedesc">

PRINT_NEWLINE_TO Like `PRINT_NEWLINE`, but prints the new line on the file-like object on the TOS. This is used by the extended print statement.

</div>

<div class="opcodedesc">

BREAK_LOOP Terminates a loop due to a statement.

</div>

<div class="opcodedesc">

LOAD_LOCALS Pushes a reference to the locals of the current scope on the stack. This is used in the code for a class definition: After the class body is evaluated, the locals are passed to the class definition.

</div>

<div class="opcodedesc">

RETURN_VALUE Returns with TOS to the caller of the function.

</div>

<div class="opcodedesc">

IMPORT_STAR Loads all symbols not starting with directly from the module TOS to the local namespace. The module is popped after loading all names. This opcode implements `from module import *`.

</div>

<div class="opcodedesc">

EXEC_STMT Implements `exec TOS2,TOS1,TOS`. The compiler fills missing optional parameters with `None`.

</div>

<div class="opcodedesc">

POP_BLOCK Removes one block from the block stack. Per frame, there is a stack of blocks, denoting nested loops, try statements, and such.

</div>

<div class="opcodedesc">

END_FINALLY Terminates a clause. The interpreter recalls whether the exception has to be re-raised, or whether the function returns, and continues with the outer-next block.

</div>

<div class="opcodedesc">

BUILD_CLASS Creates a new class object. TOS is the methods dictionary, TOS1 the tuple of the names of the base classes, and TOS2 the class name.

</div>

All of the following opcodes expect arguments. An argument is two bytes, with the more significant byte last.

<div class="opcodedesc">

STORE_NAMEnamei Implements `name = TOS`. *namei* is the index of *name* in the attribute `co_names` of the code object. The compiler tries to use `STORE_LOCAL` or `STORE_GLOBAL` if possible.

</div>

<div class="opcodedesc">

DELETE_NAMEnamei Implements `del name`, where *namei* is the index into `co_names` attribute of the code object.

</div>

<div class="opcodedesc">

UNPACK_SEQUENCEcount Unpacks TOS into *count* individual values, which are put onto the stack right-to-left.

</div>

<div class="opcodedesc">

DUP_TOPXcount Duplicate *count* items, keeping them in the same order. Due to implementation limits, *count* should be between 1 and 5 inclusive.

</div>

<div class="opcodedesc">

STORE_ATTRnamei Implements `TOS.name = TOS1`, where *namei* is the index of name in `co_names`.

</div>

<div class="opcodedesc">

DELETE_ATTRnamei Implements `del TOS.name`, using *namei* as index into `co_names`.

</div>

<div class="opcodedesc">

STORE_GLOBALnamei Works as `STORE_NAME`, but stores the name as a global.

</div>

<div class="opcodedesc">

DELETE_GLOBALnamei Works as `DELETE_NAME`, but deletes a global name.

</div>

<div class="opcodedesc">

LOAD_CONSTconsti Pushes `co_consts[`*`consti`*`]` onto the stack.

</div>

<div class="opcodedesc">

LOAD_NAMEnamei Pushes the value associated with `co_names[`*`namei`*`]` onto the stack.

</div>

<div class="opcodedesc">

BUILD_TUPLEcount Creates a tuple consuming *count* items from the stack, and pushes the resulting tuple onto the stack.

</div>

<div class="opcodedesc">

BUILD_LISTcount Works as `BUILD_TUPLE`, but creates a list.

</div>

<div class="opcodedesc">

BUILD_MAPzero Pushes a new empty dictionary object onto the stack. The argument is ignored and set to zero by the compiler.

</div>

<div class="opcodedesc">

LOAD_ATTRnamei Replaces TOS with `getattr(TOS, co_names[`*`namei`*`]`.

</div>

<div class="opcodedesc">

COMPARE_OPopname Performs a boolean operation. The operation name can be found in `cmp_op[`*`opname`*`]`.

</div>

<div class="opcodedesc">

IMPORT_NAMEnamei Imports the module `co_names[`*`namei`*`]`. The module object is pushed onto the stack. The current namespace is not affected: for a proper import statement, a subsequent `STORE_FAST` instruction modifies the namespace.

</div>

<div class="opcodedesc">

IMPORT_FROMnamei Loads the attribute `co_names[`*`namei`*`]` from the module found in TOS. The resulting object is pushed onto the stack, to be subsequently stored by a `STORE_FAST` instruction.

</div>

<div class="opcodedesc">

JUMP_FORWARDdelta Increments byte code counter by *delta*.

</div>

<div class="opcodedesc">

JUMP_IF_TRUEdelta If TOS is true, increment the byte code counter by *delta*. TOS is left on the stack.

</div>

<div class="opcodedesc">

JUMP_IF_FALSEdelta If TOS is false, increment the byte code counter by *delta*. TOS is not changed.

</div>

<div class="opcodedesc">

JUMP_ABSOLUTEtarget Set byte code counter to *target*.

</div>

<div class="opcodedesc">

FOR_LOOPdelta Iterate over a sequence. TOS is the current index, TOS1 the sequence. First, the next element is computed. If the sequence is exhausted, increment byte code counter by *delta*. Otherwise, push the sequence, the incremented counter, and the current item onto the stack.

</div>

<div class="opcodedesc">

LOAD_GLOBALnamei Loads the global named `co_names[`*`namei`*`]` onto the stack.

</div>

<div class="opcodedesc">

SETUP_LOOPdelta Pushes a block for a loop onto the block stack. The block spans from the current instruction with a size of *delta* bytes.

</div>

<div class="opcodedesc">

SETUP_EXCEPTdelta Pushes a try block from a try-except clause onto the block stack. *delta* points to the first except block.

</div>

<div class="opcodedesc">

SETUP_FINALLYdelta Pushes a try block from a try-except clause onto the block stack. *delta* points to the finally block.

</div>

<div class="opcodedesc">

LOAD_FASTvar_num Pushes a reference to the local `co_varnames[`*`var_num`*`]` onto the stack.

</div>

<div class="opcodedesc">

STORE_FASTvar_num Stores TOS into the local `co_varnames[`*`var_num`*`]`.

</div>

<div class="opcodedesc">

DELETE_FASTvar_num Deletes local `co_varnames[`*`var_num`*`]`.

</div>

<div class="opcodedesc">

SET_LINENOlineno Sets the current line number to *lineno*.

</div>

<div class="opcodedesc">

RAISE_VARARGSargc Raises an exception. *argc* indicates the number of parameters to the raise statement, ranging from 0 to 3. The handler will find the traceback as TOS2, the parameter as TOS1, and the exception as TOS.

</div>

<div class="opcodedesc">

CALL_FUNCTIONargc Calls a function. The low byte of *argc* indicates the number of positional parameters, the high byte the number of keyword parameters. On the stack, the opcode finds the keyword parameters first. For each keyword argument, the value is on top of the key. Below the keyword parameters, the positional parameters are on the stack, with the right-most parameter on top. Below the parameters, the function object to call is on the stack.

</div>

<div class="opcodedesc">

MAKE_FUNCTIONargc Pushes a new function object on the stack. TOS is the code associated with the function. The function object is defined to have *argc* default parameters, which are found below TOS.

</div>

<div class="opcodedesc">

BUILD_SLICEargc Pushes a slice object on the stack. *argc* must be 2 or 3. If it is 2, `slice(TOS1, TOS)` is pushed; if it is 3, `slice(TOS2, TOS1, TOS)` is pushed. See the `slice()`built-in function for more information.

</div>

<div class="opcodedesc">

EXTENDED_ARGext Prefixes any opcode which has an argument too big to fit into the default two bytes. *ext* holds two additional bytes which, taken together with the subsequent opcode’s argument, comprise a four-byte argument, *ext* being the two most-significant bytes.

</div>

<div class="opcodedesc">

CALL_FUNCTION_VARargc Calls a function. *argc* is interpreted as in `CALL_FUNCTION`. The top element on the stack contains the variable argument list, followed by keyword and positional arguments.

</div>

<div class="opcodedesc">

CALL_FUNCTION_KWargc Calls a function. *argc* is interpreted as in `CALL_FUNCTION`. The top element on the stack contains the keyword arguments dictionary, followed by explicit keyword and positional arguments.

</div>

<div class="opcodedesc">

CALL_FUNCTION_VAR_KWargc Calls a function. *argc* is interpreted as in `CALL_FUNCTION`. The top element on the stack contains the keyword arguments dictionary, followed by the variable-arguments tuple, followed by explicit keyword and positional arguments.

</div>
# `dl` — Call C functions in shared objects

*Call C functions in shared objects.*\
The `dl` module defines an interface to the function, which is the most common interface on Unix platforms for handling dynamically linked libraries. It allows the program to call arbitrary functions in such a library.

**Note:** This module will not work unless

    sizeof(int) == sizeof(long) == sizeof(char *)

If this is not the case, `SystemError` will be raised on import.

The `dl` module defines the following function:

<div class="funcdesc">

openname Open a shared object file, and return a handle. Mode signifies late binding () or immediate binding (). Default is . Note that some systems do not support .

Return value is a .

</div>

The `dl` module defines the following constants:

<div class="datadesc">

RTLD_LAZY Useful as an argument to `open()`.

</div>

<div class="datadesc">

RTLD_NOW Useful as an argument to `open()`. Note that on systems which do not support immediate binding, this constant will not appear in the module. For maximum portability, use `hasattr()` to determine if the system supports immediate binding.

</div>

The `dl` module defines the following exception:

<div class="excdesc">

error Exception raised when an error has occurred inside the dynamic loading and linking routines.

</div>

Example:

    >>> import dl, time
    >>> a=dl.open('/lib/libc.so.6')
    >>> a.call('time'), time.time()
    (929723914, 929723914.498)

This example was tried on a Debian GNU/Linux system, and is a good example of the fact that using this module is usually a bad alternative.

## Dl Objects <span id="dl-objects" label="dl-objects"></span>

Dl objects, as returned by `open()` above, have the following methods:

<div class="methoddesc">

close Free all resources, except the memory.

</div>

<div class="methoddesc">

symname Return the pointer for the function named *name*, as a number, if it exists in the referenced shared object, otherwise `None`. This is useful in code like:

    >>> if a.sym('time'): 
    ...     a.call('time')
    ... else: 
    ...     time.time()

(Note that this function will return a non-zero number, as zero is the NULL pointer)

</div>

<div class="methoddesc">

callname Call the function named *name* in the referenced shared object. The arguments must be either Python integers, which will be passed as is, Python strings, to which a pointer will be passed, or `None`, which will be passed as NULL. Note that strings should only be passed to functions as `const char*`, as Python will not like its string mutated.

There must be at most 10 arguments, and arguments not given will be treated as `None`. The function’s return value must be a C `long`, which is a Python integer.

</div>
# `errno` — Standard errno system symbols.

*Standard errno system symbols.*\
This module makes available standard errno system symbols. The value of each symbol is the corresponding integer value. The names and descriptions are borrowed from `linux/include/errno.h`, which should be pretty all-inclusive.

<div class="datadesc">

errorcode Dictionary providing a mapping from the errno value to the string name in the underlying system. For instance, `errno.errorcode[errno.EPERM]` maps to `’EPERM’`.

</div>

To translate a numeric error code to an error message, use `os.strerror()`.

Of the following list, symbols that are not used on the current platform are not defined by the module. Symbols available can include:

<div class="datadesc">

EPERM Operation not permitted

</div>

<div class="datadesc">

ENOENT No such file or directory

</div>

<div class="datadesc">

ESRCH No such process

</div>

<div class="datadesc">

EINTR Interrupted system call

</div>

<div class="datadesc">

EIO I/O error

</div>

<div class="datadesc">

ENXIO No such device or address

</div>

<div class="datadesc">

E2BIG Arg list too long

</div>

<div class="datadesc">

ENOEXEC Exec format error

</div>

<div class="datadesc">

EBADF Bad file number

</div>

<div class="datadesc">

ECHILD No child processes

</div>

<div class="datadesc">

EAGAIN Try again

</div>

<div class="datadesc">

ENOMEM Out of memory

</div>

<div class="datadesc">

EACCES Permission denied

</div>

<div class="datadesc">

EFAULT Bad address

</div>

<div class="datadesc">

ENOTBLK Block device required

</div>

<div class="datadesc">

EBUSY Device or resource busy

</div>

<div class="datadesc">

EEXIST File exists

</div>

<div class="datadesc">

EXDEV Cross-device link

</div>

<div class="datadesc">

ENODEV No such device

</div>

<div class="datadesc">

ENOTDIR Not a directory

</div>

<div class="datadesc">

EISDIR Is a directory

</div>

<div class="datadesc">

EINVAL Invalid argument

</div>

<div class="datadesc">

ENFILE File table overflow

</div>

<div class="datadesc">

EMFILE Too many open files

</div>

<div class="datadesc">

ENOTTY Not a typewriter

</div>

<div class="datadesc">

ETXTBSY Text file busy

</div>

<div class="datadesc">

EFBIG File too large

</div>

<div class="datadesc">

ENOSPC No space left on device

</div>

<div class="datadesc">

ESPIPE Illegal seek

</div>

<div class="datadesc">

EROFS Read-only file system

</div>

<div class="datadesc">

EMLINK Too many links

</div>

<div class="datadesc">

EPIPE Broken pipe

</div>

<div class="datadesc">

EDOM Math argument out of domain of func

</div>

<div class="datadesc">

ERANGE Math result not representable

</div>

<div class="datadesc">

EDEADLK Resource deadlock would occur

</div>

<div class="datadesc">

ENAMETOOLONG File name too long

</div>

<div class="datadesc">

ENOLCK No record locks available

</div>

<div class="datadesc">

ENOSYS Function not implemented

</div>

<div class="datadesc">

ENOTEMPTY Directory not empty

</div>

<div class="datadesc">

ELOOP Too many symbolic links encountered

</div>

<div class="datadesc">

EWOULDBLOCK Operation would block

</div>

<div class="datadesc">

ENOMSG No message of desired type

</div>

<div class="datadesc">

EIDRM Identifier removed

</div>

<div class="datadesc">

ECHRNG Channel number out of range

</div>

<div class="datadesc">

EL2NSYNC Level 2 not synchronized

</div>

<div class="datadesc">

EL3HLT Level 3 halted

</div>

<div class="datadesc">

EL3RST Level 3 reset

</div>

<div class="datadesc">

ELNRNG Link number out of range

</div>

<div class="datadesc">

EUNATCH Protocol driver not attached

</div>

<div class="datadesc">

ENOCSI No CSI structure available

</div>

<div class="datadesc">

EL2HLT Level 2 halted

</div>

<div class="datadesc">

EBADE Invalid exchange

</div>

<div class="datadesc">

EBADR Invalid request descriptor

</div>

<div class="datadesc">

EXFULL Exchange full

</div>

<div class="datadesc">

ENOANO No anode

</div>

<div class="datadesc">

EBADRQC Invalid request code

</div>

<div class="datadesc">

EBADSLT Invalid slot

</div>

<div class="datadesc">

EDEADLOCK File locking deadlock error

</div>

<div class="datadesc">

EBFONT Bad font file format

</div>

<div class="datadesc">

ENOSTR Device not a stream

</div>

<div class="datadesc">

ENODATA No data available

</div>

<div class="datadesc">

ETIME Timer expired

</div>

<div class="datadesc">

ENOSR Out of streams resources

</div>

<div class="datadesc">

ENONET Machine is not on the network

</div>

<div class="datadesc">

ENOPKG Package not installed

</div>

<div class="datadesc">

EREMOTE Object is remote

</div>

<div class="datadesc">

ENOLINK Link has been severed

</div>

<div class="datadesc">

EADV Advertise error

</div>

<div class="datadesc">

ESRMNT Srmount error

</div>

<div class="datadesc">

ECOMM Communication error on send

</div>

<div class="datadesc">

EPROTO Protocol error

</div>

<div class="datadesc">

EMULTIHOP Multihop attempted

</div>

<div class="datadesc">

EDOTDOT RFS specific error

</div>

<div class="datadesc">

EBADMSG Not a data message

</div>

<div class="datadesc">

EOVERFLOW Value too large for defined data type

</div>

<div class="datadesc">

ENOTUNIQ Name not unique on network

</div>

<div class="datadesc">

EBADFD File descriptor in bad state

</div>

<div class="datadesc">

EREMCHG Remote address changed

</div>

<div class="datadesc">

ELIBACC Can not access a needed shared library

</div>

<div class="datadesc">

ELIBBAD Accessing a corrupted shared library

</div>

<div class="datadesc">

ELIBSCN .lib section in a.out corrupted

</div>

<div class="datadesc">

ELIBMAX Attempting to link in too many shared libraries

</div>

<div class="datadesc">

ELIBEXEC Cannot exec a shared library directly

</div>

<div class="datadesc">

EILSEQ Illegal byte sequence

</div>

<div class="datadesc">

ERESTART Interrupted system call should be restarted

</div>

<div class="datadesc">

ESTRPIPE Streams pipe error

</div>

<div class="datadesc">

EUSERS Too many users

</div>

<div class="datadesc">

ENOTSOCK Socket operation on non-socket

</div>

<div class="datadesc">

EDESTADDRREQ Destination address required

</div>

<div class="datadesc">

EMSGSIZE Message too long

</div>

<div class="datadesc">

EPROTOTYPE Protocol wrong type for socket

</div>

<div class="datadesc">

ENOPROTOOPT Protocol not available

</div>

<div class="datadesc">

EPROTONOSUPPORT Protocol not supported

</div>

<div class="datadesc">

ESOCKTNOSUPPORT Socket type not supported

</div>

<div class="datadesc">

EOPNOTSUPP Operation not supported on transport endpoint

</div>

<div class="datadesc">

EPFNOSUPPORT Protocol family not supported

</div>

<div class="datadesc">

EAFNOSUPPORT Address family not supported by protocol

</div>

<div class="datadesc">

EADDRINUSE Address already in use

</div>

<div class="datadesc">

EADDRNOTAVAIL Cannot assign requested address

</div>

<div class="datadesc">

ENETDOWN Network is down

</div>

<div class="datadesc">

ENETUNREACH Network is unreachable

</div>

<div class="datadesc">

ENETRESET Network dropped connection because of reset

</div>

<div class="datadesc">

ECONNABORTED Software caused connection abort

</div>

<div class="datadesc">

ECONNRESET Connection reset by peer

</div>

<div class="datadesc">

ENOBUFS No buffer space available

</div>

<div class="datadesc">

EISCONN Transport endpoint is already connected

</div>

<div class="datadesc">

ENOTCONN Transport endpoint is not connected

</div>

<div class="datadesc">

ESHUTDOWN Cannot send after transport endpoint shutdown

</div>

<div class="datadesc">

ETOOMANYREFS Too many references: cannot splice

</div>

<div class="datadesc">

ETIMEDOUT Connection timed out

</div>

<div class="datadesc">

ECONNREFUSED Connection refused

</div>

<div class="datadesc">

EHOSTDOWN Host is down

</div>

<div class="datadesc">

EHOSTUNREACH No route to host

</div>

<div class="datadesc">

EALREADY Operation already in progress

</div>

<div class="datadesc">

EINPROGRESS Operation now in progress

</div>

<div class="datadesc">

ESTALE Stale NFS file handle

</div>

<div class="datadesc">

EUCLEAN Structure needs cleaning

</div>

<div class="datadesc">

ENOTNAM Not a XENIX named type file

</div>

<div class="datadesc">

ENAVAIL No XENIX semaphores available

</div>

<div class="datadesc">

EISNAM Is a named type file

</div>

<div class="datadesc">

EREMOTEIO Remote I/O error

</div>

<div class="datadesc">

EDQUOT Quota exceeded

</div>
# Built-in Exceptions

*Standard exceptions classes.*\
Exceptions can be class objects or string objects. Though most exceptions have been string objects in past versions of Python, in Python 1.5 and newer versions, all standard exceptions have been converted to class objects, and users are encouraged to do the same. The exceptions are defined in the module `exceptions`. This module never needs to be imported explicitly: the exceptions are provided in the built-in namespace.

Two distinct string objects with the same value are considered different exceptions. This is done to force programmers to use exception names rather than their string value when specifying exception handlers. The string value of all built-in exceptions is their name, but this is not a requirement for user-defined exceptions or exceptions defined by library modules.

For class exceptions, in a statement with an clause that mentions a particular class, that clause also handles any exception classes derived from that class (but not exception classes from which *it* is derived). Two exception classes that are not related via subclassing are never equivalent, even if they have the same name.

The built-in exceptions listed below can be generated by the interpreter or built-in functions. Except where mentioned, they have an “associated value” indicating the detailed cause of the error. This may be a string or a tuple containing several items of information (e.g., an error code and a string explaining the code). The associated value is the second argument to the statement. For string exceptions, the associated value itself will be stored in the variable named as the second argument of the clause (if any). For class exceptions, that variable receives the exception instance. If the exception class is derived from the standard root class `Exception`, the associated value is present as the exception instance’s `args` attribute, and possibly on other attributes as well.

User code can raise built-in exceptions. This can be used to test an exception handler or to report an error condition “just like” the situation in which the interpreter raises the same exception; but beware that there is nothing to prevent user code from raising an inappropriate error.

The following exceptions are only used as base classes for other exceptions.

<div class="excdesc">

Exception The root class for exceptions. All built-in exceptions are derived from this class. All user-defined exceptions should also be derived from this class, but this is not (yet) enforced. The `str()` function, when applied to an instance of this class (or most derived classes) returns the string value of the argument or arguments, or an empty string if no arguments were given to the constructor. When used as a sequence, this accesses the arguments given to the constructor (handy for backward compatibility with old code). The arguments are also available on the instance’s `args` attribute, as a tuple.

</div>

<div class="excdesc">

StandardError The base class for all built-in exceptions except `SystemExit`. `StandardError` itself is derived from the root class `Exception`.

</div>

<div class="excdesc">

ArithmeticError The base class for those built-in exceptions that are raised for various arithmetic errors: `OverflowError`, `ZeroDivisionError`, `FloatingPointError`.

</div>

<div class="excdesc">

LookupError The base class for the exceptions that are raised when a key or index used on a mapping or sequence is invalid: `IndexError`, `KeyError`.

</div>

<div class="excdesc">

EnvironmentError The base class for exceptions that can occur outside the Python system: `IOError`, `OSError`. When exceptions of this type are created with a 2-tuple, the first item is available on the instance’s `errno` attribute (it is assumed to be an error number), and the second item is available on the `strerror` attribute (it is usually the associated error message). The tuple itself is also available on the `args` attribute. *New in version 1.5.2.*

When an `EnvironmentError` exception is instantiated with a 3-tuple, the first two items are available as above, while the third item is available on the `filename` attribute. However, for backwards compatibility, the `args` attribute contains only a 2-tuple of the first two constructor arguments.

The `filename` attribute is `None` when this exception is created with other than 3 arguments. The `errno` and `strerror` attributes are also `None` when the instance was created with other than 2 or 3 arguments. In this last case, `args` contains the verbatim constructor arguments as a tuple.

</div>

The following exceptions are the exceptions that are actually raised.

<div class="excdesc">

AssertionError Raised when an statement fails.

</div>

<div class="excdesc">

AttributeError

Raised when an attribute reference or assignment fails. (When an object does not support attribute references or attribute assignments at all, `TypeError` is raised.)

</div>

<div class="excdesc">

EOFError

Raised when one of the built-in functions (`input()` or `raw_input()`) hits an end-of-file condition (EOF) without reading any data.

(N.B.: the `read()` and `readline()` methods of file objects return an empty string when they hit EOF.)

</div>

<div class="excdesc">

FloatingPointError Raised when a floating point operation fails. This exception is always defined, but can only be raised when Python is configured with the `--with-fpectl` option, or the symbol is defined in the `config.h` file.

</div>

<div class="excdesc">

IOError

Raised when an I/O operation (such as a statement, the built-in `open()` function or a method of a file object) fails for an I/O-related reason, e.g., “file not found” or “disk full”.

This class is derived from `EnvironmentError`. See the discussion above for more information on exception instance attributes.

</div>

<div class="excdesc">

ImportError

Raised when an statement fails to find the module definition or when a `from `<span class="roman">`…`</span>` import` fails to find a name that is to be imported.

</div>

<div class="excdesc">

IndexError

Raised when a sequence subscript is out of range. (Slice indices are silently truncated to fall in the allowed range; if an index is not a plain integer, `TypeError` is raised.)

</div>

<div class="excdesc">

KeyError

Raised when a mapping (dictionary) key is not found in the set of existing keys.

</div>

<div class="excdesc">

KeyboardInterrupt Raised when the user hits the interrupt key (normally `Control-C` or `DEL`). During execution, a check for interrupts is made regularly.

Interrupts typed when a built-in function `input()` or `raw_input()`) is waiting for input also raise this exception.

</div>

<div class="excdesc">

MemoryError Raised when an operation runs out of memory but the situation may still be rescued (by deleting some objects). The associated value is a string indicating what kind of (internal) operation ran out of memory. Note that because of the underlying memory management architecture (C’s function), the interpreter may not always be able to completely recover from this situation; it nevertheless raises an exception so that a stack traceback can be printed, in case a run-away program was the cause.

</div>

<div class="excdesc">

NameError Raised when a local or global name is not found. This applies only to unqualified names. The associated value is the name that could not be found.

</div>

<div class="excdesc">

NotImplementedError This exception is derived from `RuntimeError`. In user defined base classes, abstract methods should raise this exception when they require derived classes to override the method. *New in version 1.5.2.*

</div>

<div class="excdesc">

OSError

This class is derived from `EnvironmentError` and is used primarily as the `os` module’s `os.error` exception. See `EnvironmentError` above for a description of the possible associated values. *New in version 1.5.2.*

</div>

<div class="excdesc">

OverflowError

Raised when the result of an arithmetic operation is too large to be represented. This cannot occur for long integers (which would rather raise `MemoryError` than give up). Because of the lack of standardization of floating point exception handling in C, most floating point operations also aren’t checked. For plain integers, all operations that can overflow are checked except left shift, where typical applications prefer to drop bits than raise an exception.

</div>

<div class="excdesc">

RuntimeError Raised when an error is detected that doesn’t fall in any of the other categories. The associated value is a string indicating what precisely went wrong. (This exception is mostly a relic from a previous version of the interpreter; it is not used very much any more.)

</div>

<div class="excdesc">

SyntaxError

Raised when the parser encounters a syntax error. This may occur in an statement, in an statement, in a call to the built-in function `eval()` or `input()`, or when reading the initial script or standard input (also interactively).

When class exceptions are used, instances of this class have atttributes `filename`, `lineno`, `offset` and `text` for easier access to the details; for string exceptions, the associated value is usually a tuple of the form `(message, (filename, lineno, offset, text))`. For class exceptions, `str()` returns only the message.

</div>

<div class="excdesc">

SystemError Raised when the interpreter finds an internal error, but the situation does not look so serious to cause it to abandon all hope. The associated value is a string indicating what went wrong (in low-level terms).

You should report this to the author or maintainer of your Python interpreter. Be sure to report the version string of the Python interpreter (`sys.version`; it is also printed at the start of an interactive Python session), the exact error message (the exception’s associated value) and if possible the source of the program that triggered the error.

</div>

<div class="excdesc">

SystemExit

This exception is raised by the `sys.exit()` function. When it is not handled, the Python interpreter exits; no stack traceback is printed. If the associated value is a plain integer, it specifies the system exit status (passed to C’s function); if it is `None`, the exit status is zero; if it has another type (such as a string), the object’s value is printed and the exit status is one.

Instances have an attribute `code` which is set to the proposed exit status or error message (defaulting to `None`). Also, this exception derives directly from `Exception` and not `StandardError`, since it is not technically an error.

A call to `sys.exit()` is translated into an exception so that clean-up handlers ( clauses of statements) can be executed, and so that a debugger can execute a script without running the risk of losing control. The `os._exit()` function can be used if it is absolutely positively necessary to exit immediately (e.g., after a `fork()` in the child process).

</div>

<div class="excdesc">

TypeError Raised when a built-in operation or function is applied to an object of inappropriate type. The associated value is a string giving details about the type mismatch.

</div>

<div class="excdesc">

UnboundLocalError Raised when a reference is made to a local variable in a function or method, but no value has been bound to that variable. This is a subclass of `NameError`. *New in version 2.0.*

</div>

<div class="excdesc">

UnicodeError Raised when a Unicode-related encoding or decoding error occurs. It is a subclass of `ValueError`. *New in version 2.0.*

</div>

<div class="excdesc">

ValueError Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value, and the situation is not described by a more precise exception such as `IndexError`.

</div>

<div class="excdesc">

WindowsError Raised when a Windows-specific error occurs or when the error number does not correspond to an value. The `errno` and `strerror` values are created from the return values of the and functions from the Windows Platform API. This is a subclass of `OSError`. *New in version 2.0.*

</div>

<div class="excdesc">

ZeroDivisionError Raised when the second argument of a division or modulo operation is zero. The associated value is a string indicating the type of the operands and the operation.

</div>
# `fcntl` — The `fcntl()` and `ioctl()` system calls

*The `fcntl()` and `ioctl()` system calls.*\
This module performs file control and I/O control on file descriptors. It is an interface to the and Unix routines. File descriptors can be obtained with the `fileno()` method of a file or socket object.

The module defines the following functions:

<div class="funcdesc">

fcntlfd, op Perform the requested operation on file descriptor *fd*. The operation is defined by *op* and is operating system dependent. Typically these codes can be retrieved from the library module `FCNTL`. The argument *arg* is optional, and defaults to the integer value `0`. When present, it can either be an integer value, or a string. With the argument missing or an integer value, the return value of this function is the integer return value of the C call. When the argument is a string it represents a binary structure, e.g. created by `struct.pack()`. The binary data is copied to a buffer whose address is passed to the C call. The return value after a successful call is the contents of the buffer, converted to a string object. The length of the returned string will be the same as the length of the *arg* argument. This is limited to 1024 bytes. If the information returned in the buffer by the operating system is larger than 1024 bytes, this is most likely to result in a segmentation violation or a more subtle data corruption.

If the fails, an `IOError` is raised.

</div>

<div class="funcdesc">

ioctlfd, op, arg This function is identical to the `fcntl()` function, except that the operations are typically defined in the library module `IOCTL`.

</div>

<div class="funcdesc">

flockfd, op Perform the lock operation *op* on file descriptor *fd*. See the Unix manual for details. (On some systems, this function is emulated using .)

</div>

<div class="funcdesc">

lockffd, code, This is a wrapper around the and `fcntl()` calls. See the Unix manual for details.

</div>

If the library modules `FCNTL`or `IOCTL`are missing, you can find the opcodes in the C include files `<sys/fcntl.h>` and `<sys/ioctl.h>`. You can create the modules yourself with the script, found in the `Tools/scripts/` directory.

Examples (all on a SVR4 compliant system):

    import struct, fcntl, FCNTL

    file = open(...)
    rv = fcntl(file.fileno(), FCNTL.O_NDELAY, 1)

    lockdata = struct.pack('hhllhh', FCNTL.F_WRLCK, 0, 0, 0, 0, 0)
    rv = fcntl.fcntl(file.fileno(), FCNTL.F_SETLKW, lockdata)

Note that in the first example the return value variable `rv` will hold an integer value; in the second example it will hold a string value. The structure lay-out for the *lockdata* variable is system dependent — therefore using the `flock()` call may be better.
# `filecmp` — File and Directory Comparisons

*Compare files efficiently.*\
The `filecmp` module defines functions to compare files and directories, with various optional time/correctness trade-offs.

The `filecmp` module defines the following function:

<div class="funcdesc">

cmpf1, f2 Compare the files named *f1* and *f2*, returning `1` if they seem equal, `0` otherwise.

Unless *shallow* is given and is false, files with identical `os.stat()` signatures are taken to be equal. If *use_statcache* is given and is true, `statcache.stat()` will be called rather then `os.stat()`; the default is to use `os.stat()`.

Files that were compared using this function will not be compared again unless their `os.stat()` signature changes. Note that using *use_statcache* true will cause the cache invalidation mechanism to fail — the stale stat value will be used from `statcache`’s cache.

Note that no external programs are called from this function, giving it portability and efficiency.

</div>

<div class="funcdesc">

cmpfilesdir1, dir2, common Returns three lists of file names: *match*, *mismatch*, *errors*. *match* contains the list of files match in both directories, *mismatch* includes the names of those that don’t, and *errros* lists the names of files which could not be compared. Files may be listed in *errors* because the user may lack permission to read them or many other reasons, but always that the comparison could not be done for some reason.

The *shallow* and *use_statcache* parameters have the same meanings and default values as for `filecmp.cmp()`.

</div>

Example:

    >>> import filecmp
    >>> filecmp.cmp('libundoc.tex', 'libundoc.tex')
    1
    >>> filecmp.cmp('libundoc.tex', 'lib.tex')
    0

## The `dircmp` class <span id="dircmp-objects" label="dircmp-objects"></span>

<div class="classdesc">

dircmpa, b Construct a new directory comparison object, to compare the directories *a* and *b*. *ignore* is a list of names to ignore, and defaults to `[’RCS’, ’CVS’, ’tags’]`. *hide* is a list of names to hid, and defaults to `[os.curdir, os.pardir]`.

</div>

<div class="methoddesc">

report Print (to `sys.stdout`) a comparison between *a* and *b*.

</div>

<div class="methoddesc">

report_partial_closure Print a comparison between *a* and *b* and common immediate subdirctories.

</div>

<div class="methoddesc">

report_full_closure Print a comparison between *a* and *b* and common subdirctories (recursively).

</div>

<div class="memberdesc">

left_list Files and subdirectories in *a*, filtered by *hide* and *ignore*.

</div>

<div class="memberdesc">

right_list Files and subdirectories in *b*, filtered by *hide* and *ignore*.

</div>

<div class="memberdesc">

common Files and subdirectories in both *a* and *b*.

</div>

<div class="memberdesc">

left_only Files and subdirectories only in *a*.

</div>

<div class="memberdesc">

right_only Files and subdirectories only in *b*.

</div>

<div class="memberdesc">

common_dirs Subdirectories in both *a* and *b*.

</div>

<div class="memberdesc">

common_files Files in both *a* and *b*

</div>

<div class="memberdesc">

common_funny Names in both *a* and *b*, such that the type differs between the directories, or names for which `os.stat()` reports an error.

</div>

<div class="memberdesc">

same_files Files which are identical in both *a* and *b*.

</div>

<div class="memberdesc">

diff_files Files which are in both *a* and *b*, whose contents differ.

</div>

<div class="memberdesc">

funny_files Files which are in both *a* and *b*, but could not be compared.

</div>

<div class="memberdesc">

subdirs A dictionary mapping names in `common_dirs` to `dircmp` objects.

</div>

Note that via `__getattr__()` hooks, all attributes are computed lazilly, so there is no speed penalty if only those attributes which are lightweight to compute are used.
# `fileinput` — Iterate over lines from multiple input streams

*Perl-like iteration over lines from multiple input streams, with “save in place” capability.*\
This module implements a helper class and functions to quickly write a loop over standard input or a list of files.

The typical use is:

    import fileinput
    for line in fileinput.input():
        process(line)

This iterates over the lines of all files listed in `sys.argv[1:]`, defaulting to `sys.stdin` if the list is empty. If a filename is `’-’`, it is also replaced by `sys.stdin`. To specify an alternative list of filenames, pass it as the first argument to `input()`. A single file name is also allowed.

All files are opened in text mode. If an I/O error occurs during opening or reading a file, `IOError` is raised.

If `sys.stdin` is used more than once, the second and further use will return no lines, except perhaps for interactive use, or if it has been explicitly reset (e.g. using `sys.stdin.seek(0)`).

Empty files are opened and immediately closed; the only time their presence in the list of filenames is noticeable at all is when the last file opened is empty.

It is possible that the last line of a file does not end in a newline character; lines are returned including the trailing newline when it is present.

The following function is the primary interface of this module:

<div class="funcdesc">

input Create an instance of the `FileInput` class. The instance will be used as global state for the functions of this module, and is also returned to use during iteration.

</div>

The following functions use the global state created by `input()`; if there is no active state, `RuntimeError` is raised.

<div class="funcdesc">

filename Return the name of the file currently being read. Before the first line has been read, returns `None`.

</div>

<div class="funcdesc">

lineno Return the cumulative line number of the line that has just been read. Before the first line has been read, returns `0`. After the last line of the last file has been read, returns the line number of that line.

</div>

<div class="funcdesc">

filelineno Return the line number in the current file. Before the first line has been read, returns `0`. After the last line of the last file has been read, returns the line number of that line within the file.

</div>

<div class="funcdesc">

isfirstline Returns true the line just read is the first line of its file, otherwise returns false.

</div>

<div class="funcdesc">

isstdin Returns true if the last line was read from `sys.stdin`, otherwise returns false.

</div>

<div class="funcdesc">

nextfile Close the current file so that the next iteration will read the first line from the next file (if any); lines not read from the file will not count towards the cumulative line count. The filename is not changed until after the first line of the next file has been read. Before the first line has been read, this function has no effect; it cannot be used to skip the first file. After the last line of the last file has been read, this function has no effect.

</div>

<div class="funcdesc">

close Close the sequence.

</div>

The class which implements the sequence behavior provided by the module is available for subclassing as well:

<div class="classdesc">

FileInput Class `FileInput` is the implementation; its methods `filename()`, `lineno()`, `fileline()`, `isfirstline()`, `isstdin()`, `nextfile()` and `close()` correspond to the functions of the same name in the module. In addition it has a `readline()` method which returns the next input line, and a `__getitem__()` method which implements the sequence behavior. The sequence must be accessed in strictly sequential order; random access and `readline()` cannot be mixed.

</div>

**Optional in-place filtering:** if the keyword argument *`inplace`*`=1` is passed to `input()` or to the `FileInput` constructor, the file is moved to a backup file and standard output is directed to the input file. This makes it possible to write a filter that rewrites its input file in place. If the keyword argument *`backup`*`=’.<some extension>’` is also given, it specifies the extension for the backup file, and the backup file remains around; by default, the extension is `’.bak’` and it is deleted when the output file is closed. In-place filtering is disabled when standard input is read.

**Caveat:** The current implementation does not work for MS-DOS 8+3 filesystems.
# `fl` — FORMS library interface for GUI applications

*FORMS library interface for GUI applications.*\
This module provides an interface to the FORMS Libraryby Mark Overmars. The source for the library can be retrieved by anonymous ftp from host `ftp.cs.ruu.nl`, directory `SGI/FORMS`. It was last tested with version 2.0b.

Most functions are literal translations of their C equivalents, dropping the initial `fl_` from their name. Constants used by the library are defined in module `FL` described below.

The creation of objects is a little different in Python than in C: instead of the ‘current form’ maintained by the library to which new FORMS objects are added, all functions that add a FORMS object to a form are methods of the Python object representing the form. Consequently, there are no Python equivalents for the C functions and , and the equivalent of is called `fl.make_form()`.

Watch out for the somewhat confusing terminology: FORMS uses the word *object* for the buttons, sliders etc. that you can place in a form. In Python, ‘object’ means any value. The Python interface to FORMS introduces two new Python object types: form objects (representing an entire form) and FORMS objects (representing one button, slider etc.). Hopefully this isn’t too confusing.

There are no ‘free objects’ in the Python interface to FORMS, nor is there an easy way to add object classes written in Python. The FORMS interface to GL event handling is available, though, so you can mix FORMS with pure GL windows.

**Please note:** importing `fl` implies a call to the GL function and to the FORMS routine .

## Functions Defined in Module `fl`

Module `fl` defines the following functions. For more information about what they do, see the description of the equivalent C function in the FORMS documentation:

<div class="funcdesc">

make_formtype, width, height Create a form with given type, width and height. This returns a *form* object, whose methods are described below.

</div>

<div class="funcdesc">

do_forms The standard FORMS main loop. Returns a Python object representing the FORMS object needing interaction, or the special value .

</div>

<div class="funcdesc">

check_forms Check for FORMS events. Returns what `do_forms()` above returns, or `None` if there is no event that immediately needs interaction.

</div>

<div class="funcdesc">

set_event_call_backfunction Set the event callback function.

</div>

<div class="funcdesc">

set_graphics_modergbmode, doublebuffering Set the graphics modes.

</div>

<div class="funcdesc">

get_rgbmode Return the current rgb mode. This is the value of the C global variable .

</div>

<div class="funcdesc">

show_messagestr1, str2, str3 Show a dialog box with a three-line message and an OK button.

</div>

<div class="funcdesc">

show_questionstr1, str2, str3 Show a dialog box with a three-line message and YES and NO buttons. It returns `1` if the user pressed YES, `0` if NO.

</div>

<div class="funcdesc">

show_choicestr1, str2, str3, but1 Show a dialog box with a three-line message and up to three buttons. It returns the number of the button clicked by the user (`1`, `2` or `3`).

</div>

<div class="funcdesc">

show_inputprompt, default Show a dialog box with a one-line prompt message and text field in which the user can enter a string. The second argument is the default input string. It returns the string value as edited by the user.

</div>

<div class="funcdesc">

show_file_selectormessage, directory, pattern, default Show a dialog box in which the user can select a file. It returns the absolute filename selected by the user, or `None` if the user presses Cancel.

</div>

<div class="funcdesc">

get_directory These functions return the directory, pattern and filename (the tail part only) selected by the user in the last `show_file_selector()` call.

</div>

<div class="funcdesc">

qdevicedev

These functions are the FORMS interfaces to the corresponding GL functions. Use these if you want to handle some GL events yourself when using `fl.do_events()`. When a GL event is detected that FORMS cannot handle, `fl.do_forms()` returns the special value and you should call `fl.qread()` to read the event from the queue. Don’t use the equivalent GL functions!

</div>

<div class="funcdesc">

color See the description in the FORMS documentation of , and .

</div>

## Form Objects

Form objects (returned by `make_form()` above) have the following methods. Each method corresponds to a C function whose name is prefixed with `fl_`; and whose first argument is a form pointer; please refer to the official FORMS documentation for descriptions.

All the `add_*()` methods return a Python object representing the FORMS object. Methods of FORMS objects are described below. Most kinds of FORMS object also have some methods specific to that kind; these methods are listed here.

<div class="flushleft">

<div class="methoddesc">

show_formplacement, bordertype, name Show the form.

</div>

<div class="methoddesc">

hide_form Hide the form.

</div>

<div class="methoddesc">

redraw_form Redraw the form.

</div>

<div class="methoddesc">

set_form_positionx, y Set the form’s position.

</div>

<div class="methoddesc">

freeze_form Freeze the form.

</div>

<div class="methoddesc">

unfreeze_form Unfreeze the form.

</div>

<div class="methoddesc">

activate_form Activate the form.

</div>

<div class="methoddesc">

deactivate_form Deactivate the form.

</div>

<div class="methoddesc">

bgn_group Begin a new group of objects; return a group object.

</div>

<div class="methoddesc">

end_group End the current group of objects.

</div>

<div class="methoddesc">

find_first Find the first object in the form.

</div>

<div class="methoddesc">

find_last Find the last object in the form.

</div>

<div class="methoddesc">

add_boxtype, x, y, w, h, name Add a box object to the form. No extra methods.

</div>

<div class="methoddesc">

add_texttype, x, y, w, h, name Add a text object to the form. No extra methods.

</div>

<div class="methoddesc">

add_clocktype, x, y, w, h, name Add a clock object to the form.\
Method: `get_clock()`.

</div>

<div class="methoddesc">

add_buttontype, x, y, w, h, name Add a button object to the form.\
Methods: `get_button()`, `set_button()`.

</div>

<div class="methoddesc">

add_lightbuttontype, x, y, w, h, name Add a lightbutton object to the form.\
Methods: `get_button()`, `set_button()`.

</div>

<div class="methoddesc">

add_roundbuttontype, x, y, w, h, name Add a roundbutton object to the form.\
Methods: `get_button()`, `set_button()`.

</div>

<div class="methoddesc">

add_slidertype, x, y, w, h, name Add a slider object to the form.\
Methods: `set_slider_value()`, `get_slider_value()`, `set_slider_bounds()`, `get_slider_bounds()`, `set_slider_return()`, `set_slider_size()`, `set_slider_precision()`, `set_slider_step()`.

</div>

<div class="methoddesc">

add_valslidertype, x, y, w, h, name Add a valslider object to the form.\
Methods: `set_slider_value()`, `get_slider_value()`, `set_slider_bounds()`, `get_slider_bounds()`, `set_slider_return()`, `set_slider_size()`, `set_slider_precision()`, `set_slider_step()`.

</div>

<div class="methoddesc">

add_dialtype, x, y, w, h, name Add a dial object to the form.\
Methods: `set_dial_value()`, `get_dial_value()`, `set_dial_bounds()`, `get_dial_bounds()`.

</div>

<div class="methoddesc">

add_positionertype, x, y, w, h, name Add a positioner object to the form.\
Methods: `set_positioner_xvalue()`, `set_positioner_yvalue()`, `set_positioner_xbounds()`, `set_positioner_ybounds()`, `get_positioner_xvalue()`, `get_positioner_yvalue()`, `get_positioner_xbounds()`, `get_positioner_ybounds()`.

</div>

<div class="methoddesc">

add_countertype, x, y, w, h, name Add a counter object to the form.\
Methods: `set_counter_value()`, `get_counter_value()`, `set_counter_bounds()`, `set_counter_step()`, `set_counter_precision()`, `set_counter_return()`.

</div>

<div class="methoddesc">

add_inputtype, x, y, w, h, name Add a input object to the form.\
Methods: `set_input()`, `get_input()`, `set_input_color()`, `set_input_return()`.

</div>

<div class="methoddesc">

add_menutype, x, y, w, h, name Add a menu object to the form.\
Methods: `set_menu()`, `get_menu()`, `addto_menu()`.

</div>

<div class="methoddesc">

add_choicetype, x, y, w, h, name Add a choice object to the form.\
Methods: `set_choice()`, `get_choice()`, `clear_choice()`, `addto_choice()`, `replace_choice()`, `delete_choice()`, `get_choice_text()`, `set_choice_fontsize()`, `set_choice_fontstyle()`.

</div>

<div class="methoddesc">

add_browsertype, x, y, w, h, name Add a browser object to the form.\
Methods: `set_browser_topline()`, `clear_browser()`, `add_browser_line()`, `addto_browser()`, `insert_browser_line()`, `delete_browser_line()`, `replace_browser_line()`, `get_browser_line()`, `load_browser()`, `get_browser_maxline()`, `select_browser_line()`, `deselect_browser_line()`, `deselect_browser()`, `isselected_browser_line()`, `get_browser()`, `set_browser_fontsize()`, `set_browser_fontstyle()`, `set_browser_specialkey()`.

</div>

<div class="methoddesc">

add_timertype, x, y, w, h, name Add a timer object to the form.\
Methods: `set_timer()`, `get_timer()`.

</div>

</div>

Form objects have the following data attributes; see the FORMS documentation:

|                          |                 |                                |
|:-------------------------|:----------------|:-------------------------------|
| NameC TypeMeaning window | int (read-only) | GL window id                   |
| w                        | float           | form width                     |
| h                        | float           | form height                    |
| x                        | float           | form x origin                  |
| y                        | float           | form y origin                  |
| deactivated              | int             | nonzero if form is deactivated |
| visible                  | int             | nonzero if form is visible     |
| frozen                   | int             | nonzero if form is frozen      |
| doublebuf                | int             | nonzero if double buffering on |
|                          |                 |                                |

## FORMS Objects

Besides methods specific to particular kinds of FORMS objects, all FORMS objects also have the following methods:

<div class="methoddesc">

set_call_backfunction, argument Set the object’s callback function and argument. When the object needs interaction, the callback function will be called with two arguments: the object, and the callback argument. (FORMS objects without a callback function are returned by `fl.do_forms()` or `fl.check_forms()` when they need interaction.) Call this method without arguments to remove the callback function.

</div>

<div class="methoddesc">

delete_object Delete the object.

</div>

<div class="methoddesc">

show_object Show the object.

</div>

<div class="methoddesc">

hide_object Hide the object.

</div>

<div class="methoddesc">

redraw_object Redraw the object.

</div>

<div class="methoddesc">

freeze_object Freeze the object.

</div>

<div class="methoddesc">

unfreeze_object Unfreeze the object.

</div>

FORMS objects have these data attributes; see the FORMS documentation:

|                            |                 |                  |
|:---------------------------|:----------------|:-----------------|
| NameC TypeMeaning objclass | int (read-only) | object class     |
| type                       | int (read-only) | object type      |
| boxtype                    | int             | box type         |
| x                          | float           | x origin         |
| y                          | float           | y origin         |
| w                          | float           | width            |
| h                          | float           | height           |
| col1                       | int             | primary color    |
| col2                       | int             | secondary color  |
| align                      | int             | alignment        |
| lcol                       | int             | label color      |
| lsize                      | float           | label font size  |
| label                      | string          | label string     |
| lstyle                     | int             | label style      |
| pushed                     | int (read-only) | (see FORMS docs) |
| focus                      | int (read-only) | (see FORMS docs) |
| belowmouse                 | int (read-only) | (see FORMS docs) |
| frozen                     | int (read-only) | (see FORMS docs) |
| active                     | int (read-only) | (see FORMS docs) |
| input                      | int (read-only) | (see FORMS docs) |
| visible                    | int (read-only) | (see FORMS docs) |
| radio                      | int (read-only) | (see FORMS docs) |
| automatic                  | int (read-only) | (see FORMS docs) |
|                            |                 |                  |

# `FL` — Constants used with the `fl` module

*Constants used with the `fl` module.*\
This module defines symbolic constants needed to use the built-in module `fl` (see above); they are equivalent to those defined in the C header file `<forms.h>` except that the name prefix `FL_` is omitted. Read the module source for a complete list of the defined names. Suggested use:

    import fl
    from FL import *

# `flp` — Functions for loading stored FORMS designs

*Functions for loading stored FORMS designs.*\
This module defines functions that can read form definitions created by the ‘form designer’ () program that comes with the FORMS library (see module `fl` above).

For now, see the file `flp.doc` in the Python library source directory for a description.

XXX A complete description should be inserted here!
# `fm` — *Font Manager* interface

**Font Manager* interface for SGI workstations.*\
This module provides access to the IRIS *Font Manager* library. It is available only on Silicon Graphics machines. See also: *4Sight User’s Guide*, section 1, chapter 5: “Using the IRIS Font Manager.”

This is not yet a full interface to the IRIS Font Manager. Among the unsupported features are: matrix operations; cache operations; character operations (use string operations instead); some details of font info; individual glyph metrics; and printer matching.

It supports the following operations:

<div class="funcdesc">

init Initialization function. Calls . It is normally not necessary to call this function, since it is called automatically the first time the `fm` module is imported.

</div>

<div class="funcdesc">

findfontfontname Return a font handle object. Calls `fmfindfont(`*`fontname`*`)`.

</div>

<div class="funcdesc">

enumerate Returns a list of available font names. This is an interface to .

</div>

<div class="funcdesc">

prstrstring Render a string using the current font (see the `setfont()` font handle method below). Calls `fmprstr(`*`string`*`)`.

</div>

<div class="funcdesc">

setpathstring Sets the font search path. Calls `fmsetpath(`*`string`*`)`. (XXX Does not work!?!)

</div>

<div class="funcdesc">

fontpath Returns the current font search path.

</div>

Font handle objects support the following operations:

<div class="funcdesc">

scalefontfactor Returns a handle for a scaled version of this font. Calls `fmscalefont(`*`fh`*`, `*`factor`*`)`.

</div>

<div class="funcdesc">

setfont Makes this font the current font. Note: the effect is undone silently when the font handle object is deleted. Calls `fmsetfont(`*`fh`*`)`.

</div>

<div class="funcdesc">

getfontname Returns this font’s name. Calls `fmgetfontname(`*`fh`*`)`.

</div>

<div class="funcdesc">

getcomment Returns the comment string associated with this font. Raises an exception if there is none. Calls `fmgetcomment(`*`fh`*`)`.

</div>

<div class="funcdesc">

getfontinfo Returns a tuple giving some pertinent data about this font. This is an interface to `fmgetfontinfo()`. The returned tuple contains the following numbers: `(`*printermatched*, *fixed_width*, *xorig*, *yorig*, *xsize*, *ysize*, *height*, *nglyphs*`)`.

</div>

<div class="funcdesc">

getstrwidthstring Returns the width, in pixels, of *string* when drawn in this font. Calls `fmgetstrwidth(`*`fh`*`, `*`string`*`)`.

</div>
# `formatter` — Generic output formatting

*Generic output formatter and device interface.*\
This module supports two interface definitions, each with multiple implementations. The *formatter* interface is used by the `HTMLParser` class of the `htmllib` module, and the *writer* interface is required by the formatter interface. Formatter objects transform an abstract flow of formatting events into specific output events on writer objects. Formatters manage several stack structures to allow various properties of a writer object to be changed and restored; writers need not be able to handle relative changes nor any sort of “change back” operation. Specific writer properties which may be controlled via formatter objects are horizontal alignment, font, and left margin indentations. A mechanism is provided which supports providing arbitrary, non-exclusive style settings to a writer as well. Additional interfaces facilitate formatting events which are not reversible, such as paragraph separation.

Writer objects encapsulate device interfaces. Abstract devices, such as file formats, are supported as well as physical devices. The provided implementations all work with abstract devices. The interface makes available mechanisms for setting the properties which formatter objects manage and inserting data into the output.

## The Formatter Interface <span id="formatter-interface" label="formatter-interface"></span>

Interfaces to create formatters are dependent on the specific formatter class being instantiated. The interfaces described below are the required interfaces which all formatters must support once initialized.

One data element is defined at the module level:

<div class="datadesc">

AS_IS Value which can be used in the font specification passed to the `push_font()` method described below, or as the new value to any other `push_`*`property`*`()` method. Pushing the `AS_IS` value allows the corresponding `pop_`*`property`*`()` method to be called without having to track whether the property was changed.

</div>

The following attributes are defined for formatter instance objects:

<div class="memberdesc">

writer The writer instance with which the formatter interacts.

</div>

<div class="methoddesc">

end_paragraphblanklines Close any open paragraphs and insert at least *blanklines* before the next paragraph.

</div>

<div class="methoddesc">

add_line_break Add a hard line break if one does not already exist. This does not break the logical paragraph.

</div>

<div class="methoddesc">

add_hor_rule\*args, \*\*kw Insert a horizontal rule in the output. A hard break is inserted if there is data in the current paragraph, but the logical paragraph is not broken. The arguments and keywords are passed on to the writer’s `send_line_break()` method.

</div>

<div class="methoddesc">

add_flowing_datadata Provide data which should be formatted with collapsed whitespace. Whitespace from preceding and successive calls to `add_flowing_data()` is considered as well when the whitespace collapse is performed. The data which is passed to this method is expected to be word-wrapped by the output device. Note that any word-wrapping still must be performed by the writer object due to the need to rely on device and font information.

</div>

<div class="methoddesc">

add_literal_datadata Provide data which should be passed to the writer unchanged. Whitespace, including newline and tab characters, are considered legal in the value of *data*.

</div>

<div class="methoddesc">

add_label_dataformat, counter Insert a label which should be placed to the left of the current left margin. This should be used for constructing bulleted or numbered lists. If the *format* value is a string, it is interpreted as a format specification for *counter*, which should be an integer. The result of this formatting becomes the value of the label; if *format* is not a string it is used as the label value directly. The label value is passed as the only argument to the writer’s `send_label_data()` method. Interpretation of non-string label values is dependent on the associated writer.

Format specifications are strings which, in combination with a counter value, are used to compute label values. Each character in the format string is copied to the label value, with some characters recognized to indicate a transform on the counter value. Specifically, the character represents the counter value formatter as an Arabic number, the characters and represent alphabetic representations of the counter value in upper and lower case, respectively, and and represent the counter value in Roman numerals, in upper and lower case. Note that the alphabetic and roman transforms require that the counter value be greater than zero.

</div>

<div class="methoddesc">

flush_softspace Send any pending whitespace buffered from a previous call to `add_flowing_data()` to the associated writer object. This should be called before any direct manipulation of the writer object.

</div>

<div class="methoddesc">

push_alignmentalign Push a new alignment setting onto the alignment stack. This may be if no change is desired. If the alignment value is changed from the previous setting, the writer’s `new_alignment()` method is called with the *align* value.

</div>

<div class="methoddesc">

pop_alignment Restore the previous alignment.

</div>

<div class="methoddesc">

push_font`(`size, italic, bold, teletype`)` Change some or all font properties of the writer object. Properties which are not set to are set to the values passed in while others are maintained at their current settings. The writer’s `new_font()` method is called with the fully resolved font specification.

</div>

<div class="methoddesc">

pop_font Restore the previous font.

</div>

<div class="methoddesc">

push_marginmargin Increase the number of left margin indentations by one, associating the logical tag *margin* with the new indentation. The initial margin level is `0`. Changed values of the logical tag must be true values; false values other than are not sufficient to change the margin.

</div>

<div class="methoddesc">

pop_margin Restore the previous margin.

</div>

<div class="methoddesc">

push_style\*styles Push any number of arbitrary style specifications. All styles are pushed onto the styles stack in order. A tuple representing the entire stack, including values, is passed to the writer’s `new_styles()` method.

</div>

<div class="methoddesc">

pop_style Pop the last *n* style specifications passed to `push_style()`. A tuple representing the revised stack, including values, is passed to the writer’s `new_styles()` method.

</div>

<div class="methoddesc">

set_spacingspacing Set the spacing style for the writer.

</div>

<div class="methoddesc">

assert_line_data Inform the formatter that data has been added to the current paragraph out-of-band. This should be used when the writer has been manipulated directly. The optional *flag* argument can be set to false if the writer manipulations produced a hard line break at the end of the output.

</div>

## Formatter Implementations <span id="formatter-impls" label="formatter-impls"></span>

Two implementations of formatter objects are provided by this module. Most applications may use one of these classes without modification or subclassing.

<div class="classdesc">

NullFormatter A formatter which does nothing. If *writer* is omitted, a `NullWriter` instance is created. No methods of the writer are called by `NullFormatter` instances. Implementations should inherit from this class if implementing a writer interface but don’t need to inherit any implementation.

</div>

<div class="classdesc">

AbstractFormatterwriter The standard formatter. This implementation has demonstrated wide applicability to many writers, and may be used directly in most circumstances. It has been used to implement a full-featured world-wide web browser.

</div>

## The Writer Interface <span id="writer-interface" label="writer-interface"></span>

Interfaces to create writers are dependent on the specific writer class being instantiated. The interfaces described below are the required interfaces which all writers must support once initialized. Note that while most applications can use the `AbstractFormatter` class as a formatter, the writer must typically be provided by the application.

<div class="methoddesc">

flush Flush any buffered output or device control events.

</div>

<div class="methoddesc">

new_alignmentalign Set the alignment style. The *align* value can be any object, but by convention is a string or `None`, where `None` indicates that the writer’s “preferred” alignment should be used. Conventional *align* values are `’left’`, `’center’`, `’right’`, and `’justify’`.

</div>

<div class="methoddesc">

new_fontfont Set the font style. The value of *font* will be `None`, indicating that the device’s default font should be used, or a tuple of the form `(`*size*, *italic*, *bold*, *teletype*`)`. Size will be a string indicating the size of font that should be used; specific strings and their interpretation must be defined by the application. The *italic*, *bold*, and *teletype* values are boolean indicators specifying which of those font attributes should be used.

</div>

<div class="methoddesc">

new_marginmargin, level Set the margin level to the integer *level* and the logical tag to *margin*. Interpretation of the logical tag is at the writer’s discretion; the only restriction on the value of the logical tag is that it not be a false value for non-zero values of *level*.

</div>

<div class="methoddesc">

new_spacingspacing Set the spacing style to *spacing*.

</div>

<div class="methoddesc">

new_stylesstyles Set additional styles. The *styles* value is a tuple of arbitrary values; the value should be ignored. The *styles* tuple may be interpreted either as a set or as a stack depending on the requirements of the application and writer implementation.

</div>

<div class="methoddesc">

send_line_break Break the current line.

</div>

<div class="methoddesc">

send_paragraphblankline Produce a paragraph separation of at least *blankline* blank lines, or the equivalent. The *blankline* value will be an integer. Note that the implementation will receive a call to `send_line_break()` before this call if a line break is needed; this method should not include ending the last line of the paragraph. It is only responsible for vertical spacing between paragraphs.

</div>

<div class="methoddesc">

send_hor_rule\*args, \*\*kw Display a horizontal rule on the output device. The arguments to this method are entirely application- and writer-specific, and should be interpreted with care. The method implementation may assume that a line break has already been issued via `send_line_break()`.

</div>

<div class="methoddesc">

send_flowing_datadata Output character data which may be word-wrapped and re-flowed as needed. Within any sequence of calls to this method, the writer may assume that spans of multiple whitespace characters have been collapsed to single space characters.

</div>

<div class="methoddesc">

send_literal_datadata Output character data which has already been formatted for display. Generally, this should be interpreted to mean that line breaks indicated by newline characters should be preserved and no new line breaks should be introduced. The data may contain embedded newline and tab characters, unlike data provided to the `send_formatted_data()` interface.

</div>

<div class="methoddesc">

send_label_datadata Set *data* to the left of the current left margin, if possible. The value of *data* is not restricted; treatment of non-string values is entirely application- and writer-dependent. This method will only be called at the beginning of a line.

</div>

## Writer Implementations <span id="writer-impls" label="writer-impls"></span>

Three implementations of the writer object interface are provided as examples by this module. Most applications will need to derive new writer classes from the `NullWriter` class.

<div class="classdesc">

NullWriter A writer which only provides the interface definition; no actions are taken on any methods. This should be the base class for all writers which do not need to inherit any implementation methods.

</div>

<div class="classdesc">

AbstractWriter A writer which can be used in debugging formatters, but not much else. Each method simply announces itself by printing its name and arguments on standard output.

</div>

<div class="classdesc">

DumbWriter Simple writer class which writes output on the file object passed in as *file* or, if *file* is omitted, on standard output. The output is simply word-wrapped to the number of columns specified by *maxcol*. This class is suitable for reflowing a sequence of paragraphs.

</div>
# `fpformat` — Floating point conversions

*General floating point formatting functions.*\
The `fpformat` module defines functions for dealing with floating point numbers representations in 100% pure Python. **Note:** This module is unneeded: everything here could be done via the `%` string interpolation operator.

The `fpformat` module defines the following functions and an exception:

<div class="funcdesc">

fixx, digs Format *x* as `[-]ddd.ddd` with *digs* digits after the point and at least one digit before. If *`digs`*` <= 0`, the decimal point is suppressed.

*x* can be either a number or a string that looks like one. *digs* is an integer.

Return value is a string.

</div>

<div class="funcdesc">

scix, digs Format *x* as `[-]d.dddE[+-]ddd` with *digs* digits after the point and exactly one digit before. If *`digs`*` <= 0`, one digit is kept and the point is suppressed.

*x* can be either a real number, or a string that looks like one. *digs* is an integer.

Return value is a string.

</div>

<div class="excdesc">

NotANumber Exception raised when a string passed to `fix()` or `sci()` as the *x* parameter does not look like a number. This is a subclass of `ValueError` when the standard exceptions are strings. The exception value is the improperly formatted string that caused the exception to be raised.

</div>

Example:

    >>> import fpformat
    >>> fpformat.fix(1.23, 1)
    '1.2'
# Built-in Functions <span id="built-in-funcs" label="built-in-funcs"></span>

The Python interpreter has a number of functions built into it that are always available. They are listed here in alphabetical order.

<div class="funcdesc">

\_\_import\_\_name This function is invoked by the statement. It mainly exists so that you can replace it with another function that has a compatible interface, in order to change the semantics of the statement. For examples of why and how you would do this, see the standard library modules `ihooks`and `rexec`. See also the built-in module `imp`, which defines some useful operations out of which you can build your own `__import__()` function.

For example, the statement ‘`import` `spam`’ results in the following call: `__import__(’spam’,` `globals(),` `locals(), [])`; the statement `from` `spam.ham import` `eggs` results in `__import__(’spam.ham’,` `globals(),` `locals(),` `[’eggs’])`. Note that even though `locals()` and `[’eggs’]` are passed in as arguments, the `__import__()` function does not set the local variable named `eggs`; this is done by subsequent code that is generated for the import statement. (In fact, the standard implementation does not use its *locals* argument at all, and uses its *globals* only to determine the package context of the statement.)

When the *name* variable is of the form `package.module`, normally, the top-level package (the name up till the first dot) is returned, *not* the module named by *name*. However, when a non-empty *fromlist* argument is given, the module named by *name* is returned. This is done for compatibility with the bytecode generated for the different kinds of import statement; when using `import spam.ham.eggs`, the top-level package `spam` must be placed in the importing namespace, but when using `from spam.ham import eggs`, the `spam.ham` subpackage must be used to find the `eggs` variable. As a workaround for this behavior, use `getattr()` to extract the desired components. For example, you could define the following helper:

    import string

    def my_import(name):
        mod = __import__(name)
        components = string.split(name, '.')
        for comp in components[1:]:
            mod = getattr(mod, comp)
        return mod

</div>

<div class="funcdesc">

absx Return the absolute value of a number. The argument may be a plain or long integer or a floating point number. If the argument is a complex number, its magnitude is returned.

</div>

<div class="funcdesc">

applyfunction, args The *function* argument must be a callable object (a user-defined or built-in function or method, or a class object) and the *args* argument must be a sequence (if it is not a tuple, the sequence is first converted to a tuple). The *function* is called with *args* as the argument list; the number of arguments is the the length of the tuple. (This is different from just calling *`func`*`(`*`args`*`)`, since in that case there is always exactly one argument.) If the optional *keywords* argument is present, it must be a dictionary whose keys are strings. It specifies keyword arguments to be added to the end of the the argument list.

</div>

<div class="funcdesc">

bufferobject The *object* argument must be an object that supports the buffer call interface (such as strings, arrays, and buffers). A new buffer object will be created which references the *object* argument. The buffer object will be a slice from the beginning of *object* (or from the specified *offset*). The slice will extend to the end of *object* (or will have a length given by the *size* argument).

</div>

<div class="funcdesc">

callableobject Return true if the *object* argument appears callable, false if not. If this returns true, it is still possible that a call fails, but if it is false, calling *object* will never succeed. Note that classes are callable (calling a class returns a new instance); class instances are callable if they have a `__call__()` method.

</div>

<div class="funcdesc">

chri Return a string of one character whose code is the integer *i*, e.g., `chr(97)` returns the string `’a’`. This is the inverse of `ord()`. The argument must be in the range \[0..255\], inclusive; `ValueError` will be raised if *i* is outside that range.

</div>

<div class="funcdesc">

cmpx, y Compare the two objects *x* and *y* and return an integer according to the outcome. The return value is negative if *`x`*` < `*`y`*, zero if *`x`*` == `*`y`* and strictly positive if *`x`*` > `*`y`*.

</div>

<div class="funcdesc">

coercex, y Return a tuple consisting of the two numeric arguments converted to a common type, using the same rules as used by arithmetic operations.

</div>

<div class="funcdesc">

compilestring, filename, kind Compile the *string* into a code object. Code objects can be executed by an statement or evaluated by a call to `eval()`. The *filename* argument should give the file from which the code was read; pass e.g. `’<string>’` if it wasn’t read from a file. The *kind* argument specifies what kind of code must be compiled; it can be `’exec’` if *string* consists of a sequence of statements, `’eval’` if it consists of a single expression, or `’single’` if it consists of a single interactive statement (in the latter case, expression statements that evaluate to something else than `None` will printed).

</div>

<div class="funcdesc">

complexreal Create a complex number with the value *real* + *imag*\*j or convert a string or number to a complex number. Each argument may be any numeric type (including complex). If *imag* is omitted, it defaults to zero and the function serves as a numeric conversion function like `int()`, `long()` and `float()`; in this case it also accepts a string argument which should be a valid complex number.

</div>

<div class="funcdesc">

delattrobject, name This is a relative of `setattr()`. The arguments are an object and a string. The string must be the name of one of the object’s attributes. The function deletes the named attribute, provided the object allows it. For example, `delattr(`*`x`*`, ’`*`foobar`*`’)` is equivalent to `del `*`x`*`.`*`foobar`*.

</div>

<div class="funcdesc">

dir Without arguments, return the list of names in the current local symbol table. With an argument, attempts to return a list of valid attribute for that object. This information is gleaned from the object’s `__dict__`, `__methods__` and `__members__` attributes, if defined. The list is not necessarily complete; e.g., for classes, attributes defined in base classes are not included, and for class instances, methods are not included. The resulting list is sorted alphabetically. For example:

    >>> import sys
    >>> dir()
    ['sys']
    >>> dir(sys)
    ['argv', 'exit', 'modules', 'path', 'stderr', 'stdin', 'stdout']

</div>

<div class="funcdesc">

divmoda, b Take two numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using long division. With mixed operand types, the rules for binary arithmetic operators apply. For plain and long integers, the result is the same as `(`*`a`*` / `*`b`*`, `*`a`*` % `*`b`*`)`. For floating point numbers the result is `(`*`q`*`, `*`a`*` % `*`b`*`)`, where *q* is usually `math.floor(`*`a`*` / `*`b`*`)` but may be 1 less than that. In any case *`q`*` * `*`b`*` + `*`a`*` % `*`b`* is very close to *a*, if *`a`*` % `*`b`* is non-zero it has the same sign as *b*, and `0 <= abs(`*`a`*` % `*`b`*`) < abs(`*`b`*`)`.

</div>

<div class="funcdesc">

evalexpression The arguments are a string and two optional dictionaries. The *expression* argument is parsed and evaluated as a Python expression (technically speaking, a condition list) using the *globals* and *locals* dictionaries as global and local name space. If the *locals* dictionary is omitted it defaults to the *globals* dictionary. If both dictionaries are omitted, the expression is executed in the environment where is called. The return value is the result of the evaluated expression. Syntax errors are reported as exceptions. Example:

    >>> x = 1
    >>> print eval('x+1')
    2

This function can also be used to execute arbitrary code objects (e.g. created by `compile()`). In this case pass a code object instead of a string. The code object must have been compiled passing `’eval’` to the *kind* argument.

Hints: dynamic execution of statements is supported by the statement. Execution of statements from a file is supported by the `execfile()` function. The `globals()` and `locals()` functions returns the current global and local dictionary, respectively, which may be useful to pass around for use by `eval()` or `execfile()`.

</div>

<div class="funcdesc">

execfilefile This function is similar to the statement, but parses a file instead of a string. It is different from the statement in that it does not use the module administration — it reads the file unconditionally and does not create a new module.[^1]

The arguments are a file name and two optional dictionaries. The file is parsed and evaluated as a sequence of Python statements (similarly to a module) using the *globals* and *locals* dictionaries as global and local namespace. If the *locals* dictionary is omitted it defaults to the *globals* dictionary. If both dictionaries are omitted, the expression is executed in the environment where `execfile()` is called. The return value is `None`.

</div>

<div class="funcdesc">

filterfunction, list Construct a list from those elements of *list* for which *function* returns true. If *list* is a string or a tuple, the result also has that type; otherwise it is always a list. If *function* is `None`, the identity function is assumed, i.e. all elements of *list* that are false (zero or empty) are removed.

</div>

<div class="funcdesc">

floatx Convert a string or a number to floating point. If the argument is a string, it must contain a possibly signed decimal or floating point number, possibly embedded in whitespace; this behaves identical to `string.atof(`*`x`*`)`. Otherwise, the argument may be a plain or long integer or a floating point number, and a floating point number with the same value (within Python’s floating point precision) is returned.

**Note:** When passing in a string, values for NaNand Infinitymay be returned, depending on the underlying C library. The specific set of strings accepted which cause these values to be returned depends entirely on the C library and is known to vary.

</div>

<div class="funcdesc">

getattrobject, name Return the value of the named attributed of *object*. *name* must be a string. If the string is the name of one of the object’s attributes, the result is the value of that attribute. For example, `getattr(x, ’foobar’)` is equivalent to `x.foobar`. If the named attribute does not exist, *default* is returned if provided, otherwise `AttributeError` is raised.

</div>

<div class="funcdesc">

globals Return a dictionary representing the current global symbol table. This is always the dictionary of the current module (inside a function or method, this is the module where it is defined, not the module from which it is called).

</div>

<div class="funcdesc">

hasattrobject, name The arguments are an object and a string. The result is 1 if the string is the name of one of the object’s attributes, 0 if not. (This is implemented by calling `getattr(`*`object`*`, `*`name`*`)` and seeing whether it raises an exception or not.)

</div>

<div class="funcdesc">

hashobject Return the hash value of the object (if it has one). Hash values are integers. They are used to quickly compare dictionary keys during a dictionary lookup. Numeric values that compare equal have the same hash value (even if they are of different types, e.g. 1 and 1.0).

</div>

<div class="funcdesc">

hexx Convert an integer number (of any size) to a hexadecimal string. The result is a valid Python expression. Note: this always yields an unsigned literal, e.g. on a 32-bit machine, `hex(-1)` yields `’0xffffffff’`. When evaluated on a machine with the same word size, this literal is evaluated as -1; at a different word size, it may turn up as a large positive number or raise an `OverflowError` exception.

</div>

<div class="funcdesc">

idobject Return the ‘identity’ of an object. This is an integer (or long integer) which is guaranteed to be unique and constant for this object during its lifetime. Two objects whose lifetimes are disjunct may have the same `id()` value. (Implementation note: this is the address of the object.)

</div>

<div class="funcdesc">

input Equivalent to `eval(raw_input(`*`prompt`*`))`. **Warning:** This function is not safe from user errors! It expects a valid Python expression as input; if the input is not syntactically valid, a `SyntaxError` will be raised. Other exceptions may be raised if there is an error during evaluation. (On the other hand, sometimes this is exactly what you need when writing a quick script for expert use.)

If the `readline` module was loaded, then `input()` will use it to provide elaborate line editing and history features.

Consider using the `raw_input()` function for general input from users.

</div>

<div class="funcdesc">

intx Convert a string or number to a plain integer. If the argument is a string, it must contain a possibly signed decimal number representable as a Python integer, possibly embedded in whitespace; this behaves identical to `string.atoi(`*`x`*`)`. The *radix* parameter gives the base for the conversion and may be any integer in the range \[2, 36\]. If *radix* is specified and *x* is not a string, `TypeError` is raised. Otherwise, the argument may be a plain or long integer or a floating point number. Conversion of floating point numbers to integers is defined by the C semantics; normally the conversion truncates towards zero.[^2]

</div>

<div class="funcdesc">

internstring Enter *string* in the table of “interned” strings and return the interned string – which is *string* itself or a copy. Interning strings is useful to gain a little performance on dictionary lookup – if the keys in a dictionary are interned, and the lookup key is interned, the key comparisons (after hashing) can be done by a pointer compare instead of a string compare. Normally, the names used in Python programs are automatically interned, and the dictionaries used to hold module, class or instance attributes have interned keys. Interned strings are immortal (i.e. never get garbage collected).

</div>

<div class="funcdesc">

isinstanceobject, class Return true if the *object* argument is an instance of the *class* argument, or of a (direct or indirect) subclass thereof. Also return true if *class* is a type object and *object* is an object of that type. If *object* is not a class instance or a object of the given type, the function always returns false. If *class* is neither a class object nor a type object, a `TypeError` exception is raised.

</div>

<div class="funcdesc">

issubclassclass1, class2 Return true if *class1* is a subclass (direct or indirect) of *class2*. A class is considered a subclass of itself. If either argument is not a class object, a `TypeError` exception is raised.

</div>

<div class="funcdesc">

lens Return the length (the number of items) of an object. The argument may be a sequence (string, tuple or list) or a mapping (dictionary).

</div>

<div class="funcdesc">

listsequence Return a list whose items are the same and in the same order as *sequence*’s items. If *sequence* is already a list, a copy is made and returned, similar to *`sequence`*`[:]`. For instance, `list(’abc’)` returns returns `[’a’, ’b’, ’c’]` and `list( (1, 2, 3) )` returns `[1, 2, 3]`.

</div>

<div class="funcdesc">

locals Return a dictionary representing the current local symbol table. **Warning:** The contents of this dictionary should not be modified; changes may not affect the values of local variables used by the interpreter.

</div>

<div class="funcdesc">

longx Convert a string or number to a long integer. If the argument is a string, it must contain a possibly signed decimal number of arbitrary size, possibly embedded in whitespace; this behaves identical to `string.atol(`*`x`*`)`. Otherwise, the argument may be a plain or long integer or a floating point number, and a long integer with the same value is returned. Conversion of floating point numbers to integers is defined by the C semantics; see the description of `int()`.

</div>

<div class="funcdesc">

mapfunction, list, ... Apply *function* to every item of *list* and return a list of the results. If additional *list* arguments are passed, *function* must take that many arguments and is applied to the items of all lists in parallel; if a list is shorter than another it is assumed to be extended with `None` items. If *function* is `None`, the identity function is assumed; if there are multiple list arguments, `map()` returns a list consisting of tuples containing the corresponding items from all lists (i.e. a kind of transpose operation). The *list* arguments may be any kind of sequence; the result is always a list.

</div>

<div class="funcdesc">

maxs With a single argument *s*, return the largest item of a non-empty sequence (e.g., a string, tuple or list). With more than one argument, return the largest of the arguments.

</div>

<div class="funcdesc">

mins With a single argument *s*, return the smallest item of a non-empty sequence (e.g., a string, tuple or list). With more than one argument, return the smallest of the arguments.

</div>

<div class="funcdesc">

octx Convert an integer number (of any size) to an octal string. The result is a valid Python expression. Note: this always yields an unsigned literal, e.g. on a 32-bit machine, `oct(-1)` yields `’037777777777’`. When evaluated on a machine with the same word size, this literal is evaluated as -1; at a different word size, it may turn up as a large positive number or raise an `OverflowError` exception.

</div>

<div class="funcdesc">

openfilename Return a new file object (described earlier under Built-in Types). The first two arguments are the same as for `stdio`’s : *filename* is the file name to be opened, *mode* indicates how the file is to be opened: `’r’` for reading, `’w’` for writing (truncating an existing file), and `’a’` opens it for appending (which on *some* Unix systems means that *all* writes append to the end of the file, regardless of the current seek position).

Modes `’r+’`, `’w+’` and `’a+’` open the file for updating (note that `’w+’` truncates the file). Append `’b’` to the mode to open the file in binary mode, on systems that differentiate between binary and text files (else it is ignored). If the file cannot be opened, `IOError` is raised.

If *mode* is omitted, it defaults to `’r’`. When opening a binary file, you should append `’b’` to the *mode* value for improved portability. (It’s useful even on systems which don’t treat binary and text files differently, where it serves as documentation.) The optional *bufsize* argument specifies the file’s desired buffer size: 0 means unbuffered, 1 means line buffered, any other positive value means use a buffer of (approximately) that size. A negative *bufsize* means to use the system default, which is usually line buffered for for tty devices and fully buffered for other files. If omitted, the system default is used.[^3]

</div>

<div class="funcdesc">

ordc Return the value of a string of one character or a Unicode character. E.g., `ord(’a’)` returns the integer `97`, `ord(u’`\
`u2020’)` returns `8224`. This is the inverse of `chr()` for strings and of `unichr()` for Unicode characters.

</div>

<div class="funcdesc">

powx, y Return *x* to the power *y*; if *z* is present, return *x* to the power *y*, modulo *z* (computed more efficiently than `pow(`*`x`*`, `*`y`*`) % `*`z`*). The arguments must have numeric types. With mixed operand types, the rules for binary arithmetic operators apply. The effective operand type is also the type of the result; if the result is not expressible in this type, the function raises an exception; e.g., `pow(2, -1)` or `pow(2, 35000)` is not allowed.

</div>

<div class="funcdesc">

range stop This is a versatile function to create lists containing arithmetic progressions. It is most often used in loops. The arguments must be plain integers. If the *step* argument is omitted, it defaults to `1`. If the *start* argument is omitted, it defaults to `0`. The full form returns a list of plain integers `[`*`start`*`, `*`start`*` + `*`step`*`, `*`start`*` + 2 * `*`step`*`, …]`. If *step* is positive, the last element is the largest *`start`*` + `*`i`*` * `*`step`* less than *stop*; if *step* is negative, the last element is the largest *`start`*` + `*`i`*` * `*`step`* greater than *stop*. *step* must not be zero (or else `ValueError` is raised). Example:

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

</div>

<div class="funcdesc">

raw_input If the *prompt* argument is present, it is written to standard output without a trailing newline. The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that. When EOF is read, `EOFError` is raised. Example:

    >>> s = raw_input('--> ')
    --> Monty Python's Flying Circus
    >>> s
    "Monty Python's Flying Circus"

If the `readline` module was loaded, then `raw_input()` will use it to provide elaborate line editing and history features.

</div>

<div class="funcdesc">

reducefunction, sequence Apply *function* of two arguments cumulatively to the items of *sequence*, from left to right, so as to reduce the sequence to a single value. For example, `reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])` calculates `((((1+2)+3)+4)+5)`. If the optional *initializer* is present, it is placed before the items of the sequence in the calculation, and serves as a default when the sequence is empty.

</div>

<div class="funcdesc">

reloadmodule Re-parse and re-initialize an already imported *module*. The argument must be a module object, so it must have been successfully imported before. This is useful if you have edited the module source file using an external editor and want to try out the new version without leaving the Python interpreter. The return value is the module object (i.e. the same as the *module* argument).

There are a number of caveats:

If a module is syntactically correct but its initialization fails, the first statement for it does not bind its name locally, but does store a (partially initialized) module object in `sys.modules`. To reload the module you must first it again (this will bind the name to the partially initialized module object) before you can `reload()` it.

When a module is reloaded, its dictionary (containing the module’s global variables) is retained. Redefinitions of names will override the old definitions, so this is generally not a problem. If the new version of a module does not define a name that was defined by the old version, the old definition remains. This feature can be used to the module’s advantage if it maintains a global table or cache of objects — with a statement it can test for the table’s presence and skip its initialization if desired.

It is legal though generally not very useful to reload built-in or dynamically loaded modules, except for `sys`, `__main__` and `__builtin__`. In many cases, however, extension modules are not designed to be initialized more than once, and may fail in arbitrary ways when reloaded.

If a module imports objects from another module using … …, calling `reload()` for the other module does not redefine the objects imported from it — one way around this is to re-execute the statement, another is to use and qualified names (*module*.*name*) instead.

If a module instantiates instances of a class, reloading the module that defines the class does not affect the method definitions of the instances — they continue to use the old class definition. The same is true for derived classes.

</div>

<div class="funcdesc">

reprobject Return a string containing a printable representation of an object. This is the same value yielded by conversions (reverse quotes). It is sometimes useful to be able to access this operation as an ordinary function. For many types, this function makes an attempt to return a string that would yield an object with the same value when passed to `eval()`.

</div>

<div class="funcdesc">

roundx Return the floating point value *x* rounded to *n* digits after the decimal point. If *n* is omitted, it defaults to zero. The result is a floating point number. Values are rounded to the closest multiple of 10 to the power minus *n*; if two multiples are equally close, rounding is done away from 0 (so e.g. `round(0.5)` is `1.0` and `round(-0.5)` is `-1.0`).

</div>

<div class="funcdesc">

setattrobject, name, value This is the counterpart of `getattr()`. The arguments are an object, a string and an arbitrary value. The string may name an existing attribute or a new attribute. The function assigns the value to the attribute, provided the object allows it. For example, `setattr(`*`x`*`, ’`*`foobar`*`’, 123)` is equivalent to *`x`*`.`*`foobar`*` = 123`.

</div>

<div class="funcdesc">

slice stop Return a slice object representing the set of indices specified by `range(`*`start`*`, `*`stop`*`, `*`step`*`)`. The *start* and *step* arguments default to None. Slice objects have read-only data attributes `start`, `stop` and `step` which merely return the argument values (or their default). They have no other explicit functionality; however they are used by Numerical Pythonand other third party extensions. Slice objects are also generated when extended indexing syntax is used, e.g. for `a[start:stop:step]` or `a[start:stop, i]`.

</div>

<div class="funcdesc">

strobject Return a string containing a nicely printable representation of an object. For strings, this returns the string itself. The difference with `repr(`*`object`*`)` is that `str(`*`object`*`)` does not always attempt to return a string that is acceptable to `eval()`; its goal is to return a printable string.

</div>

<div class="funcdesc">

tuplesequence Return a tuple whose items are the same and in the same order as *sequence*’s items. If *sequence* is already a tuple, it is returned unchanged. For instance, `tuple(’abc’)` returns returns `(’a’, ’b’, ’c’)` and `tuple([1, 2, 3])` returns `(1, 2, 3)`.

</div>

<div class="funcdesc">

typeobject Return the type of an *object*. The return value is a type object. The standard module `types` defines names for all built-in types. For instance:

    >>> import types
    >>> if type(x) == types.StringType: print "It's a string"

</div>

<div class="funcdesc">

unichri Return the Unicode string of one character whose Unicode code is the integer *i*, e.g., `unichr(97)` returns the string `u’a’`. This is the inverse of `ord()` for Unicode strings. The argument must be in the range \[0..65535\], inclusive. `ValueError` is raised otherwise. *New in version 2.0.*

</div>

<div class="funcdesc">

unicodestring Decodes *string* using the codec for *encoding*. Error handling is done according to *errors*. The default behavior is to decode UTF-8 in strict mode, meaning that encoding errors raise `ValueError`. See also the `codecs` module. *New in version 2.0.*

</div>

<div class="funcdesc">

vars Without arguments, return a dictionary corresponding to the current local symbol table. With a module, class or class instance object as argument (or anything else that has a `__dict__` attribute), returns a dictionary corresponding to the object’s symbol table. The returned dictionary should not be modified: the effects on the corresponding symbol table are undefined.[^4]

</div>

<div class="funcdesc">

xrange stop This function is very similar to `range()`, but returns an “xrange object” instead of a list. This is an opaque sequence type which yields the same values as the corresponding list, without actually storing them all simultaneously. The advantage of `xrange()` over `range()` is minimal (since `xrange()` still has to create the values when asked for them) except when a very large range is used on a memory-starved machine (e.g. MS-DOS) or when all of the range’s elements are never used (e.g. when the loop is usually terminated with ).

</div>

<div class="funcdesc">

zipseq1, This function returns a list of tuples, where each tuple contains the *i*-th element from each of the argument sequences. At least one sequence is required, otherwise a `TypeError` is raised. The returned list is truncated in length to the length of the shortest argument sequence. When there are multiple argument sequences which are all of the same length, `zip()` is similar to `map()` with an initial argument of `None`. With a single sequence argument, it returns a list of 1-tuples. *New in version 2.0.*

</div>

[^1]: It is used relatively rarely so does not warrant being made into a statement.

[^2]: This is ugly — the language definition should require truncation towards zero.

[^3]: Specifying a buffer size currently has no effect on systems that don’t have . The interface to specify the buffer size is not done using a method that calls , because that may dump core when called after any I/O has been performed, and there’s no reliable way to determine whether this is the case.

[^4]: In the current implementation, local variable bindings cannot normally be affected this way, but variables retrieved from other scopes (e.g. modules) can be. This may change.
# `gc` — Garbage Collector interface

*Interface to the cycle-detecting garbage collector.*\
The `gc` module is only available if the interpreter was built with the optional cyclic garbage detector (enabled by default). If this was not enabled, an `ImportError` is raised by attempts to import this module.

This module provides an interface to the optional garbage collector. It provides the ability to disable the collector, tune the collection frequency, and set debugging options. It also provides access to unreachable objects that the collector found but cannot free. Since the collector supplements the reference counting already used in Python, you can disable the collector if you are sure your program does not create reference cycles. Automatic collection can be disabled by calling `gc.disable()`. To debug a leaking program call `gc.set_debug(gc.DEBUG_LEAK)`.

The `gc` module provides the following functions:

<div class="funcdesc">

enable Enable automatic garbage collection.

</div>

<div class="funcdesc">

disable Disable automatic garbage collection.

</div>

<div class="funcdesc">

isenabled Returns true if automatic collection is enabled.

</div>

<div class="funcdesc">

collect Run a full collection. All generations are examined and the number of unreachable objects found is returned.

</div>

<div class="funcdesc">

set_debugflags Set the garbage collection debugging flags. Debugging information will be written to `sys.stderr`. See below for a list of debugging flags which can be combined using bit operations to control debugging.

</div>

<div class="funcdesc">

get_debug Return the debugging flags currently set.

</div>

<div class="funcdesc">

set_thresholdthreshold0 Set the garbage collection thresholds (the collection frequency). Setting *threshold0* to zero disables collection.

The GC classifies objects into three generations depending on how many collection sweeps they have survived. New objects are placed in the youngest generation (generation `0`). If an object survives a collection it is moved into the next older generation. Since generation `2` is the oldest generation, objects in that generation remain there after a collection. In order to decide when to run, the collector keeps track of the number object allocations and deallocations since the last collection. When the number of allocations minus the number of deallocations exceeds *threshold0*, collection starts. Initially only generation `0` is examined. If generation `0` has been examined more than *threshold1* times since generation `1` has been examined, then generation `1` is examined as well. Similarly, *threshold2* controls the number of collections of generation `1` before collecting generation `2`.

</div>

<div class="funcdesc">

get_threshold Return the current collection thresholds as a tuple of `(`*`threshold0`*`, `*`threshold1`*`, `*`threshold2`*`)`.

</div>

The following variable is provided for read-only access:

<div class="datadesc">

garbage A list of objects which the collector found to be unreachable but could not be freed (uncollectable objects). Objects that have `__del__()` methods and create part of a reference cycle cause the entire reference cycle to be uncollectable. If is set, then all unreachable objects will be added to this list rather than freed.

</div>

The following constants are provided for use with `set_debug()`:

<div class="datadesc">

DEBUG_STATS Print statistics during collection. This information can be useful when tuning the collection frequency.

</div>

<div class="datadesc">

DEBUG_COLLECTABLE Print information on collectable objects found.

</div>

<div class="datadesc">

DEBUG_UNCOLLECTABLE Print information of uncollectable objects found (objects which are not reachable but cannot be freed by the collector). These objects will be added to the `garbage` list.

</div>

<div class="datadesc">

DEBUG_INSTANCES When or is set, print information about instance objects found.

</div>

<div class="datadesc">

DEBUG_OBJECTS When or is set, print information about objects other than instance objects found.

</div>

<div class="datadesc">

DEBUG_SAVEALL When set, all unreachable objects found will be appended to *garbage* rather than being freed. This can be useful for debugging a leaking program.

</div>

<div class="datadesc">

DEBUG_LEAK The debugging flags necessary for the collector to print information about a leaking program (equal to `DEBUG_COLLECTABLE | DEBUG_UNCOLLECTABLE | DEBUG_INSTANCES | DEBUG_OBJECTS | DEBUG_SAVEALL`).

</div>
# `getopt` — Parser for command line options.

*Parser for command line options.*\
This module helps scripts to parse the command line arguments in `sys.argv`. It supports the same conventions as the Unix function (including the special meanings of arguments of the form ‘`-`’ and ‘`-``-`’).

Long options similar to those supported by GNU software may be used as well via an optional third argument. This module provides a single function and an exception:

<div class="funcdesc">

getoptargs, options Parses command line options and parameter list. *args* is the argument list to be parsed, without the leading reference to the running program. Typically, this means `sys.argv[1:]`. *options* is the string of option letters that the script wants to recognize, with options that require an argument followed by a colon (; i.e., the same format that Unix uses).

*long_options*, if specified, must be a list of strings with the names of the long options which should be supported. The leading `’-``-’` characters should not be included in the option name. Long options which require an argument should be followed by an equal sign ().

The return value consists of two elements: the first is a list of `(`*`option`*`, `*`value`*`)` pairs; the second is the list of program arguments left after the option list was stripped (this is a trailing slice of *args*). Each option-and-value pair returned has the option as its first element, prefixed with a hyphen for short options (e.g., `’-x’`) or two hyphens for long options (e.g., `’-``-long-option’`), and the option argument as its second element, or an empty string if the option has no argument. The options occur in the list in the same order in which they were found, thus allowing multiple occurrences. Long and short options may be mixed.

</div>

<div class="excdesc">

GetoptError This is raised when an unrecognized option is found in the argument list or when an option requiring an argument is given none. The argument to the exception is a string indicating the cause of the error. For long options, an argument given to an option which does not require one will also cause this exception to be raised. The attributes `msg` and `opt` give the error message and related option; if there is no specific option to which the exception relates, `opt` is an empty string.

</div>

<div class="excdesc">

error Alias for `GetoptError`; for backward compatibility.

</div>

An example using only Unix style options:

    >>> import getopt
    >>> args = '-a -b -cfoo -d bar a1 a2'.split()
    >>> args
    ['-a', '-b', '-cfoo', '-d', 'bar', 'a1', 'a2']
    >>> optlist, args = getopt.getopt(args, 'abc:d:')
    >>> optlist
    [('-a', ''), ('-b', ''), ('-c', 'foo'), ('-d', 'bar')]
    >>> args
    ['a1', 'a2']

Using long option names is equally easy:

    >>> s = '--condition=foo --testing --output-file abc.def -x a1 a2'
    >>> args = s.split()
    >>> args
    ['--condition=foo', '--testing', '--output-file', 'abc.def', '-x', 'a1', 'a2']
    >>> optlist, args = getopt.getopt(args, 'x', [
    ...     'condition=', 'output-file=', 'testing'])
    >>> optlist
    [('--condition', 'foo'), ('--testing', ''), ('--output-file', 'abc.def'), ('-x',
     '')]
    >>> args
    ['a1', 'a2']

In a script, typical usage is something like this:

    import getopt, sys

    def main():
        try:
            opts, args = getopt.getopt(sys.argv[1:], "ho:", ["help", "output="])
        except getopt.GetoptError:
            # print help information and exit:
            usage()
            sys.exit(2)
        output = None
        for o, a in opts:
            if o in ("-h", "--help"):
                usage()
                sys.exit()
            if o in ("-o", "--output"):
                output = a
        # ...

    if __name__ == "__main__":
        main()
# `getpass` — Portable password input

*Portable reading of passwords and retrieval of the userid.*\
The `getpass` module provides two functions:

<div class="funcdesc">

getpass Prompt the user for a password without echoing. The user is prompted using the string *prompt*, which defaults to `’Password: ’`. Availability: Macintosh, Unix, Windows.

</div>

<div class="funcdesc">

getuser Return the “login name” of the user. Availability: Unix, Windows.

This function checks the environment variables , , and , in order, and returns the value of the first one which is set to a non-empty string. If none are set, the login name from the password database is returned on systems which support the `pwd` module, otherwise, an exception is raised.

</div>
# `gettext` — Multilingual internationalization services

*Multilingual internationalization services.*\
The `gettext` module provides internationalization (I18N) and localization (L10N) services for your Python modules and applications. It supports both the GNU `gettext` message catalog API and a higher level, class-based API that may be more appropriate for Python files. The interface described below allows you to write your module and application messages in one natural language, and provide a catalog of translated messages for running under different natural languages.

Some hints on localizing your Python modules and applications are also given.

## GNU API

The `gettext` module defines the following API, which is very similar to the GNU API. If you use this API you will affect the translation of your entire application globally. Often this is what you want if your application is monolingual, with the choice of language dependent on the locale of your user. If you are localizing a Python module, or if your application needs to switch languages on the fly, you probably want to use the class-based API instead.

<div class="funcdesc">

bindtextdomaindomain Bind the *domain* to the locale directory *localedir*. More concretely, `gettext` will look for binary `.mo` files for the given domain using the path (on Unix): *`localedir`*`/`*`language`*`/LC_MESSAGES/`*`domain`*`.mo`, where *languages* is searched for in the environment variables , , , and respectively.

If *localedir* is omitted or `None`, then the current binding for *domain* is returned.[^1]

</div>

<div class="funcdesc">

textdomain Change or query the current global domain. If *domain* is `None`, then the current global domain is returned, otherwise the global domain is set to *domain*, which is returned.

</div>

<div class="funcdesc">

gettextmessage Return the localized translation of *message*, based on the current global domain, language, and locale directory. This function is usually aliased as `_` in the local namespace (see examples below).

</div>

<div class="funcdesc">

dgettextdomain, message Like `gettext()`, but look the message up in the specified *domain*.

</div>

Note that GNU also defines a `dcgettext()` method, but this was deemed not useful and so it is currently unimplemented.

Here’s an example of typical usage for this API:

    import gettext
    gettext.bindtextdomain('myapplication', '/path/to/my/language/directory')
    gettext.textdomain('myapplication')
    _ = gettext.gettext
    # ...
    print _('This is a translatable string.')

## Class-based API

The class-based API of the `gettext` module gives you more flexibility and greater convenience than the GNU API. It is the recommended way of localizing your Python applications and modules. `gettext` defines a “translations” class which implements the parsing of GNU `.mo` format files, and has methods for returning either standard 8-bit strings or Unicode strings. Translations instances can also install themselves in the built-in namespace as the function `_()`.

<div class="funcdesc">

finddomain This function implements the standard `.mo` file search algorithm. It takes a *domain*, identical to what `textdomain()` takes, and optionally a *localedir* (as in `bindtextdomain()`), and a list of languages. All arguments are strings.

If *localedir* is not given, then the default system locale directory is used.[^2] If *languages* is not given, then the following environment variables are searched: , , , and . The first one returning a non-empty value is used for the *languages* variable. The environment variables can contain a colon separated list of languages, which will be split.

`find()` then expands and normalizes the languages, and then iterates through them, searching for an existing file built of these components:

*`localedir`*`/`*`language`*`/LC_MESSAGES/`*`domain`*`.mo`

The first such file name that exists is returned by `find()`. If no such file is found, then `None` is returned.

</div>

<div class="funcdesc">

translationdomain Return a `Translations` instance based on the *domain*, *localedir*, and *languages*, which are first passed to `find()` to get the associated `.mo` file path. Instances with identical `.mo` file names are cached. The actual class instantiated is either *class\_* if provided, otherwise `GNUTranslations`. The class’s constructor must take a single file object argument. If no `.mo` file is found, this function raises `IOError`.

</div>

<div class="funcdesc">

installdomain This installs the function `_` in Python’s builtin namespace, based on *domain*, and *localedir* which are passed to the function `translation()`. The *unicode* flag is passed to the resulting translation object’s `install` method.

As seen below, you usually mark the strings in your application that are candidates for translation, by wrapping them in a call to the function `_()`, e.g.

    print _('This string will be translated.')

For convenience, you want the `_()` function to be installed in Python’s builtin namespace, so it is easily accessible in all modules of your application.

</div>

### The `NullTranslations` class

Translation classes are what actually implement the translation of original source file message strings to translated message strings. The base class used by all translation classes is `NullTranslations`; this provides the basic interface you can use to write your own specialized translation classes. Here are the methods of `NullTranslations`:

<div class="methoddesc">

\_\_init\_\_ Takes an optional file object *fp*, which is ignored by the base class. Initializes “protected” instance variables *\_info* and *\_charset* which are set by derived classes. It then calls `self._parse(fp)` if *fp* is not `None`.

</div>

<div class="methoddesc">

\_parsefp No-op’d in the base class, this method takes file object *fp*, and reads the data from the file, initializing its message catalog. If you have an unsupported message catalog file format, you should override this method to parse your format.

</div>

<div class="methoddesc">

gettextmessage Return the translated message. Overridden in derived classes.

</div>

<div class="methoddesc">

ugettextmessage Return the translated message as a Unicode string. Overridden in derived classes.

</div>

<div class="methoddesc">

info Return the “protected” `_info` variable.

</div>

<div class="methoddesc">

charset Return the “protected” `_charset` variable.

</div>

<div class="methoddesc">

install If the *unicode* flag is false, this method installs `self.gettext()` into the built-in namespace, binding it to `_`. If *unicode* is true, it binds `self.ugettext()` instead. By default, *unicode* is false.

Note that this is only one way, albeit the most convenient way, to make the `_` function available to your application. Because it affects the entire application globally, and specifically the built-in namespace, localized modules should never install `_`. Instead, they should use this code to make `_` available to their module:

    import gettext
    t = gettext.translation('mymodule', ...)
    _ = t.gettext

This puts `_` only in the module’s global namespace and so only affects calls within this module.

</div>

### The `GNUTranslations` class

The `gettext` module provides one additional class derived from `NullTranslations`: `GNUTranslations`. This class overrides `_parse()` to enable reading GNU format `.mo` files in both big-endian and little-endian format.

It also parses optional meta-data out of the translation catalog. It is convention with GNU to include meta-data as the translation for the empty string. This meta-data is in -style `key: value` pairs. If the key `Content-Type` is found, then the `charset` property is used to initialize the “protected” `_charset` instance variable. The entire set of key/value pairs are placed into a dictionary and set as the “protected” `_info` instance variable.

If the `.mo` file’s magic number is invalid, or if other problems occur while reading the file, instantiating a `GNUTranslations` class can raise `IOError`.

The other usefully overridden method is `ugettext()`, which returns a Unicode string by passing both the translated message string and the value of the “protected” `_charset` variable to the builtin `unicode()` function.

### Solaris message catalog support

The Solaris operating system defines its own binary `.mo` file format, but since no documentation can be found on this format, it is not supported at this time.

### The Catalog constructor

GNOMEuses a version of the `gettext` module by James Henstridge, but this version has a slightly different API. Its documented usage was:

    import gettext
    cat = gettext.Catalog(domain, localedir)
    _ = cat.gettext
    print _('hello world')

For compatibility with this older module, the function `Catalog()` is an alias for the the `translation()` function described above.

One difference between this module and Henstridge’s: his catalog objects supported access through a mapping API, but this appears to be unused and so is not currently supported.

## Internationalizing your programs and modules

Internationalization (I18N) refers to the operation by which a program is made aware of multiple languages. Localization (L10N) refers to the adaptation of your program, once internationalized, to the local language and cultural habits. In order to provide multilingual messages for your Python programs, you need to take the following steps:

1.  prepare your program or module by specially marking translatable strings

2.  run a suite of tools over your marked files to generate raw messages catalogs

3.  create language specific translations of the message catalogs

4.  use the `gettext` module so that message strings are properly translated

In order to prepare your code for I18N, you need to look at all the strings in your files. Any string that needs to be translated should be marked by wrapping it in `_(’...’)` – i.e. a call to the function `_()`. For example:

    filename = 'mylog.txt'
    message = _('writing a log message')
    fp = open(filename, 'w')
    fp.write(message)
    fp.close()

In this example, the string `’writing a log message’` is marked as a candidate for translation, while the strings `’mylog.txt’` and `’w’` are not.

The GNU `gettext` package provides a tool, called , that scans C and C++ source code looking for these specially marked strings. generates what are called `.pot` files, essentially structured human readable files which contain every marked string in the source code. These `.pot` files are copied and handed over to human translators who write language-specific versions for every supported natural language.

For I18N Python programs however, won’t work; it doesn’t understand the myriad of string types support by Python. The standard Python distribution provides a tool called that does though (found in the `Tools/i18n/` directory).[^3] This is a command line script that supports a similar interface as ; see its documentation for details. Once you’ve used to create your `.pot` files, you can use the standard GNU tools to generate your machine-readable `.mo` files, which are readable by the `GNUTranslations` class.

How you use the `gettext` module in your code depends on whether you are internationalizing your entire application or a single module.

### Localizing your module

If you are localizing your module, you must take care not to make global changes, e.g. to the built-in namespace. You should not use the GNU `gettext` API but instead the class-based API.

Let’s say your module is called “spam” and the module’s various natural language translation `.mo` files reside in `/usr/share/locale` in GNU format. Here’s what you would put at the top of your module:

    import gettext
    t = gettext.translation('spam', '/usr/share/locale')
    _ = t.gettext

If your translators were providing you with Unicode strings in their `.po` files, you’d instead do:

    import gettext
    t = gettext.translation('spam', '/usr/share/locale')
    _ = t.ugettext

### Localizing your application

If you are localizing your application, you can install the `_()` function globally into the built-in namespace, usually in the main driver file of your application. This will let all your application-specific files just use `_(’...’)` without having to explicitly install it in each file.

In the simple case then, you need only add the following bit of code to the main driver file of your application:

    import gettext
    gettext.install('myapplication')

If you need to set the locale directory or the *unicode* flag, you can pass these into the `install()` function:

    import gettext
    gettext.install('myapplication', '/usr/share/locale', unicode=1)

### Changing languages on the fly

If your program needs to support many languages at the same time, you may want to create multiple translation instances and then switch between them explicitly, like so:

    import gettext

    lang1 = gettext.translation(languages=['en'])
    lang2 = gettext.translation(languages=['fr'])
    lang3 = gettext.translation(languages=['de'])

    # start by using language1
    lang1.install()

    # ... time goes by, user selects language 2
    lang2.install()

    # ... more time goes by, user selects language 3
    lang3.install()

### Deferred translations

In most coding situations, strings are translated were they are coded. Occasionally however, you need to mark strings for translation, but defer actual translation until later. A classic example is:

    animals = ['mollusk',
               'albatross',
           'rat',
           'penguin',
           'python',
           ]
    # ...
    for a in animals:
        print a

Here, you want to mark the strings in the `animals` list as being translatable, but you don’t actually want to translate them until they are printed.

Here is one way you can handle this situation:

    def _(message): return message

    animals = [_('mollusk'),
               _('albatross'),
           _('rat'),
           _('penguin'),
           _('python'),
           ]

    del _

    # ...
    for a in animals:
        print _(a)

This works because the dummy definition of `_()` simply returns the string unchanged. And this dummy definition will temporarily override any definition of `_()` in the built-in namespace (until the command). Take care, though if you have a previous definition of `_` in the local namespace.

Note that the second use of `_()` will not identify “a” as being translatable to the program, since it is not a string.

Another way to handle this is with the following example:

    def N_(message): return message

    animals = [N_('mollusk'),
               N_('albatross'),
           N_('rat'),
           N_('penguin'),
           N_('python'),
           ]

    # ...
    for a in animals:
        print _(a)

In this case, you are marking translatable strings with the function `N_()`,[^4] which won’t conflict with any definition of `_()`. However, you will need to teach your message extraction program to look for translatable strings marked with `N_()`. and both support this through the use of command line switches.

## Acknowledgements

The following people contributed code, feedback, design suggestions, previous implementations, and valuable experience to the creation of this module:

- Peter Funk

- James Henstridge

- Marc-André Lemburg

- Martin von Löwis

- François Pinard

- Barry Warsaw

[^1]: The default locale directory is system dependent; e.g. on RedHat Linux it is `/usr/share/locale`, but on Solaris it is `/usr/lib/locale`. The `gettext` module does not try to support these system dependent defaults; instead its default is `sys.prefix``/share/locale`. For this reason, it is always best to call `bindtextdomain()` with an explicit absolute path at the start of your application.

[^2]: See the footnote for `bindtextdomain()` above.

[^3]: François Pinard has written a program called which does a similar job. It is available as part of his package at `http://www.iro.umontreal.ca/contrib/po-utils/HTML`.

[^4]: The choice of `N_()` here is totally arbitrary; it could have just as easily been `MarkThisStringForTranslation()`.
# `gopherlib` — Gopher protocol client

*Gopher protocol client (requires sockets).*\
This module provides a minimal implementation of client side of the the Gopher protocol. It is used by the module `urllib` to handle URLs that use the Gopher protocol.

The module defines the following functions:

<div class="funcdesc">

send_selectorselector, host Send a *selector* string to the gopher server at *host* and *port* (default `70`). Returns an open file object from which the returned document can be read.

</div>

<div class="funcdesc">

send_queryselector, query, host Send a *selector* string and a *query* string to a gopher server at *host* and *port* (default `70`). Returns an open file object from which the returned document can be read.

</div>

Note that the data returned by the Gopher server can be of any type, depending on the first character of the selector string. If the data is text (first character of the selector is `0`), lines are terminated by CRLF, and the data is terminated by a line consisting of a single `.`, and a leading `.` should be stripped from lines that begin with `..`. Directory listings (first character of the selector is `1`) are transferred using the same protocol.
# `httplib` — HTTP protocol client

*HTTP protocol client (requires sockets).*\
This module defines a class which implements the client side of the HTTP protocol. It is normally not used directly — the module `urllib`uses it to handle URLs that use HTTP.

The module defines one class, `HTTP`:

<div class="classdesc">

HTTP An `HTTP` instance represents one transaction with an HTTP server. It should be instantiated passing it a host and optional port number. If no port number is passed, the port is extracted from the host string if it has the form *`host`*`:`*`port`*, else the default HTTP port (80) is used. If no host is passed, no connection is made, and the `connect()` method should be used to connect to a server. For example, the following calls all create instances that connect to the server at the same host and port:

    >>> h1 = httplib.HTTP('www.cwi.nl')
    >>> h2 = httplib.HTTP('www.cwi.nl:80')
    >>> h3 = httplib.HTTP('www.cwi.nl', 80)

Once an `HTTP` instance has been connected to an HTTP server, it should be used as follows:

1.  Make exactly one call to the `putrequest()` method.

2.  Make zero or more calls to the `putheader()` method.

3.  Call the `endheaders()` method (this can be omitted if step 4 makes no calls).

4.  Optional calls to the `send()` method.

5.  Call the `getreply()` method.

6.  Call the `getfile()` method and read the data off the file object that it returns.

</div>

## HTTP Objects

`HTTP` instances have the following methods:

<div class="methoddesc">

set_debuglevellevel Set the debugging level (the amount of debugging output printed). The default debug level is `0`, meaning no debugging output is printed.

</div>

<div class="methoddesc">

connecthost Connect to the server given by *host* and *port*. See the intro for the default port. This should be called directly only if the instance was instantiated without passing a host.

</div>

<div class="methoddesc">

senddata Send data to the server. This should be used directly only after the `endheaders()` method has been called and before `getreply()` has been called.

</div>

<div class="methoddesc">

putrequestrequest, selector This should be the first call after the connection to the server has been made. It sends a line to the server consisting of the *request* string, the *selector* string, and the HTTP version (`HTTP/1.0`).

</div>

<div class="methoddesc">

putheaderheader, argument Send an style header to the server. It sends a line to the server consisting of the header, a colon and a space, and the first argument. If more arguments are given, continuation lines are sent, each consisting of a tab and an argument.

</div>

<div class="methoddesc">

endheaders Send a blank line to the server, signalling the end of the headers.

</div>

<div class="methoddesc">

getreply Complete the request by shutting down the sending end of the socket, read the reply from the server, and return a triple `(`*`replycode`*`, `*`message`*`, `*`headers`*`)`. Here, *replycode* is the integer reply code from the request (e.g., `200` if the request was handled properly); *message* is the message string corresponding to the reply code; and *headers* is an instance of the class `mimetools.Message` containing the headers received from the server. See the description of the `mimetools`module.

</div>

<div class="methoddesc">

getfile Return a file object from which the data returned by the server can be read, using the `read()`, `readline()` or `readlines()` methods.

</div>

## Examples

Here is an example session that uses the `GET` method:

    >>> import httplib
    >>> h = httplib.HTTP('www.cwi.nl')
    >>> h.putrequest('GET', '/index.html')
    >>> h.putheader('Accept', 'text/html')
    >>> h.putheader('Accept', 'text/plain')
    >>> h.endheaders()
    >>> errcode, errmsg, headers = h.getreply()
    >>> print errcode # Should be 200
    >>> f = h.getfile()
    >>> data = f.read() # Get the raw HTML
    >>> f.close()

Here is an example session that shows how to `POST` requests:

    >>> import httplib, urllib
    >>> params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
    >>> h = httplib.HTTP("www.musi-cal.com:80")
    >>> h.putrequest("POST", "/cgi-bin/query")
    >>> h.putheader("Content-length", "%d" % len(params))
    >>> h.putheader('Accept', 'text/plain')
    >>> h.putheader('Host', 'www.musi-cal.com')
    >>> h.endheaders()
    >>> h.send(paramstring)
    >>> reply, msg, hdrs = h.getreply()
    >>> print errcode # should be 200
    >>> data = h.getfile().read() # get the raw HTML
# `imageop` — Manipulate raw image data

*Manipulate raw image data.*\
The `imageop` module contains some useful operations on images. It operates on images consisting of 8 or 32 bit pixels stored in Python strings. This is the same format as used by `gl.lrectwrite()` and the `imgfile` module.

The module defines the following variables and functions:

<div class="excdesc">

error This exception is raised on all errors, such as unknown number of bits per pixel, etc.

</div>

<div class="funcdesc">

cropimage, psize, width, height, x0, y0, x1, y1 Return the selected part of *image*, which should by *width* by *height* in size and consist of pixels of *psize* bytes. *x0*, *y0*, *x1* and *y1* are like the `gl.lrectread()` parameters, i.e. the boundary is included in the new image. The new boundaries need not be inside the picture. Pixels that fall outside the old image will have their value set to zero. If *x0* is bigger than *x1* the new image is mirrored. The same holds for the y coordinates.

</div>

<div class="funcdesc">

scaleimage, psize, width, height, newwidth, newheight Return *image* scaled to size *newwidth* by *newheight*. No interpolation is done, scaling is done by simple-minded pixel duplication or removal. Therefore, computer-generated images or dithered images will not look nice after scaling.

</div>

<div class="funcdesc">

tovideoimage, psize, width, height Run a vertical low-pass filter over an image. It does so by computing each destination pixel as the average of two vertically-aligned source pixels. The main use of this routine is to forestall excessive flicker if the image is displayed on a video device that uses interlacing, hence the name.

</div>

<div class="funcdesc">

grey2monoimage, width, height, threshold Convert a 8-bit deep greyscale image to a 1-bit deep image by thresholding all the pixels. The resulting image is tightly packed and is probably only useful as an argument to `mono2grey()`.

</div>

<div class="funcdesc">

dither2monoimage, width, height Convert an 8-bit greyscale image to a 1-bit monochrome image using a (simple-minded) dithering algorithm.

</div>

<div class="funcdesc">

mono2greyimage, width, height, p0, p1 Convert a 1-bit monochrome image to an 8 bit greyscale or color image. All pixels that are zero-valued on input get value *p0* on output and all one-value input pixels get value *p1* on output. To convert a monochrome black-and-white image to greyscale pass the values `0` and `255` respectively.

</div>

<div class="funcdesc">

grey2grey4image, width, height Convert an 8-bit greyscale image to a 4-bit greyscale image without dithering.

</div>

<div class="funcdesc">

grey2grey2image, width, height Convert an 8-bit greyscale image to a 2-bit greyscale image without dithering.

</div>

<div class="funcdesc">

dither2grey2image, width, height Convert an 8-bit greyscale image to a 2-bit greyscale image with dithering. As for `dither2mono()`, the dithering algorithm is currently very simple.

</div>

<div class="funcdesc">

grey42greyimage, width, height Convert a 4-bit greyscale image to an 8-bit greyscale image.

</div>

<div class="funcdesc">

grey22greyimage, width, height Convert a 2-bit greyscale image to an 8-bit greyscale image.

</div>
# `imgfile` — Support for SGI imglib files

*Support for SGI imglib files.*\
The `imgfile` module allows Python programs to access SGI imglib image files (also known as `.rgb` files). The module is far from complete, but is provided anyway since the functionality that there is is enough in some cases. Currently, colormap files are not supported.

The module defines the following variables and functions:

<div class="excdesc">

error This exception is raised on all errors, such as unsupported file type, etc.

</div>

<div class="funcdesc">

getsizesfile This function returns a tuple `(`*`x`*`, `*`y`*`, `*`z`*`)` where *x* and *y* are the size of the image in pixels and *z* is the number of bytes per pixel. Only 3 byte RGB pixels and 1 byte greyscale pixels are currently supported.

</div>

<div class="funcdesc">

readfile This function reads and decodes the image on the specified file, and returns it as a Python string. The string has either 1 byte greyscale pixels or 4 byte RGBA pixels. The bottom left pixel is the first in the string. This format is suitable to pass to `gl.lrectwrite()`, for instance.

</div>

<div class="funcdesc">

readscaledfile, x, y, filter This function is identical to read but it returns an image that is scaled to the given *x* and *y* sizes. If the *filter* and *blur* parameters are omitted scaling is done by simply dropping or duplicating pixels, so the result will be less than perfect, especially for computer-generated images.

Alternatively, you can specify a filter to use to smoothen the image after scaling. The filter forms supported are `’impulse’`, `’box’`, `’triangle’`, `’quadratic’` and `’gaussian’`. If a filter is specified *blur* is an optional parameter specifying the blurriness of the filter. It defaults to `1.0`.

`readscaled()` makes no attempt to keep the aspect ratio correct, so that is the users’ responsibility.

</div>

<div class="funcdesc">

ttobflag This function sets a global flag which defines whether the scan lines of the image are read or written from bottom to top (flag is zero, compatible with SGI GL) or from top to bottom(flag is one, compatible with X). The default is zero.

</div>

<div class="funcdesc">

writefile, data, x, y, z This function writes the RGB or greyscale data in *data* to image file *file*. *x* and *y* give the size of the image, *z* is 1 for 1 byte greyscale images or 3 for RGB images (which are stored as 4 byte values of which only the lower three bytes are used). These are the formats returned by `gl.lrectread()`.

</div>
# `imghdr` — Determine the type of an image.

*Determine the type of image contained in a file or byte stream.*\
The `imghdr` module determines the type of image contained in a file or byte stream.

The `imghdr` module defines the following function:

<div class="funcdesc">

whatfilename Tests the image data contained in the file named by *filename*, and returns a string describing the image type. If optional *h* is provided, the *filename* is ignored and *h* is assumed to contain the byte stream to test.

</div>

The following image types are recognized, as listed below with the return value from `what()`:

|                         |                           |
|:------------------------|:--------------------------|
| ValueImage format ’rgb’ | SGI ImgLib Files          |
| ’gif’                   | GIF 87a and 89a Files     |
| ’pbm’                   | Portable Bitmap Files     |
| ’pgm’                   | Portable Graymap Files    |
| ’ppm’                   | Portable Pixmap Files     |
| ’tiff’                  | TIFF Files                |
| ’rast’                  | Sun Raster Files          |
| ’xbm’                   | X Bitmap Files            |
| ’jpeg’                  | JPEG data in JFIF format  |
| ’bmp’                   | BMP files                 |
| ’png’                   | Portable Network Graphics |
|                         |                           |

You can extend the list of file types `imghdr` can recognize by appending to this variable:

<div class="datadesc">

tests A list of functions performing the individual tests. Each function takes two arguments: the byte-stream and an open file-like object. When `what()` is called with a byte-stream, the file-like object will be `None`.

The test function should return a string describing the image type if the test succeeded, or `None` if it failed.

</div>

Example:

    >>> import imghdr
    >>> imghdr.what('/tmp/bass.gif')
    'gif'
# `imp` — Access the internals

*Access the implementation of the statement.*\
Thismodule provides an interface to the mechanisms used to implement the statement. It defines the following constants and functions:

<div class="funcdesc">

get_magic Return the magic string value used to recognize byte-compiled code files (`.pyc` files). (This value may be different for each Python version.)

</div>

<div class="funcdesc">

get_suffixes Return a list of triples, each describing a particular type of module. Each triple has the form `(`*`suffix`*`, `*`mode`*`, `*`type`*`)`, where *suffix* is a string to be appended to the module name to form the filename to search for, *mode* is the mode string to pass to the built-in `open()` function to open the file (this can be `’r’` for text files or `’rb’` for binary files), and *type* is the file type, which has one of the values , , or , described below.

</div>

<div class="funcdesc">

find_modulename Try to find the module *name* on the search path *path*. If *path* is a list of directory names, each directory is searched for files with any of the suffixes returned by `get_suffixes()` above. Invalid names in the list are silently ignored (but all list items must be strings). If *path* is omitted or `None`, the list of directory names given by `sys.path` is searched, but first it searches a few special places: it tries to find a built-in module with the given name (), then a frozen module (), and on some systems some other places are looked in as well (on the Mac, it looks for a resource (); on Windows, it looks in the registry which may point to a specific file).

If search is successful, the return value is a triple `(`*`file`*`, `*`pathname`*`, `*`description`*`)` where *file* is an open file object positioned at the beginning, *pathname* is the pathname of the file found, and *description* is a triple as contained in the list returned by `get_suffixes()` describing the kind of module found. If the module does not live in a file, the returned *file* is `None`, *filename* is the empty string, and the *description* tuple contains empty strings for its suffix and mode; the module type is as indicate in parentheses above. If the search is unsuccessful, `ImportError` is raised. Other exceptions indicate problems with the arguments or environment.

This function does not handle hierarchical module names (names containing dots). In order to find *P*.*M*, i.e., submodule *M* of package *P*, use `find_module()` and `load_module()` to find and load package *P*, and then use `find_module()` with the *path* argument set to *`P`*`.__path__`. When *P* itself has a dotted name, apply this recipe recursively.

</div>

<div class="funcdesc">

load_modulename, file, filename, description Load a module that was previously found by `find_module()` (or by an otherwise conducted search yielding compatible results). This function does more than importing the module: if the module was already imported, it is equivalent to a `reload()`! The *name* argument indicates the full module name (including the package name, if this is a submodule of a package). The *file* argument is an open file, and *filename* is the corresponding file name; these can be `None` and `’’`, respectively, when the module is not being loaded from a file. The *description* argument is a tuple as returned by `find_module()` describing what kind of module must be loaded.

If the load is successful, the return value is the module object; otherwise, an exception (usually `ImportError`) is raised.

**Important:** the caller is responsible for closing the *file* argument, if it was not `None`, even when an exception is raised. This is best done using a ... statement.

</div>

<div class="funcdesc">

new_modulename Return a new empty module object called *name*. This object is *not* inserted in `sys.modules`.

</div>

The following constants with integer values, defined in this module, are used to indicate the search result of `find_module()`.

<div class="datadesc">

PY_SOURCE The module was found as a source file.

</div>

<div class="datadesc">

PY_COMPILED The module was found as a compiled code object file.

</div>

<div class="datadesc">

C_EXTENSION The module was found as dynamically loadable shared library.

</div>

<div class="datadesc">

PY_RESOURCE The module was found as a Macintosh resource. This value can only be returned on a Macintosh.

</div>

<div class="datadesc">

PKG_DIRECTORY The module was found as a package directory.

</div>

<div class="datadesc">

C_BUILTIN The module was found as a built-in module.

</div>

<div class="datadesc">

PY_FROZEN The module was found as a frozen module (see `init_frozen()`).

</div>

The following constant and functions are obsolete; their functionality is available through `find_module()` or `load_module()`. They are kept around for backward compatibility:

<div class="datadesc">

SEARCH_ERROR Unused.

</div>

<div class="funcdesc">

init_builtinname Initialize the built-in module called *name* and return its module object. If the module was already initialized, it will be initialized *again*. A few modules cannot be initialized twice — attempting to initialize these again will raise an `ImportError` exception. If there is no built-in module called *name*, `None` is returned.

</div>

<div class="funcdesc">

init_frozenname Initialize the frozen module called *name* and return its module object. If the module was already initialized, it will be initialized *again*. If there is no frozen module called *name*, `None` is returned. (Frozen modules are modules written in Python whose compiled byte-code object is incorporated into a custom-built Python interpreter by Python’s utility. See `Tools/freeze/` for now.)

</div>

<div class="funcdesc">

is_builtinname Return `1` if there is a built-in module called *name* which can be initialized again. Return `-1` if there is a built-in module called *name* which cannot be initialized again (see `init_builtin()`). Return `0` if there is no built-in module called *name*.

</div>

<div class="funcdesc">

is_frozenname Return `1` if there is a frozen module (see `init_frozen()`) called *name*, or `0` if there is no such module.

</div>

<div class="funcdesc">

load_compiledname, pathname, file Load and initialize a module implemented as a byte-compiled code file and return its module object. If the module was already initialized, it will be initialized *again*. The *name* argument is used to create or access a module object. The *pathname* argument points to the byte-compiled code file. The *file* argument is the byte-compiled code file, open for reading in binary mode, from the beginning. It must currently be a real file object, not a user-defined class emulating a file.

</div>

<div class="funcdesc">

load_dynamicname, pathname Load and initialize a module implemented as a dynamically loadable shared library and return its module object. If the module was already initialized, it will be initialized *again*. Some modules don’t like that and may raise an exception. The *pathname* argument must point to the shared library. The *name* argument is used to construct the name of the initialization function: an external C function called `init`*`name`*`()` in the shared library is called. The optional *file* argument is ignored. (Note: using shared libraries is highly system dependent, and not all systems support it.)

</div>

<div class="funcdesc">

load_sourcename, pathname, file Load and initialize a module implemented as a Python source file and return its module object. If the module was already initialized, it will be initialized *again*. The *name* argument is used to create or access a module object. The *pathname* argument points to the source file. The *file* argument is the source file, open for reading as text, from the beginning. It must currently be a real file object, not a user-defined class emulating a file. Note that if a properly matching byte-compiled file (with suffix `.pyc` or `.pyo`) exists, it will be used instead of parsing the given source file.

</div>

## Examples

The following function emulates what was the standard import statement up to Python 1.4 (i.e., no hierarchical module names). (This *implementation* wouldn’t work in that version, since `find_module()` has been extended and `load_module()` has been added in 1.4.)

    import imp import sys

    def __import__(name, globals=None, locals=None, fromlist=None):
        # Fast path: see if the module has already been imported.
        try:
            return sys.modules[name]
        except KeyError:
            pass

        # If any of the following calls raises an exception,
        # there's a problem we can't handle -- let the caller handle it.

        fp, pathname, description = imp.find_module(name)
        
        try:
            return imp.load_module(name, fp, pathname, description)
        finally:
            # Since we may exit via an exception, close fp explicitly.
            if fp:
                fp.close()

A more complete example that implements hierarchical module names and includes a `reload()`function can be found in the standard module `knee`(which is intended as an example only — don’t rely on any part of it being a standard interface).
# Introduction

The “Python library” contains several different kinds of components.

It contains data types that would normally be considered part of the “core” of a language, such as numbers and lists. For these types, the Python language core defines the form of literals and places some constraints on their semantics, but does not fully define the semantics. (On the other hand, the language core does define syntactic properties like the spelling and priorities of operators.)

The library also contains built-in functions and exceptions — objects that can be used by all Python code without the need of an statement. Some of these are defined by the core language, but many are not essential for the core semantics and are only described here.

The bulk of the library, however, consists of a collection of modules. There are many ways to dissect this collection. Some modules are written in C and built in to the Python interpreter; others are written in Python and imported in source form. Some modules provide interfaces that are highly specific to Python, like printing a stack trace; some provide interfaces that are specific to particular operating systems, such as access to specific hardware; others provide interfaces that are specific to a particular application domain, like the World-Wide Web. Some modules are available in all versions and ports of Python; others are only available when the underlying system supports or requires them; yet others are available only when a particular configuration option was chosen at the time when Python was compiled and installed.

This manual is organized “from the inside out:” it first describes the built-in data types, then the built-in functions and exceptions, and finally the modules, grouped in chapters of related modules. The ordering of the chapters as well as the ordering of the modules within each chapter is roughly from most relevant to least important.

This means that if you start reading this manual from the start, and skip to the next chapter when you get bored, you will get a reasonable overview of the available modules and application areas that are supported by the Python library. Of course, you don’t *have* to read it like a novel — you can also browse the table of contents (in front of the manual), or look for a specific function, module or term in the index (in the back). And finally, if you enjoy learning about random subjects, you choose a random page number (see module `random`) and read a section or two. Regardless of the order in which you read the sections of this manual, it helps to start with chapter <a href="#builtin" data-reference-type="ref" data-reference="builtin">[builtin]</a>, “Built-in Types, Exceptions and Functions,” as the remainder of the manual assumes familiarity with this material.

Let the show begin!
# `keyword` — Testing for Python keywords

*Test whether a string is a keyword in Python.*\
This module allows a Python program to determine if a string is a keyword. A single function is provided:

<div class="funcdesc">

iskeywords Return true if *s* is a Python keyword.

</div>
# `linecache` — Random access to text lines

*This module provides random access to individual lines from text files.*\
The `linecache` module allows one to get any line from any file, while attempting to optimize internally, using a cache, the common case where many lines are read from a single file. This is used by the `traceback` module to retrieve source lines for inclusion in the formatted traceback.

The `linecache` module defines the following functions:

<div class="funcdesc">

getlinefilename, lineno Get line *lineno* from file named *filename*. This function will never throw an exception — it will return `’’` on errors (the terminating newline character will be included for lines that are found).

If a file named *filename* is not found, the function will look for it in the modulesearch path, `sys.path`.

</div>

<div class="funcdesc">

clearcache Clear the cache. Use this function if you no longer need lines from files previously read using `getline()`.

</div>

<div class="funcdesc">

checkcache Check the cache for validity. Use this function if files in the cache may have changed on disk, and you require the updated version.

</div>

Example:

    >>> import linecache
    >>> linecache.getline('/etc/passwd', 4)
    'sys:x:3:3:sys:/dev:/bin/sh\012'
# `locale` — Internationalization services

*Internationalization services.*\
The `locale` module opens access to the locale database and functionality. The locale mechanism allows programmers to deal with certain cultural issues in an application, without requiring the programmer to know all the specifics of each country where the software is executed.

The `locale` module is implemented on top of the `_locale`module, which in turn uses an ANSI C locale implementation if available.

The `locale` module defines the following exception and functions:

<div class="funcdesc">

setlocalecategory If *value* is specified, modifies the locale setting for the *category*. The available categories are listed in the data description below. The value is the name of a locale. An empty string specifies the user’s default settings. If the modification of the locale fails, the exception `Error` is raised. If successful, the new locale setting is returned.

If no *value* is specified, the current setting for the *category* is returned.

`setlocale()` is not thread safe on most systems. Applications typically start with a call of

    import locale
    locale.setlocale(locale.LC_ALL,"")

This sets the locale for all categories to the user’s default setting (typically specified in the environment variable). If the locale is not changed thereafter, using multithreading should not cause problems.

</div>

<div class="excdesc">

Error Exception raised when `setlocale()` fails.

</div>

<div class="funcdesc">

localeconv Returns the database of of the local conventions as a dictionary. This dictionary has the following strings as keys:

- `decimal_point` specifies the decimal point used in floating point number representations for the category.

- `grouping` is a sequence of numbers specifying at which relative positions the `thousands_sep` is expected. If the sequence is terminated with , no further grouping is performed. If the sequence terminates with a `0`, the last group size is repeatedly used.

- `thousands_sep` is the character used between groups.

- `int_curr_symbol` specifies the international currency symbol from the category.

- `currency_symbol` is the local currency symbol.

- `mon_decimal_point` is the decimal point used in monetary values.

- `mon_thousands_sep` is the separator for grouping of monetary values.

- `mon_grouping` has the same format as the `grouping` key; it is used for monetary values.

- `positive_sign` and `negative_sign` gives the sign used for positive and negative monetary quantities.

- `int_frac_digits` and `frac_digits` specify the number of fractional digits used in the international and local formatting of monetary values.

- `p_cs_precedes` and `n_cs_precedes` specifies whether the currency symbol precedes the value for positive or negative values.

- `p_sep_by_space` and `n_sep_by_space` specifies whether there is a space between the positive or negative value and the currency symbol.

- `p_sign_posn` and `n_sign_posn` indicate how the sign should be placed for positive and negative monetary values.

The possible values for `p_sign_posn` and `n_sign_posn` are given below.

|                    |                                                        |
|:-------------------|:-------------------------------------------------------|
| ValueExplanation 0 | Currency and value are surrounded by parentheses.      |
| 1                  | The sign should precede the value and currency symbol. |
| 2                  | The sign should follow the value and currency symbol.  |
| 3                  | The sign should immediately precede the value.         |
| 4                  | The sign should immediately follow the value.          |
| LC_MAX             | Nothing is specified in this locale.                   |
|                    |                                                        |

</div>

<div class="funcdesc">

strcollstring1,string2 Compares two strings according to the current setting. As any other compare function, returns a negative, or a positive value, or `0`, depending on whether *string1* collates before or after *string2* or is equal to it.

</div>

<div class="funcdesc">

strxfrmstring Transforms a string to one that can be used for the built-in function `cmp()`, and still returns locale-aware results. This function can be used when the same string is compared repeatedly, e.g. when collating a sequence of strings.

</div>

<div class="funcdesc">

formatformat, val, Formats a number *val* according to the current setting. The format follows the conventions of the `%` operator. For floating point values, the decimal point is modified if appropriate. If *grouping* is true, also takes the grouping into account.

</div>

<div class="funcdesc">

strfloat Formats a floating point number using the same format as the built-in function `str(`*`float`*`)`, but takes the decimal point into account.

</div>

<div class="funcdesc">

atofstring Converts a string to a floating point number, following the settings.

</div>

<div class="funcdesc">

atoistring Converts a string to an integer, following the conventions.

</div>

<div class="datadesc">

LC_CTYPE Locale category for the character type functions. Depending on the settings of this category, the functions of module `string` dealing with case change their behaviour.

</div>

<div class="datadesc">

LC_COLLATE Locale category for sorting strings. The functions `strcoll()` and `strxfrm()` of the `locale` module are affected.

</div>

<div class="datadesc">

LC_TIME Locale category for the formatting of time. The function `time.strftime()` follows these conventions.

</div>

<div class="datadesc">

LC_MONETARY Locale category for formatting of monetary values. The available options are available from the `localeconv()` function.

</div>

<div class="datadesc">

LC_MESSAGES Locale category for message display. Python currently does not support application specific locale-aware messages. Messages displayed by the operating system, like those returned by `os.strerror()` might be affected by this category.

</div>

<div class="datadesc">

LC_NUMERIC Locale category for formatting numbers. The functions `format()`, `atoi()`, `atof()` and `str()` of the `locale` module are affected by that category. All other numeric formatting operations are not affected.

</div>

<div class="datadesc">

LC_ALL Combination of all locale settings. If this flag is used when the locale is changed, setting the locale for all categories is attempted. If that fails for any category, no category is changed at all. When the locale is retrieved using this flag, a string indicating the setting for all categories is returned. This string can be later used to restore the settings.

</div>

<div class="datadesc">

CHAR_MAX This is a symbolic constant used for different values returned by `localeconv()`.

</div>

Example:

    >>> import locale
    >>> loc = locale.setlocale(locale.LC_ALL) # get current locale
    >>> locale.setlocale(locale.LC_ALL, "de") # use German locale
    >>> locale.strcoll("f\344n", "foo") # compare a string containing an umlaut 
    >>> locale.setlocale(locale.LC_ALL, "") # use user's preferred locale
    >>> locale.setlocale(locale.LC_ALL, "C") # use default (C) locale
    >>> locale.setlocale(locale.LC_ALL, loc) # restore saved locale

## Background, details, hints, tips and caveats

The C standard defines the locale as a program-wide property that may be relatively expensive to change. On top of that, some implementation are broken in such a way that frequent locale changes may cause core dumps. This makes the locale somewhat painful to use correctly.

Initially, when a program is started, the locale is the `C` locale, no matter what the user’s preferred locale is. The program must explicitly say that it wants the user’s preferred locale settings by calling `setlocale(LC_ALL, "")`.

It is generally a bad idea to call `setlocale()` in some library routine, since as a side effect it affects the entire program. Saving and restoring it is almost as bad: it is expensive and affects other threads that happen to run before the settings have been restored.

If, when coding a module for general use, you need a locale independent version of an operation that is affected by the locale (e.g. `string.lower()`, or certain formats used with `time.strftime()`)), you will have to find a way to do it without using the standard library routine. Even better is convincing yourself that using locale settings is okay. Only as a last resort should you document that your module is not compatible with non-`C` locale settings.

The case conversion functions in the `string`and `strop`modules are affected by the locale settings. When a call to the `setlocale()` function changes the settings, the variables `string.lowercase`, `string.uppercase` and `string.letters` (and their counterparts in `strop`) are recalculated. Note that this code that uses these variable through ‘ ... ...’, e.g. `from string import letters`, is not affected by subsequent `setlocale()` calls.

The only way to perform numeric operations according to the locale is to use the special functions defined by this module: `atof()`, `atoi()`, `format()`, `str()`.

## For extension writers and programs that embed Python

Extension modules should never call `setlocale()`, except to find out what the current locale is. But since the return value can only be used portably to restore it, that is not very useful (except perhaps to find out whether or not the locale is `C`).

When Python is embedded in an application, if the application sets the locale to something specific before initializing Python, that is generally okay, and Python will use whatever locale is set, *except* that the locale should always be `C`.

The `setlocale()` function in the `locale` module gives the Python programmer the impression that you can manipulate the locale setting, but this not the case at the C level: C code will always find that the locale setting is `C`. This is because too much would break when the decimal point character is set to something else than a period (e.g. the Python parser would break). Caveat: threads that run without holding Python’s global interpreter lock may occasionally find that the numeric locale setting differs; this is because the only portable way to implement this feature is to set the numeric locale settings to what the user requests, extract the relevant characteristics, and then restore the `C` numeric locale.

When Python code uses the `locale` module to change the locale, this also affects the embedding application. If the embedding application doesn’t want this to happen, it should remove the `_locale` extension module (which does all the work) from the table of built-in modules in the `config.c` file, and make sure that the `_locale` module is not accessible as a shared library.
# `mailbox` — Read various mailbox formats

*Read various mailbox formats.*\
This module defines a number of classes that allow easy and uniform access to mail messages in a (Unix) mailbox.

<div class="classdesc">

UnixMailboxfp Access a classic Unix-style mailbox, where all messages are contained in a single file and separated by “From name time” lines. The file object *fp* points to the mailbox file.

</div>

<div class="classdesc">

MmdfMailboxfp Access an MMDF-style mailbox, where all messages are contained in a single file and separated by lines consisting of 4 control-A characters. The file object *fp* points to the mailbox file.

</div>

<div class="classdesc">

MHMailboxdirname Access an MH mailbox, a directory with each message in a separate file with a numeric name. The name of the mailbox directory is passed in *dirname*.

</div>

<div class="classdesc">

Maildirdirname Access a Qmail mail directory. All new and current mail for the mailbox specified by *dirname* is made available.

</div>

<div class="classdesc">

BabylMailboxfp Access a Babyl mailbox, which is similar to an MMDF mailbox. Mail messages start with a line containing only `’*** EOOH ***’` and end with a line containing only `’037014’`.

</div>

## Mailbox Objects <span id="mailbox-objects" label="mailbox-objects"></span>

All implementations of Mailbox objects have one externally visible method:

<div class="methoddesc">

next Return the next message in the mailbox, as a `rfc822.Message` object (see the `rfc822` module). Depending on the mailbox implementation the *fp* attribute of this object may be a true file object or a class instance simulating a file object, taking care of things like message boundaries if multiple mail messages are contained in a single file, etc.

</div>
# `mailcap` — Mailcap file handling.

*Mailcap file handling.*\
Mailcap files are used to configure how MIME-aware applications such as mail readers and Web browsers react to files with different MIME types. (The name “mailcap” is derived from the phrase “mail capability”.) For example, a mailcap file might contain a line like `video/mpeg; xmpeg %s`. Then, if the user encounters an email message or Web document with the MIME type , `%s` will be replaced by a filename (usually one belonging to a temporary file) and the program can be automatically started to view the file.

The mailcap format is documented in , “A User Agent Configuration Mechanism For Multimedia Mail Format Information,” but is not an Internet standard. However, mailcap files are supported on most Unix systems.

<div class="funcdesc">

findmatchcaps, MIMEtype Return a 2-tuple; the first element is a string containing the command line to be executed (which can be passed to `os.system()`), and the second element is the mailcap entry for a given MIME type. If no matching MIME type can be found, `(None, None)` is returned.

*key* is the name of the field desired, which represents the type of activity to be performed; the default value is ’view’, since in the most common case you simply want to view the body of the MIME-typed data. Other possible values might be ’compose’ and ’edit’, if you wanted to create a new body of the given MIME type or alter the existing body data. See for a complete list of these fields.

*filename* is the filename to be substituted for `%s` in the command line; the default value is `’/dev/null’` which is almost certainly not what you want, so usually you’ll override it by specifying a filename.

*plist* can be a list containing named parameters; the default value is simply an empty list. Each entry in the list must be a string containing the parameter name, an equals sign (`=`), and the parameter’s value. Mailcap entries can contain named parameters like `%{foo}`, which will be replaced by the value of the parameter named ’foo’. For example, if the command line `showpartial %{id} %{number} %{total}` was in a mailcap file, and *plist* was set to `[’id=1’, ’number=2’, ’total=3’]`, the resulting command line would be `"showpartial 1 2 3"`.

In a mailcap file, the "test" field can optionally be specified to test some external condition (e.g., the machine architecture, or the window system in use) to determine whether or not the mailcap line applies. `findmatch()` will automatically check such conditions and skip the entry if the check fails.

</div>

<div class="funcdesc">

getcaps Returns a dictionary mapping MIME types to a list of mailcap file entries. This dictionary must be passed to the `findmatch()` function. An entry is stored as a list of dictionaries, but it shouldn’t be necessary to know the details of this representation.

The information is derived from all of the mailcap files found on the system. Settings in the user’s mailcap file `$HOME/.mailcap` will override settings in the system mailcap files `/etc/mailcap`, `/usr/etc/mailcap`, and `/usr/local/etc/mailcap`.

</div>

An example usage:

    >>> import mailcap
    >>> d=mailcap.getcaps()
    >>> mailcap.findmatch(d, 'video/mpeg', filename='/tmp/tmp1223')
    ('xmpeg /tmp/tmp1223', {'view': 'xmpeg %s'})
# `__main__` — Top-level script environment

*The environment where the top-level script is run.*\
This module represents the (otherwise anonymous) scope in which the interpreter’s main program executes — commands read either from standard input, from a script file, or from an interactive prompt. It is this environment in which the idiomatic “conditional script” stanza causes a script to run:

    if __name__ == "__main__":
        main()
# `marshal` — Alternate Python object serialization

*Convert Python objects to streams of bytes and back (with different constraints).*\
This module contains functions that can read and write Python values in a binary format. The format is specific to Python, but independent of machine architecture issues (e.g., you can write a Python value to a file on a PC, transport the file to a Sun, and read it back there). Details of the format are undocumented on purpose; it may change between Python versions (although it rarely does).[^1]

This is not a general “persistence” module. For general persistence and transfer of Python objects through RPC calls, see the modules `pickle` and `shelve`. The `marshal` module exists mainly to support reading and writing the “pseudo-compiled” code for Python modules of `.pyc` files. Not all Python object types are supported; in general, only objects whose value is independent from a particular invocation of Python can be written and read by this module. The following types are supported: `None`, integers, long integers, floating point numbers, strings, Unicode objects, tuples, lists, dictionaries, and code objects, where it should be understood that tuples, lists and dictionaries are only supported as long as the values contained therein are themselves supported; and recursive lists and dictionaries should not be written (they will cause infinite loops).

**Caveat:** On machines where C’s `long int` type has more than 32 bits (such as the DEC Alpha), it is possible to create plain Python integers that are longer than 32 bits. Since the current `marshal` module uses 32 bits to transfer plain Python integers, such values are silently truncated. This particularly affects the use of very long integer literals in Python modules — these will be accepted by the parser on such machines, but will be silently be truncated when the module is read from the `.pyc` instead.[^2]

There are functions that read/write files as well as functions operating on strings.

The module defines these functions:

<div class="funcdesc">

dumpvalue, file Write the value on the open file. The value must be a supported type. The file must be an open file object such as `sys.stdout` or returned by `open()` or `posix.popen()`. It must be opened in binary mode (`’wb’` or `’w+b’`).

If the value has (or contains an object that has) an unsupported type, a `ValueError` exception is raised — but garbage data will also be written to the file. The object will not be properly read back by `load()`.

</div>

<div class="funcdesc">

loadfile Read one value from the open file and return it. If no valid value is read, raise `EOFError`, `ValueError` or `TypeError`. The file must be an open file object opened in binary mode (`’rb’` or `’r+b’`).

**Warning:** If an object containing an unsupported type was marshalled with `dump()`, `load()` will substitute `None` for the unmarshallable type.

</div>

<div class="funcdesc">

dumpsvalue Return the string that would be written to a file by `dump(`*`value`*`, `*`file`*`)`. The value must be a supported type. Raise a `ValueError` exception if value has (or contains an object that has) an unsupported type.

</div>

<div class="funcdesc">

loadsstring Convert the string to a value. If no valid value is found, raise `EOFError`, `ValueError` or `TypeError`. Extra characters in the string are ignored.

</div>

[^1]: The name of this module stems from a bit of terminology used by the designers of Modula-3 (amongst others), who use the term “marshalling” for shipping of data around in a self-contained form. Strictly speaking, “to marshal” means to convert some data from internal to external form (in an RPC buffer for instance) and “unmarshalling” for the reverse process.

[^2]: A solution would be to refuse such literals in the parser, since they are inherently non-portable. Another solution would be to let the `marshal` module raise an exception when an integer value would be truncated. At least one of these solutions will be implemented in a future version.
# `mhlib` — Access to MH mailboxes

*Manipulate MH mailboxes from Python.*\
The `mhlib` module provides a Python interface to MH folders and their contents.

The module contains three basic classes, `MH`, which represents a particular collection of folders, `Folder`, which represents a single folder, and `Message`, which represents a single message.

<div class="classdesc">

MH `MH` represents a collection of MH folders.

</div>

<div class="classdesc">

Foldermh, name The `Folder` class represents a single folder and its messages.

</div>

<div class="classdesc">

Messagefolder, number `Message` objects represent individual messages in a folder. The Message class is derived from `mimetools.Message`.

</div>

## MH Objects <span id="mh-objects" label="mh-objects"></span>

`MH` instances have the following methods:

<div class="methoddesc">

errorformat Print an error message – can be overridden.

</div>

<div class="methoddesc">

getprofilekey Return a profile entry (`None` if not set).

</div>

<div class="methoddesc">

getpath Return the mailbox pathname.

</div>

<div class="methoddesc">

getcontext Return the current folder name.

</div>

<div class="methoddesc">

setcontextname Set the current folder name.

</div>

<div class="methoddesc">

listfolders Return a list of top-level folders.

</div>

<div class="methoddesc">

listallfolders Return a list of all folders.

</div>

<div class="methoddesc">

listsubfoldersname Return a list of direct subfolders of the given folder.

</div>

<div class="methoddesc">

listallsubfoldersname Return a list of all subfolders of the given folder.

</div>

<div class="methoddesc">

makefoldername Create a new folder.

</div>

<div class="methoddesc">

deletefoldername Delete a folder – must have no subfolders.

</div>

<div class="methoddesc">

openfoldername Return a new open folder object.

</div>

## Folder Objects <span id="mh-folder-objects" label="mh-folder-objects"></span>

`Folder` instances represent open folders and have the following methods:

<div class="methoddesc">

errorformat Print an error message – can be overridden.

</div>

<div class="methoddesc">

getfullname Return the folder’s full pathname.

</div>

<div class="methoddesc">

getsequencesfilename Return the full pathname of the folder’s sequences file.

</div>

<div class="methoddesc">

getmessagefilenamen Return the full pathname of message *n* of the folder.

</div>

<div class="methoddesc">

listmessages Return a list of messages in the folder (as numbers).

</div>

<div class="methoddesc">

getcurrent Return the current message number.

</div>

<div class="methoddesc">

setcurrentn Set the current message number to *n*.

</div>

<div class="methoddesc">

parsesequenceseq Parse msgs syntax into list of messages.

</div>

<div class="methoddesc">

getlast Get last message, or `0` if no messages are in the folder.

</div>

<div class="methoddesc">

setlastn Set last message (internal use only).

</div>

<div class="methoddesc">

getsequences Return dictionary of sequences in folder. The sequence names are used as keys, and the values are the lists of message numbers in the sequences.

</div>

<div class="methoddesc">

putsequencesdict Return dictionary of sequences in folder name: list.

</div>

<div class="methoddesc">

removemessageslist Remove messages in list from folder.

</div>

<div class="methoddesc">

refilemessageslist, tofolder Move messages in list to other folder.

</div>

<div class="methoddesc">

movemessagen, tofolder, ton Move one message to a given destination in another folder.

</div>

<div class="methoddesc">

copymessagen, tofolder, ton Copy one message to a given destination in another folder.

</div>

## Message Objects <span id="mh-message-objects" label="mh-message-objects"></span>

The `Message` class adds one method to those of `mimetools.Message`:

<div class="methoddesc">

openmessagen Return a new open message object (costs a file descriptor).

</div>
# `mimetypes` — Map filenames to MIME types

*Mapping of filename extensions to MIME types.*\
The `mimetypes` converts between a filename or URL and the MIME type associated with the filename extension. Conversions are provided from filename to MIME type and from MIME type to filename extension; encodings are not supported for the later conversion.

The functions described below provide the primary interface for this module. If the module has not been initialized, they will call `init()`.

<div class="funcdesc">

guess_typefilename Guess the type of a file based on its filename or URL, given by *filename*. The return value is a tuple `(`*`type`*`, `*`encoding`*`)` where *type* is `None` if the type can’t be guessed (no or unknown suffix) or a string of the form `’`*`type`*`/`*`subtype`*`’`, usable for a MIME `content-type` header; and encoding is `None` for no encoding or the name of the program used to encode (e.g. or ). The encoding is suitable for use as a `content-encoding` header, *not* as a `content-transfer-encoding` header. The mappings are table driven. Encoding suffixes are case sensitive; type suffixes are first tried case sensitive, then case insensitive.

</div>

<div class="funcdesc">

guess_extensiontype Guess the extension for a file based on its MIME type, given by *type*. The return value is a string giving a filename extension, including the leading dot (). The extension is not guaranteed to have been associated with any particular data stream, but would be mapped to the MIME type *type* by `guess_type()`. If no extension can be guessed for *type*, `None` is returned.

</div>

Some additional functions and data items are available for controlling the behavior of the module.

<div class="funcdesc">

init Initialize the internal data structures. If given, *files* must be a sequence of file names which should be used to augment the default type map. If omitted, the file names to use are taken from `knownfiles`. Each file named in *files* or `knownfiles` takes precedence over those named before it. Calling `init()` repeatedly is allowed.

</div>

<div class="funcdesc">

read_mime_typesfilename Load the type map given in the file *filename*, if it exists. The type map is returned as a dictionary mapping filename extensions, including the leading dot (), to strings of the form `’`*`type`*`/`*`subtype`*`’`. If the file *filename* does not exist or cannot be read, `None` is returned.

</div>

<div class="datadesc">

inited Flag indicating whether or not the global data structures have been initialized. This is set to true by `init()`.

</div>

<div class="datadesc">

knownfiles List of type map file names commonly installed. These files are typically named `mime.types` and are installed in different locations by different packages.

</div>

<div class="datadesc">

suffix_map Dictionary mapping suffixes to suffixes. This is used to allow recognition of encoded files for which the encoding and the type are indicated by the same extension. For example, the `.tgz` extension is mapped to `.tar.gz` to allow the encoding and type to be recognized separately.

</div>

<div class="datadesc">

encodings_map Dictionary mapping filename extensions to encoding types.

</div>

<div class="datadesc">

types_map Dictionary mapping filename extensions to MIME types.

</div>
# `MimeWriter` — Generic MIME file writer

*Generic MIME file writer.*\
This module defines the class `MimeWriter`. The `MimeWriter` class implements a basic formatter for creating MIME multi-part files. It doesn’t seek around the output file nor does it use large amounts of buffer space. You must write the parts out in the order that they should occur in the final file. `MimeWriter` does buffer the headers you add, allowing you to rearrange their order.

<div class="classdesc">

MimeWriterfp Return a new instance of the `MimeWriter` class. The only argument passed, *fp*, is a file object to be used for writing. Note that a `StringIO` object could also be used.

</div>

## MimeWriter Objects <span id="MimeWriter-objects" label="MimeWriter-objects"></span>

`MimeWriter` instances have the following methods:

<div class="methoddesc">

addheaderkey, value Add a header line to the MIME message. The *key* is the name of the header, where the *value* obviously provides the value of the header. The optional argument *prefix* determines where the header is inserted; `0` means append at the end, `1` is insert at the start. The default is to append.

</div>

<div class="methoddesc">

flushheaders Causes all headers accumulated so far to be written out (and forgotten). This is useful if you don’t need a body part at all, e.g. for a subpart of type that’s (mis)used to store some header-like information.

</div>

<div class="methoddesc">

startbodyctype Returns a file-like object which can be used to write to the body of the message. The content-type is set to the provided *ctype*, and the optional parameter *plist* provides additional parameters for the content-type declaration. *prefix* functions as in `addheader()` except that the default is to insert at the start.

</div>

<div class="methoddesc">

startmultipartbodysubtype Returns a file-like object which can be used to write to the body of the message. Additionally, this method initializes the multi-part code, where *subtype* provides the multipart subtype, *boundary* may provide a user-defined boundary specification, and *plist* provides optional parameters for the subtype. *prefix* functions as in `startbody()`. Subparts should be created using `nextpart()`.

</div>

<div class="methoddesc">

nextpart Returns a new instance of `MimeWriter` which represents an individual part in a multipart message. This may be used to write the part as well as used for creating recursively complex multipart messages. The message must first be initialized with `startmultipartbody()` before using `nextpart()`.

</div>

<div class="methoddesc">

lastpart This is used to designate the last part of a multipart message, and should *always* be used when writing multipart messages.

</div>
# Miscellaneous Services

The modules described in this chapter provide miscellaneous services that are available in all Python versions. Here’s an overview:
# Multimedia Services

The modules described in this chapter implement various algorithms or interfaces that are mainly useful for multimedia applications. They are available at the discretion of the installation. Here’s an overview:
# `mmap` — Memory-mapped file support

*Interface to memory-mapped files for Unix and Windows.*\
Memory-mapped file objects behave like both mutable strings and like file objects. You can use mmap objects in most places where strings are expected; for example, you can use the `re` module to search through a memory-mapped file. Since they’re mutable, you can change a single character by doing `obj[`*`index`*`] = ’a’`, or change a substring by assigning to a slice: `obj[`*`i1`*`:`*`i2`*`] = ’...’`. You can also read and write data starting at the current file position, and `seek()` through the file to different positions.

A memory-mapped file is created by the following function, which is different on Unix and on Windows.

<div class="funcdesc">

mmapfileno, length **(Windows version)** Maps *length* bytes from the file specified by the file handle *fileno*, and returns a mmap object. If you wish to map an existing Python file object, use its `fileno()` method to obtain the correct value for the *fileno* parameter.

*tagname*, if specified, is a string giving a tag name for the mapping. Windows allows you to have many different mappings against the same file. If you specify the name of an existing tag, that tag is opened, otherwise a new tag of this name is created. If this parameter is None, the mapping is created without a name. Avoiding the use of the tag parameter will assist in keeping your code portable between Unix and Windows.

</div>

<div class="funcdesc">

mmapfileno, size **(Unix version)** Maps *length* bytes from the file specified by the file handle *fileno*, and returns a mmap object. If you wish to map an existing Python file object, use its `fileno()` method to obtain the correct value for the *fileno* parameter.

*flags* specifies the nature of the mapping. creates a private copy-on-write mapping, so changes to the contents of the mmap object will be private to this process, and creates a mapping that’s shared with all other processes mapping the same areas of the file. The default value is .

*prot*, if specified, gives the desired memory protection; the two most useful values are and , to specify that the pages may be read or written. *prot* defaults to .

</div>

Memory-mapped file objects support the following methods:

<div class="methoddesc">

close Close the file. Subsequent calls to other methods of the object will result in an exception being raised.

</div>

<div class="methoddesc">

findstring Returns the lowest index in the object where the substring *string* is found. Returns `-1` on failure. *start* is the index at which the search begins, and defaults to zero.

</div>

<div class="methoddesc">

flush Flushes changes made to the in-memory copy of a file back to disk. Without use of this call there is no guarantee that changes are written back before the object is destroyed. If *offset* and *size* are specified, only changes to the given range of bytes will be flushed to disk; otherwise, the whole extent of the mapping is flushed.

</div>

<div class="methoddesc">

move*dest*, *src*, *count* Copy the *count* bytes starting at offset *src* to the destination index *dest*.

</div>

<div class="methoddesc">

read*num* Return a string containing up to *num* bytes starting from the current file position; the file position is updated to point after the bytes that were returned.

</div>

<div class="methoddesc">

read_byte Returns a string of length 1 containing the character at the current file position, and advances the file position by 1.

</div>

<div class="methoddesc">

readline Returns a single line, starting at the current file position and up to the next newline.

</div>

<div class="methoddesc">

resize*newsize*

</div>

<div class="methoddesc">

seekpos Set the file’s current position. *whence* argument is optional and defaults to `0` (absolute file positioning); other values are `1` (seek relative to the current position) and `2` (seek relative to the file’s end).

</div>

<div class="methoddesc">

size Return the length of the file, which can be larger than the size of the memory-mapped area.

</div>

<div class="methoddesc">

tell Returns the current position of the file pointer.

</div>

<div class="methoddesc">

write*string* Write the bytes in *string* into memory at the current position of the file pointer; the file position is updated to point after the bytes that were written.

</div>

<div class="methoddesc">

write_byte*byte* Write the single-character string *byte* into memory at the current position of the file pointer; the file position is advanced by `1`.

</div>
# `mpz` — GNU arbitrary magnitude integers

*Interface to the GNU MP library for arbitrary precision arithmetic.*\
This is an optional module. It is only available when Python is configured to include it, which requires that the GNU MP software is installed. This module implements the interface to part of the GNU MP library, which defines arbitrary precision integer and rational number arithmetic routines. Only the interfaces to the *integer* (`mpz_*()`) routines are provided. If not stated otherwise, the description in the GNU MP documentation can be applied.

Support for rational numberscan be implemented in Python. For an example, see the `Rat`module, provided as `Demos/classes/Rat.py` in the Python source distribution.

In general, *mpz*-numbers can be used just like other standard Python numbers, e.g., you can use the built-in operators like `+`, `*`, etc., as well as the standard built-in functions like `abs()`, `int()`, …, `divmod()`, `pow()`. **Please note:** the *bitwise-xor* operation has been implemented as a bunch of *and*s, *invert*s and *or*s, because the library lacks an function, and I didn’t need one.

You create an mpz-number by calling the function `mpz()` (see below for an exact description). An mpz-number is printed like this: `mpz(`*`value`*`)`.

<div class="funcdesc">

mpzvalue Create a new mpz-number. *value* can be an integer, a long, another mpz-number, or even a string. If it is a string, it is interpreted as an array of radix-256 digits, least significant digit first, resulting in a positive number. See also the `binary()` method, described below.

</div>

<div class="datadesc">

MPZType The type of the objects returned by `mpz()` and most other functions in this module.

</div>

A number of *extra* functions are defined in this module. Non mpz-arguments are converted to mpz-values first, and the functions return mpz-numbers.

<div class="funcdesc">

powmbase, exponent, modulus Return `pow(`*`base`*`, `*`exponent`*`) % `*`modulus`*. If *`exponent`*` == 0`, return `mpz(1)`. In contrast to the C library function, this version can handle negative exponents.

</div>

<div class="funcdesc">

gcdop1, op2 Return the greatest common divisor of *op1* and *op2*.

</div>

<div class="funcdesc">

gcdexta, b Return a tuple `(`*`g`*`, `*`s`*`, `*`t`*`)`, such that *`a`*`*`*`s`*` + `*`b`*`*`*`t`*` == `*`g`*` == gcd(`*`a`*`, `*`b`*`)`.

</div>

<div class="funcdesc">

sqrtop Return the square root of *op*. The result is rounded towards zero.

</div>

<div class="funcdesc">

sqrtremop Return a tuple `(`*`root`*`, `*`remainder`*`)`, such that *`root`*`*`*`root`*` + `*`remainder`*` == `*`op`*.

</div>

<div class="funcdesc">

divmnumerator, denominator, modulus Returns a number *q* such that *`q`*` * `*`denominator`*` % `*`modulus`*` == `*`numerator`*. One could also implement this function in Python, using `gcdext()`.

</div>

An mpz-number has one method:

<div class="methoddesc">

binary Convert this mpz-number to a binary string, where the number has been stored as an array of radix-256 digits, least significant digit first.

The mpz-number must have a value greater than or equal to zero, otherwise `ValueError` will be raised.

</div>
# `msvcrt` – Useful routines from the MS VC++ runtime

*Miscellaneous useful routines from the MS VC++ runtime.*\
These functions provide access to some useful capabilities on Windows platforms. Some higher-level modules use these functions to build the Windows implementations of their services. For example, the `getpass` module uses this in the implementation of the `getpass()` function.

Further documentation on these functions can be found in the Platform API documentation.

## File Operations <span id="msvcrt-files" label="msvcrt-files"></span>

<div class="funcdesc">

lockingfd, mode, nbytes Lock part of a file based on a file descriptor from the C runtime. Raises `IOError` on failure.

</div>

<div class="funcdesc">

setmodefd, flags Set the line-end translation mode for the file descriptor *fd*. To set it to text mode, *flags* should be ; for binary, it should be .

</div>

<div class="funcdesc">

open_osfhandlehandle, flags Create a C runtime file descriptor from the file handle *handle*. The *flags* parameter should be a bit-wise OR of , , and . The returned file descriptor may be used as a parameter to `os.fdopen()` to create a file object.

</div>

<div class="funcdesc">

get_osfhandlefd Return the file handle for the file descriptor *fd*. Raises `IOError` if *fd* is not recognized.

</div>

## Console I/O <span id="msvcrt-console" label="msvcrt-console"></span>

<div class="funcdesc">

kbhit Return true if a keypress is waiting to be read.

</div>

<div class="funcdesc">

getch Read a keypress and return the resulting character. Nothing is echoed to the console. This call will block if a keypress is not already available, but will not wait for `Enter` to be pressed. If the pressed key was a special function key, this will return `’’` or `’xe0’`; the next call will return the keycode. The `Control-C` keypress cannot be read with this function.

</div>

<div class="funcdesc">

getche Similar to `getch()`, but the keypress will be echoed if it represents a printable character.

</div>

<div class="funcdesc">

putchchar Print the character *char* to the console without buffering.

</div>

<div class="funcdesc">

ungetchchar Cause the character *char* to be “pushed back” into the console buffer; it will be the next character read by `getch()` or `getche()`.

</div>

## Other Functions <span id="msvcrt-other" label="msvcrt-other"></span>

<div class="funcdesc">

heapmin Force the heap to clean itself up and return unused blocks to the operating system. This only works on Windows NT. On failure, this raises `IOError`.

</div>
# `multifile` — Support for files containing distinct parts

*Support for reading files which contain distinct parts, such as some MIME data.*\
The `MultiFile` object enables you to treat sections of a text file as file-like input objects, with `’’` being returned by `readline()` when a given delimiter pattern is encountered. The defaults of this class are designed to make it useful for parsing MIME multipart messages, but by subclassing it and overriding methods it can be easily adapted for more general use.

<div class="classdesc">

MultiFilefp Create a multi-file. You must instantiate this class with an input object argument for the `MultiFile` instance to get lines from, such as as a file object returned by `open()`.

`MultiFile` only ever looks at the input object’s `readline()`, `seek()` and `tell()` methods, and the latter two are only needed if you want random access to the individual MIME parts. To use `MultiFile` on a non-seekable stream object, set the optional *seekable* argument to false; this will prevent using the input object’s `seek()` and `tell()` methods.

</div>

It will be useful to know that in `MultiFile`’s view of the world, text is composed of three kinds of lines: data, section-dividers, and end-markers. MultiFile is designed to support parsing of messages that may have multiple nested message parts, each with its own pattern for section-divider and end-marker lines.

## MultiFile Objects <span id="MultiFile-objects" label="MultiFile-objects"></span>

A `MultiFile` instance has the following methods:

<div class="methoddesc">

pushstr Push a boundary string. When an appropriately decorated version of this boundary is found as an input line, it will be interpreted as a section-divider or end-marker. All subsequent reads will return the empty string to indicate end-of-file, until a call to `pop()` removes the boundary a or `next()` call reenables it.

It is possible to push more than one boundary. Encountering the most-recently-pushed boundary will return EOF; encountering any other boundary will raise an error.

</div>

<div class="methoddesc">

readlinestr Read a line. If the line is data (not a section-divider or end-marker or real EOF) return it. If the line matches the most-recently-stacked boundary, return `’’` and set `self.last` to 1 or 0 according as the match is or is not an end-marker. If the line matches any other stacked boundary, raise an error. On encountering end-of-file on the underlying stream object, the method raises `Error` unless all boundaries have been popped.

</div>

<div class="methoddesc">

readlinesstr Return all lines remaining in this part as a list of strings.

</div>

<div class="methoddesc">

read Read all lines, up to the next section. Return them as a single (multiline) string. Note that this doesn’t take a size argument!

</div>

<div class="methoddesc">

next Skip lines to the next section (that is, read lines until a section-divider or end-marker has been consumed). Return true if there is such a section, false if an end-marker is seen. Re-enable the most-recently-pushed boundary.

</div>

<div class="methoddesc">

pop Pop a section boundary. This boundary will no longer be interpreted as EOF.

</div>

<div class="methoddesc">

seekpos Seek. Seek indices are relative to the start of the current section. The *pos* and *whence* arguments are interpreted as for a file seek.

</div>

<div class="methoddesc">

tell Return the file position relative to the start of the current section.

</div>

<div class="methoddesc">

is_datastr Return true if *str* is data and false if it might be a section boundary. As written, it tests for a prefix other than `’-``-’` at start of line (which all MIME boundaries have) but it is declared so it can be overridden in derived classes.

Note that this test is used intended as a fast guard for the real boundary tests; if it always returns false it will merely slow processing, not cause it to fail.

</div>

<div class="methoddesc">

section_dividerstr Turn a boundary into a section-divider line. By default, this method prepends `’-``-’` (which MIME section boundaries have) but it is declared so it can be overridden in derived classes. This method need not append LF or CR-LF, as comparison with the result ignores trailing whitespace.

</div>

<div class="methoddesc">

end_markerstr Turn a boundary string into an end-marker line. By default, this method prepends `’-``-’` and appends `’-``-’` (like a MIME-multipart end-of-message marker) but it is declared so it can be be overridden in derived classes. This method need not append LF or CR-LF, as comparison with the result ignores trailing whitespace.

</div>

Finally, `MultiFile` instances have two public instance variables:

<div class="memberdesc">

level Nesting depth of the current part.

</div>

<div class="memberdesc">

last True if the last end-of-file was for an end-of-message marker.

</div>

## `MultiFile` Example <span id="multifile-example" label="multifile-example"></span>

    import mimetools
    import MultiFile
    import StringIO

    def extract_mime_part_matching(stream, mimetype):
        """Return the first element in a multipart MIME message on stream
        matching mimetype."""

        msg = mimetools.Message(stream)
        msgtype = msg.gettype()
        params = msg.getplist()

        data = StringIO.StringIO()
        if msgtype[:10] == "multipart/":

            file = multifile.MultiFile(stream)
            file.push(msg.getparam("boundary"))
            while file.next():
                submsg = mimetools.Message(file)
                try:
                    data = StringIO.StringIO()
                    mimetools.decode(file, data, submsg.getencoding())
                except ValueError:
                    continue
                if submsg.gettype() == mimetype:
                    break
            file.pop()
        return data.getvalue()
# `mutex` — Mutual exclusion support

*Lock and queue for mutual exclusion.*\
The `mutex` defines a class that allows mutual-exclusion via acquiring and releasing locks. It does not require (or imply) threading or multi-tasking, though it could be useful for those purposes.

The `mutex` module defines the following class:

<div class="classdesc">

mutex Create a new (unlocked) mutex.

A mutex has two pieces of state — a “locked” bit and a queue. When the mutex is not locked, the queue is empty. Otherwise, the queue contains 0 or more `(`*`function`*`, `*`argument`*`)` pairs representing functions (or methods) waiting to acquire the lock. When the mutex is unlocked while the queue is not empty, the first queue entry is removed and its *`function`*`(`*`argument`*`)` pair called, implying it now has the lock.

Of course, no multi-threading is implied – hence the funny interface for lock, where a function is called once the lock is acquired.

</div>

## Mutex Objects <span id="mutex-objects" label="mutex-objects"></span>

`mutex` objects have following methods:

<div class="methoddesc">

test Check whether the mutex is locked.

</div>

<div class="methoddesc">

testandset “Atomic” test-and-set, grab the lock if it is not set, and return true, otherwise, return false.

</div>

<div class="methoddesc">

lockfunction, argument Execute *`function`*`(`*`argument`*`)`, unless the mutex is locked. In the case it is locked, place the function and argument on the queue. See `unlock` for explanation of when *`function`*`(`*`argument`*`)` is executed in that case.

</div>

<div class="methoddesc">

unlock Unlock the mutex if queue is empty, otherwise execute the first element in the queue.

</div>
# `netrc` — netrc file processing

*Loading of `.netrc` files.*\
*New in version 1.5.2.*

The `netrc` class parses and encapsulates the netrc file format used by the Unix program and other FTP clients.

<div class="classdesc">

netrc A `netrc` instance or subclass instance encapsulates data from a netrc file. The initialization argument, if present, specifies the file to parse. If no argument is given, the file `.netrc` in the user’s home directory will be read. Parse errors will raise `SyntaxError` with diagnostic information including the file name, line number, and terminating token.

</div>

## netrc Objects <span id="netrc-objects" label="netrc-objects"></span>

A `netrc` instance has the following methods:

<div class="methoddesc">

authenticatorshost Return a 3-tuple `(`*`login`*`, `*`account`*`, `*`password`*`)` of authenticators for *host*. If the netrc file did not contain an entry for the given host, return the tuple associated with the ‘default’ entry. If neither matching host nor default entry is available, return `None`.

</div>

<div class="methoddesc">

\_\_repr\_\_ Dump the class data as a string in the format of a netrc file. (This discards comments and may reorder the entries.)

</div>

Instances of `netrc` have public instance variables:

<div class="memberdesc">

hosts Dictionary mapping host names to `(`*`login`*`, `*`account`*`, `*`password`*`)` tuples. The ‘default’ entry, if any, is represented as a pseudo-host by that name.

</div>

<div class="memberdesc">

macros Dictionary mapping macro names to string lists.

</div>
# `new` — Runtime implementation object creation

*Interface to the creation of runtime implementation objects.*\
The `new` module allows an interface to the interpreter object creation functions. This is for use primarily in marshal-type functions, when a new object needs to be created “magically” and not by using the regular creation functions. This module provides a low-level interface to the interpreter, so care must be exercised when using this module.

The `new` module defines the following functions:

<div class="funcdesc">

instanceclass, dict This function creates an instance of *class* with dictionary *dict* without calling the `__init__()` constructor. Note that there are no guarantees that the object will be in a consistent state.

</div>

<div class="funcdesc">

instancemethodfunction, instance, class This function will return a method object, bound to *instance*, or unbound if *instance* is `None`. *function* must be callable, and *instance* must be an instance object or `None`.

</div>

<div class="funcdesc">

functioncode, globals Returns a (Python) function with the given code and globals. If *name* is given, it must be a string or `None`. If it is a string, the function will have the given name, otherwise the function name will be taken from *`code`*`.co_name`. If *argdefs* is given, it must be a tuple and will be used to the determine the default values of parameters.

</div>

<div class="funcdesc">

codeargcount, nlocals, stacksize, flags, codestring, constants, names, varnames, filename, name, firstlineno, lnotab This function is an interface to the C function.

</div>

<div class="funcdesc">

modulename This function returns a new module object with name *name*. *name* must be a string.

</div>

<div class="funcdesc">

classobjname, baseclasses, dict This function returns a new class object, with name *name*, derived from *baseclasses* (which should be a tuple of classes) and with namespace *dict*.

</div>
# `ni` — None

*None*\
**Warning: This module is obsolete.** As of Python 1.5a4, package support (with different semantics for `__init__` and no support for `__domain__` or `__`) is built in the interpreter. The ni module is retained only for backward compatibility. As of Python 1.5b2, it has been renamed to `ni1`; if you really need it, you can use `import ni1`, but the recommended approach is to rely on the built-in package support, converting existing packages if needed. Note that mixing `ni` and the built-in package support doesn’t work: once you import `ni`, all packages use it.

The `ni` module defines a new importing scheme, which supports packages containing several Python modules. To enable package support, execute `import ni` before importing any packages. Importing this module automatically installs the relevant import hooks. There are no publicly-usable functions or variables in the `ni` module.

To create a package named `spam` containing sub-modules `ham`, `bacon` and `eggs`, create a directory `spam` somewhere on Python’s module search path, as given in `sys.path`. Then, create files called `ham.py`, `bacon.py` and `eggs.py` inside `spam`.

To import module `ham` from package `spam` and use function `hamneggs()` from that module, you can use any of the following possibilities:

    import spam.ham     # *not* "import spam" !!!
    spam.ham.hamneggs()

    from spam import ham
    ham.hamneggs()

    from spam.ham import hamneggs
    hamneggs()

`import spam` creates an empty package named `spam` if one does not already exist, but it does *not* automatically import `spam`’s submodules. The only submodule that is guaranteed to be imported is `spam.__init__`, if it exists; it would be in a file named `__init__.py` in the `spam` directory. Note that `spam.__init__` is a submodule of package spam. It can refer to spam’s namespace as `__` (two underscores):

    __.spam_inited = 1      # Set a package-level variable

Additional initialization code (setting up variables, importing other submodules) can be performed in `spam/__init__.py`.
# `nis` — Interface to Sun’s NIS (Yellow Pages)

*Interface to Sun’s NIS (a.k.a. Yellow Pages) library.*\
The `nis` module gives a thin wrapper around the NIS library, useful for central administration of several hosts.

Because NIS exists only on Unix systems, this module is only available for Unix.

The `nis` module defines the following functions:

<div class="funcdesc">

matchkey, mapname Return the match for *key* in map *mapname*, or raise an error (`nis.error`) if there is none. Both should be strings, *key* is 8-bit clean. Return value is an arbitrary array of bytes (i.e., may contain `NULL` and other joys).

Note that *mapname* is first checked if it is an alias to another name.

</div>

<div class="funcdesc">

catmapname Return a dictionary mapping *key* to *value* such that `match(`*`key`*`, `*`mapname`*`)==`*`value`*. Note that both keys and values of the dictionary are arbitrary arrays of bytes.

Note that *mapname* is first checked if it is an alias to another name.

</div>

<div class="funcdesc">

maps Return a list of all valid maps.

</div>

The `nis` module defines the following exception:

<div class="excdesc">

error An error raised when a NIS function returns an error code.

</div>
# `nntplib` — NNTP protocol client

*NNTP protocol client (requires sockets).*\
This module defines the class `NNTP` which implements the client side of the NNTP protocol. It can be used to implement a news reader or poster, or automated news processors. For more information on NNTP (Network News Transfer Protocol), see Internet .

Here are two small examples of how it can be used. To list some statistics about a newsgroup and print the subjects of the last 10 articles:

    >>> s = NNTP('news.cwi.nl')
    >>> resp, count, first, last, name = s.group('comp.lang.python')
    >>> print 'Group', name, 'has', count, 'articles, range', first, 'to', last
    Group comp.lang.python has 59 articles, range 3742 to 3803
    >>> resp, subs = s.xhdr('subject', first + '-' + last)
    >>> for id, sub in subs[-10:]: print id, sub
    ... 
    3792 Re: Removing elements from a list while iterating...
    3793 Re: Who likes Info files?
    3794 Emacs and doc strings
    3795 a few questions about the Mac implementation
    3796 Re: executable python scripts
    3797 Re: executable python scripts
    3798 Re: a few questions about the Mac implementation 
    3799 Re: PROPOSAL: A Generic Python Object Interface for Python C Modules
    3802 Re: executable python scripts 
    3803 Re: \POSIX{} wait and SIGCHLD
    >>> s.quit()
    '205 news.cwi.nl closing connection.  Goodbye.'

To post an article from a file (this assumes that the article has valid headers):

    >>> s = NNTP('news.cwi.nl')
    >>> f = open('/tmp/article')
    >>> s.post(f)
    '240 Article posted successfully.'
    >>> s.quit()
    '205 news.cwi.nl closing connection.  Goodbye.'

The module itself defines the following items:

<div class="classdesc">

NNTPhost Return a new instance of the `NNTP` class, representing a connection to the NNTP server running on host *host*, listening at port *port*. The default *port* is 119. If the optional *user* and *password* are provided, the `AUTHINFO USER` and `AUTHINFO PASS` commands are used to identify and authenticate the user to the server. If the optional flag *readermode* is true, then a `mode reader` command is sent before authentication is performed. Reader mode is sometimes necessary if you are connecting to an NNTP server on the local machine and intend to call reader-specific commands, such as `group`. If you get unexpected `NNTPPermanentError`s, you might need to set *readermode*. *readermode* defaults to `None`.

</div>

<div class="classdesc">

NNTPError Derived from the standard exception `Exception`, this is the base class for all exceptions raised by the `nntplib` module.

</div>

<div class="classdesc">

NNTPReplyError Exception raised when an unexpected reply is received from the server. For backwards compatibility, the exception `error_reply` is equivalent to this class.

</div>

<div class="classdesc">

NNTPTemporaryError Exception raised when an error code in the range 400–499 is received. For backwards compatibility, the exception `error_temp` is equivalent to this class.

</div>

<div class="classdesc">

NNTPPermanentError Exception raised when an error code in the range 500–599 is received. For backwards compatibility, the exception `error_perm` is equivalent to this class.

</div>

<div class="classdesc">

NNTPProtocolError Exception raised when a reply is received from the server that does not begin with a digit in the range 1–5. For backwards compatibility, the exception `error_proto` is equivalent to this class.

</div>

<div class="classdesc">

NNTPDataError Exception raised when there is some error in the response data. For backwards compatibility, the exception `error_data` is equivalent to this class.

</div>

## NNTP Objects <span id="nntp-objects" label="nntp-objects"></span>

NNTP instances have the following methods. The *response* that is returned as the first item in the return tuple of almost all methods is the server’s response: a string beginning with a three-digit code. If the server’s response indicates an error, the method raises one of the above exceptions.

<div class="methoddesc">

getwelcome Return the welcome message sent by the server in reply to the initial connection. (This message sometimes contains disclaimers or help information that may be relevant to the user.)

</div>

<div class="methoddesc">

set_debuglevellevel Set the instance’s debugging level. This controls the amount of debugging output printed. The default, `0`, produces no debugging output. A value of `1` produces a moderate amount of debugging output, generally a single line per request or response. A value of `2` or higher produces the maximum amount of debugging output, logging each line sent and received on the connection (including message text).

</div>

<div class="methoddesc">

newgroupsdate, time Send a `NEWGROUPS` command. The *date* argument should be a string of the form `’`*`yymmdd`*`’` indicating the date, and *time* should be a string of the form `’`*`hhmmss`*`’` indicating the time. Return a pair `(`*`response`*`, `*`groups`*`)` where *groups* is a list of group names that are new since the given date and time.

</div>

<div class="methoddesc">

newnewsgroup, date, time Send a `NEWNEWS` command. Here, *group* is a group name or `’*’`, and *date* and *time* have the same meaning as for `newgroups()`. Return a pair `(`*`response`*`, `*`articles`*`)` where *articles* is a list of article ids.

</div>

<div class="methoddesc">

list Send a `LIST` command. Return a pair `(`*`response`*`, `*`list`*`)` where *list* is a list of tuples. Each tuple has the form `(`*`group`*`, `*`last`*`, `*`first`*`, `*`flag`*`)`, where *group* is a group name, *last* and *first* are the last and first article numbers (as strings), and *flag* is `’y’` if posting is allowed, `’n’` if not, and `’m’` if the newsgroup is moderated. (Note the ordering: *last*, *first*.)

</div>

<div class="methoddesc">

groupname Send a `GROUP` command, where *name* is the group name. Return a tuple `(`*`response`*`, `*`count`*`, `*`first`*`, `*`last`*`, `*`name`*`)` where *count* is the (estimated) number of articles in the group, *first* is the first article number in the group, *last* is the last article number in the group, and *name* is the group name. The numbers are returned as strings.

</div>

<div class="methoddesc">

help Send a `HELP` command. Return a pair `(`*`response`*`, `*`list`*`)` where *list* is a list of help strings.

</div>

<div class="methoddesc">

statid Send a `STAT` command, where *id* is the message id (enclosed in and ) or an article number (as a string). Return a triple `(`*`response`*`, `*`number`*`, `*`id`*`)` where *number* is the article number (as a string) and *id* is the article id (enclosed in and ).

</div>

<div class="methoddesc">

next Send a `NEXT` command. Return as for `stat()`.

</div>

<div class="methoddesc">

last Send a `LAST` command. Return as for `stat()`.

</div>

<div class="methoddesc">

headid Send a `HEAD` command, where *id* has the same meaning as for `stat()`. Return a tuple `(`*`response`*`, `*`number`*`, `*`id`*`, `*`list`*`)` where the first three are the same as for `stat()`, and *list* is a list of the article’s headers (an uninterpreted list of lines, without trailing newlines).

</div>

<div class="methoddesc">

bodyid Send a `BODY` command, where *id* has the same meaning as for `stat()`. Return as for `head()`.

</div>

<div class="methoddesc">

articleid Send an `ARTICLE` command, where *id* has the same meaning as for `stat()`. Return as for `head()`.

</div>

<div class="methoddesc">

slave Send a `SLAVE` command. Return the server’s *response*.

</div>

<div class="methoddesc">

xhdrheader, string Send an `XHDR` command. This command is not defined in the RFC but is a common extension. The *header* argument is a header keyword, e.g. `’subject’`. The *string* argument should have the form `’`*`first`*`-`*`last`*`’` where *first* and *last* are the first and last article numbers to search. Return a pair `(`*`response`*`, `*`list`*`)`, where *list* is a list of pairs `(`*`id`*`, `*`text`*`)`, where *id* is an article id (as a string) and *text* is the text of the requested header for that article.

</div>

<div class="methoddesc">

postfile Post an article using the `POST` command. The *file* argument is an open file object which is read until EOF using its `readline()` method. It should be a well-formed news article, including the required headers. The `post()` method automatically escapes lines beginning with `.`.

</div>

<div class="methoddesc">

ihaveid, file Send an `IHAVE` command. If the response is not an error, treat *file* exactly as for the `post()` method.

</div>

<div class="methoddesc">

date Return a triple `(`*`response`*`, `*`date`*`, `*`time`*`)`, containing the current date and time in a form suitable for the `newnews()` and `newgroups()` methods. This is an optional NNTP extension, and may not be supported by all servers.

</div>

<div class="methoddesc">

xgtitlename Process an `XGTITLE` command, returning a pair `(`*`response`*`, `*`list`*`)`, where *list* is a list of tuples containing `(`*`name`*`, `*`title`*`)`.

This is an optional NNTP extension, and may not be supported by all servers.

</div>

<div class="methoddesc">

xoverstart, end Return a pair `(`*`resp`*`, `*`list`*`)`. *list* is a list of tuples, one for each article in the range delimited by the *start* and *end* article numbers. Each tuple is of the form `(`*`article number`*`, `*`subject`*`, `*`poster`*`, `*`date`*`, `*`id`*`, `*`references`*`, `*`size`*`, `*`lines`*`)`. This is an optional NNTP extension, and may not be supported by all servers.

</div>

<div class="methoddesc">

xpathid Return a pair `(`*`resp`*`, `*`path`*`)`, where *path* is the directory path to the article with message ID *id*. This is an optional NNTP extension, and may not be supported by all servers.

</div>

<div class="methoddesc">

quit Send a `QUIT` command and close the connection. Once this method has been called, no other methods of the NNTP object should be called.

</div>
# Built-in Types, Exceptions and Functions

<span id="builtin" label="builtin"></span>

Names for built-in exceptions and functions are found in a separate symbol table. This table is searched last when the interpreter looks up the meaning of a name, so local and global user-defined names can override built-in names. Built-in types are described together here for easy reference.[^1] The tables in this chapter document the priorities of operators by listing them in order of ascending priority (within a table) and grouping operators that have the same priority in the same box. Binary operators of the same priority group from left to right. (Unary operators group from right to left, but there you have no real choice.) See chapter 5 of the Python Reference Manual for the complete picture on operator priorities.

[^1]: Most descriptions sorely lack explanations of the exceptions that may be raised — this will be fixed in a future version of this manual.
# `operator` — Standard operators as functions.

*All Python’s standard operators as built-in functions.*\
The `operator` module exports a set of functions implemented in C corresponding to the intrinsic operators of Python. For example, `operator.add(x, y)` is equivalent to the expression `x+y`. The function names are those used for special class methods; variants without leading and trailing `__` are also provided for convenience.

The `operator` module defines the following functions:

<div class="funcdesc">

adda, b Return *a* `+` *b*, for *a* and *b* numbers.

</div>

<div class="funcdesc">

suba, b Return *a* `-` *b*.

</div>

<div class="funcdesc">

mula, b Return *a* `*` *b*, for *a* and *b* numbers.

</div>

<div class="funcdesc">

diva, b Return *a* `/` *b*.

</div>

<div class="funcdesc">

moda, b Return *a* `%` *b*.

</div>

<div class="funcdesc">

nego Return *o* negated.

</div>

<div class="funcdesc">

poso Return *o* positive.

</div>

<div class="funcdesc">

abso Return the absolute value of *o*.

</div>

<div class="funcdesc">

invo Return the inverse of *o*. The names `invert()` and `__invert__()` were added in Python 2.0.

</div>

<div class="funcdesc">

lshifta, b Return *a* shifted left by *b*.

</div>

<div class="funcdesc">

rshifta, b Return *a* shifted right by *b*.

</div>

<div class="funcdesc">

and\_a, b Return the bitwise and of *a* and *b*.

</div>

<div class="funcdesc">

or\_a, b Return the bitwise or of *a* and *b*.

</div>

<div class="funcdesc">

xora, b Return the bitwise exclusive or of *a* and *b*.

</div>

<div class="funcdesc">

not\_o Return the outcome of *o*. (Note that there is no `__not__()` discipline for object instances; only the interpreter core defines this operation.)

</div>

<div class="funcdesc">

trutho Return `1` if *o* is true, and 0 otherwise.

</div>

<div class="funcdesc">

concata, b Return *a* `+` *b* for *a* and *b* sequences.

</div>

<div class="funcdesc">

repeata, b Return *a* `*` *b* where *a* is a sequence and *b* is an integer.

</div>

<div class="funcdesc">

containsa, b Return the outcome of the test *b* `in` *a*. Note the reversed operands. The name `__contains__()` was added in Python 2.0.

</div>

<div class="funcdesc">

sequenceIncludes *Deprecated since version 2.0: Use `contains()` instead.* Alias for `contains()`.

</div>

<div class="funcdesc">

countOfa, b Return the number of occurrences of *b* in *a*.

</div>

<div class="funcdesc">

indexOfa, b Return the index of the first of occurrence of *b* in *a*.

</div>

<div class="funcdesc">

getitema, b Return the value of *a* at index *b*.

</div>

<div class="funcdesc">

setitema, b, c Set the value of *a* at index *b* to *c*.

</div>

<div class="funcdesc">

delitema, b Remove the value of *a* at index *b*.

</div>

<div class="funcdesc">

getslicea, b, c Return the slice of *a* from index *b* to index *c*`-1`.

</div>

<div class="funcdesc">

setslicea, b, c, v Set the slice of *a* from index *b* to index *c*`-1` to the sequence *v*.

</div>

<div class="funcdesc">

delslicea, b, c Delete the slice of *a* from index *b* to index *c*`-1`.

</div>

Example: Build a dictionary that maps the ordinals from `0` to `256` to their character equivalents.

    >>> import operator
    >>> d = {}
    >>> keys = range(256)
    >>> vals = map(chr, keys)
    >>> map(operator.setitem, [d]*len(keys), keys, vals)
# `os` — Miscellaneous OS interfaces

*Miscellaneous OS interfaces.*\
This module provides a more portable way of using operating system (OS) dependent functionality than importing an OS dependent built-in module like `posix` or `nt`.

This module searches for an OS dependent built-in module like `mac` or `posix` and exports the same functions and data as found there. The design of all Python’s built-in OS dependent modules is such that as long as the same functionality is available, it uses the same interface; e.g., the function `os.stat(`*`path`*`)` returns stat information about *path* in the same format (which happens to have originated with the interface).

Extensions peculiar to a particular OS are also available through the `os` module, but using them is of course a threat to portability!

Note that after the first time `os` is imported, there is *no* performance penalty in using functions from `os` instead of directly from the OS dependent built-in module, so there should be *no* reason not to use `os`!

<div class="excdesc">

error This exception is raised when a function returns a system-related error (e.g., not for illegal argument types). This is also known as the built-in exception `OSError`. The accompanying value is a pair containing the numeric error code from and the corresponding string, as would be printed by the C function . See the module `errno`, which contains names for the error codes defined by the underlying operating system.

When exceptions are classes, this exception carries two attributes, `errno` and `strerror`. The first holds the value of the C variable, and the latter holds the corresponding error message from . For exceptions that involve a file system path (e.g. `chdir()` or `unlink()`), the exception instance will contain a third attribute, `filename`, which is the file name passed to the function.

When exceptions are strings, the string for the exception is `’OSError’`.

</div>

<div class="datadesc">

name The name of the OS dependent module imported. The following names have currently been registered: `’posix’`, `’nt’`, `’dos’`, `’mac’`, `’os2’`, `’ce’`, `’java’`.

</div>

<div class="datadesc">

path The corresponding OS dependent standard module for pathname operations, e.g., `posixpath` or `macpath`. Thus, given the proper imports, `os.path.split(`*`file`*`)` is equivalent to but more portable than `posixpath.split(`*`file`*`)`. Note that this is also a valid module: it may be imported directly as `os.path`.

</div>

## Process Parameters <span id="os-procinfo" label="os-procinfo"></span>

These functions and data items provide information and operate on the current process and user.

<div class="datadesc">

environ A mapping object representing the string environment. For example, `environ[’HOME’]` is the pathname of your home directory (on some platforms), and is equivalent to `getenv("HOME")` in C.

If the platform supports the `putenv()` function, this mapping may be used to modify the environment as well as query the environment. `putenv()` will be called automatically when the mapping is modified.

If `putenv()` is not provided, this mapping may be passed to the appropriate process-creation functions to cause child processes to use a modified environment.

</div>

<div class="funcdescni">

chdirpath These functions are described in “Files and Directories” (section <a href="#os-file-dir" data-reference-type="ref" data-reference="os-file-dir">[os-file-dir]</a>).

</div>

<div class="funcdesc">

ctermid Return the filename corresponding to the controlling terminal of the process. Availability: Unix.

</div>

<div class="funcdesc">

getegid Return the current process’ effective group id. Availability: Unix.

</div>

<div class="funcdesc">

geteuid Return the current process’ effective user id. Availability: Unix.

</div>

<div class="funcdesc">

getgid Return the current process’ group id. Availability: Unix.

</div>

<div class="funcdesc">

getgroups Return list of supplemental group ids associated with the current process. Availability: Unix.

</div>

<div class="funcdesc">

getlogin Return the actual login name for the current process, even if there are multiple login names which map to the same user id. Availability: Unix.

</div>

<div class="funcdesc">

getpgrp Return the current process group id. Availability: Unix.

</div>

<div class="funcdesc">

getpid Return the current process id. Availability: Unix, Windows.

</div>

<div class="funcdesc">

getppid Return the parent’s process id. Availability: Unix.

</div>

<div class="funcdesc">

getuid Return the current process’ user id. Availability: Unix.

</div>

<div class="funcdesc">

putenvvarname, value Set the environment variable named *varname* to the string *value*. Such changes to the environment affect subprocesses started with `os.system()`, `popen()` or `fork()` and `execv()`. Availability: most flavors of Unix, Windows.

When `putenv()` is supported, assignments to items in `os.environ` are automatically translated into corresponding calls to `putenv()`; however, calls to `putenv()` don’t update `os.environ`, so it is actually preferable to assign to items of `os.environ`.

</div>

<div class="funcdesc">

setegidegid Set the current process’s effective group id. Availability: Unix.

</div>

<div class="funcdesc">

seteuideuid Set the current process’s effective user id. Availability: Unix.

</div>

<div class="funcdesc">

setgidgid Set the current process’ group id. Availability: Unix.

</div>

<div class="funcdesc">

setpgrp Calls the system call or depending on which version is implemented (if any). See the Unix manual for the semantics. Availability: Unix.

</div>

<div class="funcdesc">

setpgidpid, pgrp Calls the system call . See the Unix manual for the semantics. Availability: Unix.

</div>

<div class="funcdesc">

setreuidruid, euid Set the current process’s real and effective user ids. Availability: Unix.

</div>

<div class="funcdesc">

setregidrgid, egid Set the current process’s real and effective group ids. Availability: Unix.

</div>

<div class="funcdesc">

setsid Calls the system call . See the Unix manual for the semantics. Availability: Unix.

</div>

<div class="funcdesc">

setuiduid Set the current process’ user id. Availability: Unix.

</div>

<div class="funcdesc">

strerrorcode Return the error message corresponding to the error code in *code*. Availability: Unix, Windows.

</div>

<div class="funcdesc">

umaskmask Set the current numeric umask and returns the previous umask. Availability: Unix, Windows.

</div>

<div class="funcdesc">

uname Return a 5-tuple containing information identifying the current operating system. The tuple contains 5 strings: `(`*`sysname`*`, `*`nodename`*`, `*`release`*`, `*`version`*`, `*`machine`*`)`. Some systems truncate the nodename to 8 characters or to the leading component; a better way to get the hostname is `socket.gethostname()` or even `socket.gethostbyaddr(socket.gethostname())`. Availability: recent flavors of Unix.

</div>

## File Object Creation <span id="os-newstreams" label="os-newstreams"></span>

These functions create new file objects.

<div class="funcdesc">

fdopenfd Return an open file object connected to the file descriptor *fd*. The *mode* and *bufsize* arguments have the same meaning as the corresponding arguments to the built-in `open()` function. Availability: Macintosh, Unix, Windows.

</div>

<div class="funcdesc">

popencommand Open a pipe to or from *command*. The return value is an open file object connected to the pipe, which can be read or written depending on whether *mode* is `’r’` (default) or `’w’`. The *bufsize* argument has the same meaning as the corresponding argument to the built-in `open()` function. The exit status of the command (encoded in the format specified for `wait()`) is available as the return value of the `close()` method of the file object, except that when the exit status is zero (termination without errors), `None` is returned. **Note:** This function behaves unreliably under Windows due to the native implementation of . Availability: Unix, Windows.

</div>

<div class="funcdesc">

tmpfile Return a new file object opened in update mode (`w+`). The file has no directory entries associated with it and will be automatically deleted once there are no file descriptors for the file. Availability: Unix.

</div>

## File Descriptor Operations <span id="os-fd-ops" label="os-fd-ops"></span>

These functions operate on I/O streams referred to using file descriptors.

<div class="funcdesc">

closefd Close file descriptor *fd*. Availability: Macintosh, Unix, Windows.

Note: this function is intended for low-level I/O and must be applied to a file descriptor as returned by `open()` or `pipe()`. To close a “file object” returned by the built-in function `open()` or by `popen()` or `fdopen()`, use its `close()` method.

</div>

<div class="funcdesc">

dupfd Return a duplicate of file descriptor *fd*. Availability: Macintosh, Unix, Windows.

</div>

<div class="funcdesc">

dup2fd, fd2 Duplicate file descriptor *fd* to *fd2*, closing the latter first if necessary. Availability: Unix, Windows.

</div>

<div class="funcdesc">

fpathconffd, name Return system configuration information relevant to an open file. *name* specifies the configuration value to retrieve; it may be a string which is the name of a defined system value; these names are specified in a number of standards (, Unix95, Unix98, and others). Some platforms define additional names as well. The names known to the host operating system are given in the `pathconf_names` dictionary. For configuration variables not included in that mapping, passing an integer for *name* is also accepted. Availability: Unix.

If *name* is a string and is not known, `ValueError` is raised. If a specific value for *name* is not supported by the host system, even if it is included in `pathconf_names`, an `OSError` is raised with for the error number.

</div>

<div class="funcdesc">

fstatfd Return status for file descriptor *fd*, like `stat()`. Availability: Unix, Windows.

</div>

<div class="funcdesc">

fstatvfsfd Return information about the filesystem containing the file associated with file descriptor *fd*, like `statvfs()`. Availability: Unix.

</div>

<div class="funcdesc">

ftruncatefd, length Truncate the file corresponding to file descriptor *fd*, so that it is at most *length* bytes in size. Availability: Unix.

</div>

<div class="funcdesc">

isattyfd Return `1` if the file descriptor *fd* is open and connected to a tty(-like) device, else `0`. Availability: Unix

</div>

<div class="funcdesc">

lseekfd, pos, how Set the current position of file descriptor *fd* to position *pos*, modified by *how*: `0` to set the position relative to the beginning of the file; `1` to set it relative to the current position; `2` to set it relative to the end of the file. Availability: Macintosh, Unix, Windows.

</div>

<div class="funcdesc">

openfile, flags Open the file *file* and set various flags according to *flags* and possibly its mode according to *mode*. The default *mode* is `0777` (octal), and the current umask value is first masked out. Return the file descriptor for the newly opened file. Availability: Macintosh, Unix, Windows.

For a description of the flag and mode values, see the C run-time documentation; flag constants (like and ) are defined in this module too (see below).

Note: this function is intended for low-level I/O. For normal usage, use the built-in function `open()`, which returns a “file object” with `read()` and `write()` methods (and many more).

</div>

<div class="funcdesc">

openpty Open a new pseudo-terminal pair. Return a pair of file descriptors `(`*`master`*`, `*`slave`*`)` for the pty and the tty, respectively. For a (slightly) more portable approach, use the `pty`module. Availability: Some flavors of Unix

</div>

<div class="funcdesc">

pipe Create a pipe. Return a pair of file descriptors `(`*`r`*`, `*`w`*`)` usable for reading and writing, respectively. Availability: Unix, Windows.

</div>

<div class="funcdesc">

readfd, n Read at most *n* bytes from file descriptor *fd*. Return a string containing the bytes read. Availability: Macintosh, Unix, Windows.

Note: this function is intended for low-level I/O and must be applied to a file descriptor as returned by `open()` or `pipe()`. To read a “file object” returned by the built-in function `open()` or by `popen()` or `fdopen()`, or `sys.stdin`, use its `read()` or `readline()` methods.

</div>

<div class="funcdesc">

tcgetpgrpfd Return the process group associated with the terminal given by *fd* (an open file descriptor as returned by `open()`). Availability: Unix.

</div>

<div class="funcdesc">

tcsetpgrpfd, pg Set the process group associated with the terminal given by *fd* (an open file descriptor as returned by `open()`) to *pg*. Availability: Unix.

</div>

<div class="funcdesc">

ttynamefd Return a string which specifies the terminal device associated with file-descriptor *fd*. If *fd* is not associated with a terminal device, an exception is raised. Availability: Unix.

</div>

<div class="funcdesc">

writefd, str Write the string *str* to file descriptor *fd*. Return the number of bytes actually written. Availability: Macintosh, Unix, Windows.

Note: this function is intended for low-level I/O and must be applied to a file descriptor as returned by `open()` or `pipe()`. To write a “file object” returned by the built-in function `open()` or by `popen()` or `fdopen()`, or `sys.stdout` or `sys.stderr`, use its `write()` method.

</div>

The following data items are available for use in constructing the *flags* parameter to the `open()` function.

<div class="datadesc">

O_RDONLY Options for the *flag* argument to the `open()` function. These can be bit-wise OR’d together. Availability: Macintosh, Unix, Windows.

</div>

<div class="datadesc">

O_BINARY Option for the *flag* argument to the `open()` function. This can be bit-wise OR’d together with those listed above. Availability: Macintosh, Windows.

</div>

## Files and Directories <span id="os-file-dir" label="os-file-dir"></span>

<div class="funcdesc">

accesspath, mode Check read/write/execute permissions for this process or existence of file *path*. *mode* should be to test the existence of *path*, or it can be the inclusive OR of one or more of , , and to test permissions. Return `1` if access is allowed, `0` if not. See the Unix man page for more information. Availability: Unix, Windows.

</div>

<div class="datadesc">

F_OK Value to pass as the *mode* parameter of `access()` to test the existence of *path*.

</div>

<div class="datadesc">

R_OK Value to include in the *mode* parameter of `access()` to test the readability of *path*.

</div>

<div class="datadesc">

W_OK Value to include in the *mode* parameter of `access()` to test the writability of *path*.

</div>

<div class="datadesc">

X_OK Value to include in the *mode* parameter of `access()` to determine if *path* can be executed.

</div>

<div class="funcdesc">

chdirpath Change the current working directory to *path*. Availability: Macintosh, Unix, Windows.

</div>

<div class="funcdesc">

getcwd Return a string representing the current working directory. Availability: Macintosh, Unix, Windows.

</div>

<div class="funcdesc">

chmodpath, mode Change the mode of *path* to the numeric *mode*. Availability: Unix, Windows.

</div>

<div class="funcdesc">

chownpath, uid, gid Change the owner and group id of *path* to the numeric *uid* and *gid*. Availability: Unix.

</div>

<div class="funcdesc">

linksrc, dst Create a hard link pointing to *src* named *dst*. Availability: Unix.

</div>

<div class="funcdesc">

listdirpath Return a list containing the names of the entries in the directory. The list is in arbitrary order. It does not include the special entries `’.’` and `’..’` even if they are present in the directory. Availability: Macintosh, Unix, Windows.

</div>

<div class="funcdesc">

lstatpath Like `stat()`, but do not follow symbolic links. Availability: Unix.

</div>

<div class="funcdesc">

mkfifopath Create a FIFO (a named pipe) named *path* with numeric mode *mode*. The default *mode* is `0666` (octal). The current umask value is first masked out from the mode. Availability: Unix.

FIFOs are pipes that can be accessed like regular files. FIFOs exist until they are deleted (for example with `os.unlink()`). Generally, FIFOs are used as rendezvous between “client” and “server” type processes: the server opens the FIFO for reading, and the client opens it for writing. Note that `mkfifo()` doesn’t open the FIFO — it just creates the rendezvous point.

</div>

<div class="funcdesc">

mkdirpath Create a directory named *path* with numeric mode *mode*. The default *mode* is `0777` (octal). On some systems, *mode* is ignored. Where it is used, the current umask value is first masked out. Availability: Macintosh, Unix, Windows.

</div>

<div class="funcdesc">

makedirspath Recursive directory creation function. Like `mkdir()`, but makes all intermediate-level directories needed to contain the leaf directory. Throws an `error` exception if the leaf directory already exists or cannot be created. The default *mode* is `0777` (octal). *New in version 1.5.2.*

</div>

<div class="funcdesc">

pathconfpath, name Return system configuration information relevant to a named file. *name* specifies the configuration value to retrieve; it may be a string which is the name of a defined system value; these names are specified in a number of standards (, Unix95, Unix98, and others). Some platforms define additional names as well. The names known to the host operating system are given in the `pathconf_names` dictionary. For configuration variables not included in that mapping, passing an integer for *name* is also accepted. Availability: Unix.

If *name* is a string and is not known, `ValueError` is raised. If a specific value for *name* is not supported by the host system, even if it is included in `pathconf_names`, an `OSError` is raised with for the error number.

</div>

<div class="datadesc">

pathconf_names Dictionary mapping names accepted by `pathconf()` and `fpathconf()` to the integer values defined for those names by the host operating system. This can be used to determine the set of names known to the system. Availability: Unix.

</div>

<div class="funcdesc">

readlinkpath Return a string representing the path to which the symbolic link points. Availability: Unix.

</div>

<div class="funcdesc">

removepath Remove the file *path*. See `rmdir()` below to remove a directory. This is identical to the `unlink()` function documented below. Availability: Macintosh, Unix, Windows.

</div>

<div class="funcdesc">

removedirspath Recursive directory removal function. Works like `rmdir()` except that, if the leaf directory is successfully removed, directories corresponding to rightmost path segments will be pruned way until either the whole path is consumed or an error is raised (which is ignored, because it generally means that a parent directory is not empty). Throws an `error` exception if the leaf directory could not be successfully removed. *New in version 1.5.2.*

</div>

<div class="funcdesc">

renamesrc, dst Rename the file or directory *src* to *dst*. Availability: Macintosh, Unix, Windows.

</div>

<div class="funcdesc">

renamesold, new Recursive directory or file renaming function. Works like `rename()`, except creation of any intermediate directories needed to make the new pathname good is attempted first. After the rename, directories corresponding to rightmost path segments of the old name will be pruned away using `removedirs()`.

Note: this function can fail with the new directory structure made if you lack permissions needed to remove the leaf directory or file. *New in version 1.5.2.*

</div>

<div class="funcdesc">

rmdirpath Remove the directory *path*. Availability: Macintosh, Unix, Windows.

</div>

<div class="funcdesc">

statpath Perform a system call on the given path. The return value is a tuple of at least 10 integers giving the most important (and portable) members of the *stat* structure, in the order `st_mode`, `st_ino`, `st_dev`, `st_nlink`, `st_uid`, `st_gid`, `st_size`, `st_atime`, `st_mtime`, `st_ctime`. More items may be added at the end by some implementations. (On MS Windows, some items are filled with dummy values.) Availability: Macintosh, Unix, Windows.

Note: The standard module `stat`defines functions and constants that are useful for extracting information from a `stat` structure.

</div>

<div class="funcdesc">

statvfspath Perform a system call on the given path. The return value is a tuple of 10 integers giving the most common members of the `statvfs` structure, in the order `f_bsize`, `f_frsize`, `f_blocks`, `f_bfree`, `f_bavail`, `f_files`, `f_ffree`, `f_favail`, `f_flag`, `f_namemax`. Availability: Unix.

Note: The standard module `statvfs`defines constants that are useful for extracting information from a `statvfs` structure.

</div>

<div class="funcdesc">

symlinksrc, dst Create a symbolic link pointing to *src* named *dst*. Availability: Unix.

</div>

<div class="funcdesc">

tempnam Return a unique path name that is reasonable for creating a temporary file. This will be an absolute path that names a potential directory entry in the directory *dir* or a common location for temporary files if *dir* is omitted or `None`. If given and not `None`, *prefix* is used to provide a short prefix to the filename. Applications are responsible for properly creating and managing files created using paths returned by `tempnam()`; no automatic cleanup is provided.

</div>

<div class="funcdesc">

tmpnam Return a unique path name that is reasonable for creating a temporary file. This will be an absolute path that names a potential directory entry in a common location for temporary files. Applications are responsible for properly creating and managing files created using paths returned by `tmpnam()`; no automatic cleanup is provided.

</div>

<div class="datadesc">

TMP_MAX The maximum number of unique names that `tmpnam()` will generate before reusing names.

</div>

<div class="funcdesc">

unlinkpath Remove the file *path*. This is the same function as `remove()`; the `unlink()` name is its traditional Unix name. Availability: Macintosh, Unix, Windows.

</div>

<div class="funcdesc">

utimepath, times Set the access and modified times of the file specified by *path*. If *times* is `None`, then the file’s access and modified times are set to the current time. Otherwise, *times* must be a 2-tuple of numbers, of the form `(`*`atime`*`, `*`mtime`*`)` which is used to set the access and modified times, respectively. *Changed in version \[.*added support for `None` for *times*\]2.0 Availability: Macintosh, Unix, Windows.

</div>

## Process Management <span id="os-process" label="os-process"></span>

These functions may be used to create and manage processes.

The various `exec*()` functions take a list of arguments for the new program loaded into the process. In each case, the first of these arguments is passed to the new program as its own name rather than as an argument a user may have typed on a command line. For the C programmer, this is the `argv[0]` passed to a program’s . For example, `os.execv(’/bin/echo’, [’foo’, ’bar’])` will only print `bar` on standard output; `foo` will seem to be ignored.

<div class="funcdesc">

abort Generate a signal to the current process. On Unix, the default behavior is to produce a core dump; on Windows, the process immediately returns an exit code of `3`. Be aware that programs which use `signal.signal()` to register a handler for will behave differently. Availability: Unix, Windows.

</div>

<div class="funcdesc">

execlpath, arg0, arg1, ... This is equivalent to `execv(`*`path`*`, (`*`arg0`*`, `*`arg1`*`, ...))`. Availability: Unix, Windows.

</div>

<div class="funcdesc">

execlepath, arg0, arg1, ..., env This is equivalent to `execve(`*`path`*`, (`*`arg0`*`, `*`arg1`*`, ...), `*`env`*`)`. Availability: Unix, Windows.

</div>

<div class="funcdesc">

execlppath, arg0, arg1, ... This is equivalent to `execvp(`*`path`*`, (`*`arg0`*`, `*`arg1`*`, ...))`. Availability: Unix, Windows.

</div>

<div class="funcdesc">

execvpath, args Execute the executable *path* with argument list *args*, replacing the current process (i.e., the Python interpreter). The argument list may be a tuple or list of strings. Availability: Unix, Windows.

</div>

<div class="funcdesc">

execvepath, args, env Execute the executable *path* with argument list *args*, and environment *env*, replacing the current process (i.e., the Python interpreter). The argument list may be a tuple or list of strings. The environment must be a dictionary mapping strings to strings. Availability: Unix, Windows.

</div>

<div class="funcdesc">

execvppath, args This is like `execv(`*`path`*`, `*`args`*`)` but duplicates the shell’s actions in searching for an executable file in a list of directories. The directory list is obtained from `environ[’PATH’]`. Availability: Unix, Windows.

</div>

<div class="funcdesc">

execvpepath, args, env This is a cross between `execve()` and `execvp()`. The directory list is obtained from *`env`*`[’PATH’]`. Availability: Unix, Windows.

</div>

<div class="funcdesc">

\_exitn Exit to the system with status *n*, without calling cleanup handlers, flushing stdio buffers, etc. Availability: Unix, Windows.

Note: the standard way to exit is `sys.exit(`*`n`*`)`. `_exit()` should normally only be used in the child process after a `fork()`.

</div>

<div class="funcdesc">

fork Fork a child process. Return `0` in the child, the child’s process id in the parent. Availability: Unix.

</div>

<div class="funcdesc">

forkpty Fork a child process, using a new pseudo-terminal as the child’s controlling terminal. Return a pair of `(`*`pid`*`, `*`fd`*`)`, where *pid* is `0` in the child, the new child’s process id in the parent, and `fd` is the file descriptor of the master end of the pseudo-terminal. For a more portable approach, use the `pty` module. Availability: Some flavors of Unix

</div>

<div class="funcdesc">

killpid, sig Kill the process *pid* with signal *sig*. Availability: Unix.

</div>

<div class="funcdesc">

niceincrement Add *increment* to the process’s “niceness”. Return the new niceness. Availability: Unix.

</div>

<div class="funcdesc">

plockop Lock program segments into memory. The value of *op* (defined in `<sys/lock.h>`) determines which segments are locked. Availability: Unix.

</div>

<div class="funcdesc">

spawnvmode, path, args Execute the program *path* in a new process, passing the arguments specified in *args* as command-line parameters. *args* may be a list or a tuple. *mode* is a magic operational constant. See the Visual C++ Runtime Library documentation for further information; the constants are exposed to the Python programmer as listed below. Availability: Unix, Windows. *New in version 1.5.2.*

</div>

<div class="funcdesc">

spawnvemode, path, args, env Execute the program *path* in a new process, passing the arguments specified in *args* as command-line parameters and the contents of the mapping *env* as the environment. *args* may be a list or a tuple. *mode* is a magic operational constant. See the Visual C++ Runtime Library documentation for further information; the constants are exposed to the Python programmer as listed below. Availability: Unix, Windows. *New in version 1.5.2.*

</div>

<div class="datadesc">

P_WAIT Possible values for the *mode* parameter to `spawnv()` and `spawnve()`. Availability: Unix, Windows. *New in version 1.5.2.*

</div>

<div class="datadesc">

P_OVERLAY Possible values for the *mode* parameter to `spawnv()` and `spawnve()`. These are less portable than those listed above. Availability: Windows. *New in version 1.5.2.*

</div>

<div class="funcdesc">

systemcommand Execute the command (a string) in a subshell. This is implemented by calling the Standard C function , and has the same limitations. Changes to `posix.environ`, `sys.stdin`, etc. are not reflected in the environment of the executed command. The return value is the exit status of the process encoded in the format specified for `wait()`, except on Windows 95 and 98, where it is always `0`. Note that does not specify the meaning of the return value of the C function, so the return value of the Python function is system-dependent. Availability: Unix, Windows.

</div>

<div class="funcdesc">

times Return a 5-tuple of floating point numbers indicating accumulated (CPU or other) times, in seconds. The items are: user time, system time, children’s user time, children’s system time, and elapsed real time since a fixed point in the past, in that order. See the Unix manual page or the corresponding Windows Platform API documentation. Availability: Unix, Windows.

</div>

<div class="funcdesc">

wait Wait for completion of a child process, and return a tuple containing its pid and exit status indication: a 16-bit number, whose low byte is the signal number that killed the process, and whose high byte is the exit status (if the signal number is zero); the high bit of the low byte is set if a core file was produced. Availability: Unix.

</div>

<div class="funcdesc">

waitpidpid, options Wait for completion of a child process given by process id *pid*, and return a tuple containing its process id and exit status indication (encoded as for `wait()`). The semantics of the call are affected by the value of the integer *options*, which should be `0` for normal operation. Availability: Unix.

If *pid* is greater than `0`, `waitpid()` requests status information for that specific process. If *pid* is `0`, the request is for the status of any child in the process group of the current process. If *pid* is `-1`, the request pertains to any child of the current process. If *pid* is less than `-1`, status is requested for any process in the process group `-`*`pid`* (the absolute value of *pid*).

</div>

<div class="datadesc">

WNOHANG The option for `waitpid()` to avoid hanging if no child process status is available immediately. Availability: Unix.

</div>

The following functions take a process status code as returned by `system()`, `wait()`, or `waitpid()` as a parameter. They may be used to determine the disposition of a process.

<div class="funcdesc">

WIFSTOPPEDstatus Return true if the process has been stopped. Availability: Unix.

</div>

<div class="funcdesc">

WIFSIGNALEDstatus Return true if the process exited due to a signal. Availability: Unix.

</div>

<div class="funcdesc">

WIFEXITEDstatus Return true if the process exited using the system call. Availability: Unix.

</div>

<div class="funcdesc">

WEXITSTATUSstatus If `WIFEXITED(`*`status`*`)` is true, return the integer parameter to the system call. Otherwise, the return value is meaningless. Availability: Unix.

</div>

<div class="funcdesc">

WSTOPSIGstatus Return the signal which caused the process to stop. Availability: Unix.

</div>

<div class="funcdesc">

WTERMSIGstatus Return the signal which caused the process to exit. Availability: Unix.

</div>

## Miscellaneous System Information <span id="os-path" label="os-path"></span>

<div class="funcdesc">

confstrname Return string-valued system configuration values. *name* specifies the configuration value to retrieve; it may be a string which is the name of a defined system value; these names are specified in a number of standards (, Unix95, Unix98, and others). Some platforms define additional names as well. The names known to the host operating system are given in the `confstr_names` dictionary. For configuration variables not included in that mapping, passing an integer for *name* is also accepted. Availability: Unix.

If the configuration value specified by *name* isn’t defined, the empty string is returned.

If *name* is a string and is not known, `ValueError` is raised. If a specific value for *name* is not supported by the host system, even if it is included in `confstr_names`, an `OSError` is raised with for the error number.

</div>

<div class="datadesc">

confstr_names Dictionary mapping names accepted by `confstr()` to the integer values defined for those names by the host operating system. This can be used to determine the set of names known to the system. Availability: Unix.

</div>

<div class="funcdesc">

sysconfname Return integer-valued system configuration values. If the configuration value specified by *name* isn’t defined, `-1` is returned. The comments regarding the *name* parameter for `confstr()` apply here as well; the dictionary that provides information on the known names is given by `sysconf_names`. Availability: Unix.

</div>

<div class="datadesc">

sysconf_names Dictionary mapping names accepted by `sysconf()` to the integer values defined for those names by the host operating system. This can be used to determine the set of names known to the system. Availability: Unix.

</div>

The follow data values are used to support path manipulation operations. These are defined for all platforms.

Higher-level operations on pathnames are defined in the `os.path` module.

<div class="datadesc">

curdir The constant string used by the OS to refer to the current directory, e.g. `’.’` for or `’:’` for the Macintosh.

</div>

<div class="datadesc">

pardir The constant string used by the OS to refer to the parent directory, e.g. `’..’` for or `’::’` for the Macintosh.

</div>

<div class="datadesc">

sep The character used by the OS to separate pathname components, e.g.  for or for the Macintosh. Note that knowing this is not sufficient to be able to parse or concatenate pathnames — use `os.path.split()` and `os.path.join()` — but it is occasionally useful.

</div>

<div class="datadesc">

altsep An alternative character used by the OS to separate pathname components, or `None` if only one separator character exists. This is set to on DOS and Windows systems where `sep` is a backslash.

</div>

<div class="datadesc">

pathsep The character conventionally used by the OS to separate search patch components (as in ), e.g.  for or for DOS and Windows.

</div>

<div class="datadesc">

defpath The default search path used by `exec*p*()` if the environment doesn’t have a `’PATH’` key.

</div>

<div class="datadesc">

linesep The string used to separate (or, rather, terminate) lines on the current platform. This may be a single character, e.g. `’n’` for or `’r’` for MacOS, or multiple characters, e.g. `’rn’` for MS-DOS and MS Windows.

</div>
# `panel` — None

*None*\
**Please note:** The FORMS library, to which the `fl`module described above interfaces, is a simpler and more accessible user interface library for use with GL than the `panel` module (besides also being by a Dutch author).

This module should be used instead of the built-in module `pnl`to interface with the *Panel Library*.

The module is too large to document here in its entirety. One interesting function:

<div class="funcdesc">

defpanellistfilename Parses a panel description file containing S-expressions written by the *Panel Editor* that accompanies the Panel Library and creates the described panels. It returns a list of panel objects.

</div>

**Warning:** the Python interpreter will dump core if you don’t create a GL window before calling `panel.mkpanel()` or `panel.defpanellist()`.

# `panelparser` — None

*None*\
This module defines a self-contained parser for S-expressions as output by the Panel Editor (which is written in Scheme so it can’t help writing S-expressions). The relevant function is `panelparser.parse_file(`*`file`*`)` which has a file object (not a filename!) as argument and returns a list of parsed S-expressions. Each S-expression is converted into a Python list, with atoms converted to Python strings and sub-expressions (recursively) to Python lists. For more details, read the module file.

# `pnl` — None

*None*\
This module provides access to the *Panel Library* built by NASA Ames(to get it, send e-mail to `panel-request@nas.nasa.gov`). All access to it should be done through the standard module `panel`, which transparently exports most functions from `pnl` but redefines `pnl.dopanel()`.

**Warning:** the Python interpreter will dump core if you don’t create a GL window before calling `pnl.mkpanel()`.

The module is too large to document here in its entirety.
# The Python Debugger

*The Python debugger for interactive interpreters.*\
The module `pdb` defines an interactive source code debuggerfor Python programs. It supports setting (conditional) breakpoints and single stepping at the source line level, inspection of stack frames, source code listing, and evaluation of arbitrary Python code in the context of any stack frame. It also supports post-mortem debugging and can be called under program control.

The debugger is extensible — it is actually defined as the class `Pdb`. This is currently undocumented but easily understood by reading the source. The extension interface uses the modules `bdb`(undocumented) and `cmd`.

The debugger’s prompt is `(Pdb) `. Typical usage to run a program under control of the debugger is:

    >>> import pdb
    >>> import mymodule
    >>> pdb.run('mymodule.test()')
    > <string>(0)?()
    (Pdb) continue
    > <string>(1)?()
    (Pdb) continue
    NameError: 'spam'
    > <string>(1)?()
    (Pdb) 

`pdb.py` can also be invoked as a script to debug other scripts. For example:

    python /usr/local/lib/python1.5/pdb.py myscript.py

Typical usage to inspect a crashed program is:

    >>> import pdb
    >>> import mymodule
    >>> mymodule.test()
    Traceback (innermost last):
      File "<stdin>", line 1, in ?
      File "./mymodule.py", line 4, in test
        test2()
      File "./mymodule.py", line 3, in test2
        print spam
    NameError: spam
    >>> pdb.pm()
    > ./mymodule.py(3)test2()
    -> print spam
    (Pdb) 

The module defines the following functions; each enters the debugger in a slightly different way:

<div class="funcdesc">

runstatement Execute the *statement* (given as a string) under debugger control. The debugger prompt appears before any code is executed; you can set breakpoints and type `continue`, or you can step through the statement using `step` or `next` (all these commands are explained below). The optional *globals* and *locals* arguments specify the environment in which the code is executed; by default the dictionary of the module `__main__` is used. (See the explanation of the statement or the `eval()` built-in function.)

</div>

<div class="funcdesc">

runevalexpression Evaluate the *expression* (given as a a string) under debugger control. When `runeval()` returns, it returns the value of the expression. Otherwise this function is similar to `run()`.

</div>

<div class="funcdesc">

runcallfunction Call the *function* (a function or method object, not a string) with the given arguments. When `runcall()` returns, it returns whatever the function call returned. The debugger prompt appears as soon as the function is entered.

</div>

<div class="funcdesc">

set_trace Enter the debugger at the calling stack frame. This is useful to hard-code a breakpoint at a given point in a program, even if the code is not otherwise being debugged (e.g. when an assertion fails).

</div>

<div class="funcdesc">

post_mortemtraceback Enter post-mortem debugging of the given *traceback* object.

</div>

<div class="funcdesc">

pm Enter post-mortem debugging of the traceback found in `sys.last_traceback`.

</div>

## Debugger Commands <span id="debugger-commands" label="debugger-commands"></span>

The debugger recognizes the following commands. Most commands can be abbreviated to one or two letters; e.g. `h(elp)` means that either `h` or `help` can be used to enter the help command (but not `he` or `hel`, nor `H` or `Help` or `HELP`). Arguments to commands must be separated by whitespace (spaces or tabs). Optional arguments are enclosed in square brackets (`[]`) in the command syntax; the square brackets must not be typed. Alternatives in the command syntax are separated by a vertical bar (`|`).

Entering a blank line repeats the last command entered. Exception: if the last command was a `list` command, the next 11 lines are listed.

Commands that the debugger doesn’t recognize are assumed to be Python statements and are executed in the context of the program being debugged. Python statements can also be prefixed with an exclamation point (`!`). This is a powerful way to inspect the program being debugged; it is even possible to change a variable or call a function. When an exception occurs in such a statement, the exception name is printed but the debugger’s state is not changed.

Multiple commands may be entered on a single line, separated by `;;`. (A single `;` is not used as it is the separator for multiple commands in a line that is passed to the Python parser.) No intelligence is applied to separating the commands; the input is split at the first `;;` pair, even if it is in the middle of a quoted string.

The debugger supports aliases. Aliases can have parameters which allows one a certain level of adaptability to the context under examination.

If a file `.pdbrc` exists in the user’s home directory or in the current directory, it is read in and executed as if it had been typed at the debugger prompt. This is particularly useful for aliases. If both files exist, the one in the home directory is read first and aliases defined there can be overridden by the local file.

h(elp)  
Without argument, print the list of available commands. With a *command* as argument, print help about that command. `help pdb` displays the full documentation file; if the environment variable is defined, the file is piped through that command instead. Since the *command* argument must be an identifier, `help exec` must be entered to get help on the `!` command.

w(here)  
Print a stack trace, with the most recent frame at the bottom. An arrow indicates the current frame, which determines the context of most commands.

d(own)  
Move the current frame one level down in the stack trace (to an newer frame).

u(p)  
Move the current frame one level up in the stack trace (to a older frame).

b(reak)  
With a *lineno* argument, set a break there in the current file. With a *function* argument, set a break at the first executable statement within that function. The line number may be prefixed with a filename and a colon, to specify a breakpoint in another file (probably one that hasn’t been loaded yet). The file is searched on `sys.path`. Note that each breakpoint is assigned a number to which all the other breakpoint commands refer.

If a second argument is present, it is an expression which must evaluate to true before the breakpoint is honored.

Without argument, list all breaks, including for each breakpoint, the number of times that breakpoint has been hit, the current ignore count, and the associated condition if any.

tbreak  
Temporary breakpoint, which is removed automatically when it is first hit. The arguments are the same as break.

cl(ear)  
With a space separated list of breakpoint numbers, clear those breakpoints. Without argument, clear all breaks (but first ask confirmation).

disable  
Disables the breakpoints given as a space separated list of breakpoint numbers. Disabling a breakpoint means it cannot cause the program to stop execution, but unlike clearing a breakpoint, it remains in the list of breakpoints and can be (re-)enabled.

enable  
Enables the breakpoints specified.

ignore *bpnumber*  
Sets the ignore count for the given breakpoint number. If count is omitted, the ignore count is set to 0. A breakpoint becomes active when the ignore count is zero. When non-zero, the count is decremented each time the breakpoint is reached and the breakpoint is not disabled and any associated condition evaluates to true.

condition *bpnumber*  
Condition is an expression which must evaluate to true before the breakpoint is honored. If condition is absent, any existing condition is removed; i.e., the breakpoint is made unconditional.

s(tep)  
Execute the current line, stop at the first possible occasion (either in a function that is called or on the next line in the current function).

n(ext)  
Continue execution until the next line in the current function is reached or it returns. (The difference between `next` and `step` is that `step` stops inside a called function, while `next` executes called functions at (nearly) full speed, only stopping at the next line in the current function.)

r(eturn)  
Continue execution until the current function returns.

c(ont(inue))  
Continue execution, only stop when a breakpoint is encountered.

l(ist)  
List source code for the current file. Without arguments, list 11 lines around the current line or continue the previous listing. With one argument, list 11 lines around at that line. With two arguments, list the given range; if the second argument is less than the first, it is interpreted as a count.

a(rgs)  
Print the argument list of the current function.

p *expression*  
Evaluate the *expression* in the current context and print its value. (Note: `print` can also be used, but is not a debugger command — this executes the Python statement.)

alias  
Creates an alias called *name* that executes *command*. The command must *not* be enclosed in quotes. Replaceable parameters can be indicated by `%1`, `%2`, and so on, while `%*` is replaced by all the parameters. If no command is given, the current alias for *name* is shown. If no arguments are given, all aliases are listed.

Aliases may be nested and can contain anything that can be legally typed at the pdb prompt. Note that internal pdb commands *can* be overridden by aliases. Such a command is then hidden until the alias is removed. Aliasing is recursively applied to the first word of the command line; all other words in the line are left alone.

As an example, here are two useful aliases (especially when placed in the `.pdbrc` file):

    #Print instance variables (usage "pi classInst")
    alias pi for k in %1.__dict__.keys(): print "%1.",k,"=",%1.__dict__[k]
    #Print instance variables in self
    alias ps pi self

unalias *name*  
Deletes the specified alias.

*statement*  
Execute the (one-line) *statement* in the context of the current stack frame. The exclamation point can be omitted unless the first word of the statement resembles a debugger command. To set a global variable, you can prefix the assignment command with a `global` command on the same line, e.g.:

    (Pdb) global list_options; list_options = ['-l']
    (Pdb)

q(uit)  
Quit from the debugger. The program being executed is aborted.

## How It Works

Some changes were made to the interpreter:

- `sys.settrace(`*`func`*`)` sets the global trace function

- there can also a local trace function (see later)

Trace functions have three arguments: *frame*, *event*, and *arg*. *frame* is the current stack frame. *event* is a string: `’call’`, `’line’`, `’return’` or `’exception’`. *arg* depends on the event type.

The global trace function is invoked (with *event* set to `’call’`) whenever a new local scope is entered; it should return a reference to the local trace function to be used that scope, or `None` if the scope shouldn’t be traced.

The local trace function should return a reference to itself (or to another function for further tracing in that scope), or `None` to turn off tracing in that scope.

Instance methods are accepted (and very useful!) as trace functions.

The events have the following meaning:

`’call’`  
A function is called (or some other code block entered). The global trace function is called; arg is the argument list to the function; the return value specifies the local trace function.

`’line’`  
The interpreter is about to execute a new line of code (sometimes multiple line events on one line exist). The local trace function is called; arg in None; the return value specifies the new local trace function.

`’return’`  
A function (or other code block) is about to return. The local trace function is called; arg is the value that will be returned. The trace function’s return value is ignored.

`’exception’`  
An exception has occurred. The local trace function is called; arg is a triple (exception, value, traceback); the return value specifies the new local trace function

Note that as an exception is propagated down the chain of callers, an `’exception’` event is generated at each level.

For more information on code and frame objects, refer to the Python Reference Manual.
# `pipes` — Interface to shell pipelines

*A Python interface to Unix shell pipelines.*\
The `pipes` module defines a class to abstract the concept of a *pipeline* — a sequence of convertors from one file to another.

Because the module uses command lines, a or compatible shell for `os.system()` and `os.popen()` is required.

The `pipes` module defines the following class:

<div class="classdesc">

Template An abstraction of a pipeline.

</div>

Example:

    >>> import pipes
    >>> t=pipes.Template()
    >>> t.append('tr a-z A-Z', '--')
    >>> f=t.open('/tmp/1', 'w')
    >>> f.write('hello world')
    >>> f.close()
    >>> open('/tmp/1').read()
    'HELLO WORLD'

## Template Objects <span id="template-objects" label="template-objects"></span>

Template objects following methods:

<div class="methoddesc">

reset Restore a pipeline template to its initial state.

</div>

<div class="methoddesc">

clone Return a new, equivalent, pipeline template.

</div>

<div class="methoddesc">

debugflag If *flag* is true, turn debugging on. Otherwise, turn debugging off. When debugging is on, commands to be executed are printed, and the shell is given `set -x` command to be more verbose.

</div>

<div class="methoddesc">

appendcmd, kind Append a new action at the end. The *cmd* variable must be a valid bourne shell command. The *kind* variable consists of two letters.

The first letter can be either of `’-’` (which means the command reads its standard input), `’f’` (which means the commands reads a given file on the command line) or `’.’` (which means the commands reads no input, and hence must be first.)

Similarly, the second letter can be either of `’-’` (which means the command writes to standard output), `’f’` (which means the command writes a file on the command line) or `’.’` (which means the command does not write anything, and hence must be last.)

</div>

<div class="methoddesc">

prependcmd, kind Add a new action at the beginning. See `append()` for explanations of the arguments.

</div>

<div class="methoddesc">

openfile, mode Return a file-like object, open to *file*, but read from or written to by the pipeline. Note that only one of `’r’`, `’w’` may be given.

</div>

<div class="methoddesc">

copyinfile, outfile Copy *infile* to *outfile* through the pipe.

</div>
# `popen2` — Subprocesses with accessible I/O streams

*Subprocesses with accessible standard I/O streams.*\
This module allows you to spawn processes and connect their input/output/error pipes and obtain their return codes under Unix. Similar functionality exists for Windows platforms using the `win32pipe` module provided as part of Mark Hammond’s Windows extensions.

The primary interface offered by this module is a pair of factory functions:

<div class="funcdesc">

popen2cmd Executes *cmd* as a sub-process. If *bufsize* is specified, it specifies the buffer size for the I/O pipes. Returns the file objects `(`*`child_stdout`*`, `*`child_stdin`*`)`.

</div>

<div class="funcdesc">

popen3cmd Executes *cmd* as a sub-process. If *bufsize* is specified, it specifies the buffer size for the I/O pipes. Returns the file objects `(`*`child_stdout`*`, `*`child_stdin`*`, `*`child_stderr`*`)`.

</div>

The class defining the objects returned by the factory functions is also available:

<div class="classdesc">

Popen3cmd This class represents a child process. Normally, `Popen3` instances are created using the factory functions described above.

If not using one off the helper functions to create `Popen3` objects, the parameter *cmd* is the shell command to execute in a sub-process. The *capturestderr* flag, if true, specifies that the object should capture standard error output of the child process. The default is false. If the *bufsize* parameter is specified, it specifies the size of the I/O buffers to/from the child process.

</div>

## Popen3 Objects <span id="popen3-objects" label="popen3-objects"></span>

Instances of the `Popen3` class have the following methods:

<div class="methoddesc">

poll Returns `-1` if child process hasn’t completed yet, or its return code otherwise.

</div>

<div class="methoddesc">

wait Waits for and returns the return code of the child process.

</div>

The following attributes of `Popen3` objects are also available:

<div class="memberdesc">

fromchild A file object that provides output from the child process.

</div>

<div class="memberdesc">

tochild A file object that provides input to the child process.

</div>

<div class="memberdesc">

childerr Where the standard error from the child process goes is *capturestderr* was true for the constructor, or `None`.

</div>

<div class="memberdesc">

pid The process ID of the child process.

</div>
# `poplib` — POP3 protocol client

*POP3 protocol client (requires sockets).*\
This module defines a class, `POP3`, which encapsulates a connection to an POP3 server and implements protocol as defined in . The `POP3` class supports both the minimal and optional command sets.

A single class is provided by the `poplib` module:

<div class="classdesc">

POP3host This class implements the actual POP3 protocol. The connection is created when the instance is initialized. If *port* is omitted, the standard POP3 port (110) is used.

</div>

One exception is defined as an attribute of the `poplib` module:

<div class="excdesc">

error_proto Exception raised on any errors. The reason for the exception is passed to the constructor as a string.

</div>

## POP3 Objects <span id="pop3-objects" label="pop3-objects"></span>

All POP3 commands are represented by methods of the same name, in lower-case; most return the response text sent by the server.

An `POP3` instance has the following methods:

<div class="methoddesc">

getwelcome Returns the greeting string sent by the POP3 server.

</div>

<div class="methoddesc">

userusername Send user command, response should indicate that a password is required.

</div>

<div class="methoddesc">

pass\_password Send password, response includes message count and mailbox size. Note: the mailbox on the server is locked until `quit()` is called.

</div>

<div class="methoddesc">

apopuser, secret Use the more secure APOP authentication to log into the POP3 server.

</div>

<div class="methoddesc">

rpopuser Use RPOP authentication (similar to UNIX r-commands) to log into POP3 server.

</div>

<div class="methoddesc">

stat Get mailbox status. The result is a tuple of 2 integers: `(`*`message count`*`, `*`mailbox size`*`)`.

</div>

<div class="methoddesc">

list Request message list, result is in the form `(`*`response`*`, [’mesg_num octets’, ...])`. If *which* is set, it is the message to list.

</div>

<div class="methoddesc">

retrwhich Retrieve whole message number *which*. Result is in form `(`*`response`*`, [’line’, ...], `*`octets`*`)`.

</div>

<div class="methoddesc">

delewhich Delete message number *which*.

</div>

<div class="methoddesc">

rset Remove any deletion marks for the mailbox.

</div>

<div class="methoddesc">

noop Do nothing. Might be used as a keep-alive.

</div>

<div class="methoddesc">

quit Signoff: commit changes, unlock mailbox, drop connection.

</div>

<div class="methoddesc">

topwhich, howmuch Retrieves the message header plus *howmuch* lines of the message after the header of message number *which*. Result is in form `(`*`response`*`, [’line’, ...], `*`octets`*`)`.

</div>

<div class="methoddesc">

uidl Return message digest (unique id) list. If *which* is specified, result contains the unique id for that message in the form `’`*`response`*` `*`mesgnum`*` `*`uid`*, otherwise result is list `(`*`response`*`, [’mesgnum uid’, ...], `*`octets`*`)`.

</div>

## POP3 Example <span id="pop3-example" label="pop3-example"></span>

Here is a minimal example (without error checking) that opens a mailbox and retrieves and prints all messages:

    import getpass, poplib

    M = poplib.POP3('localhost')
    M.user(getpass.getuser())
    M.pass_(getpass.getpass())
    numMessages = len(M.list()[1])
    for i in range(numMessages):
        for j in M.retr(i+1)[1]:
            print j

At the end of the module, there is a test section that contains a more extensive example of usage.
# `posix` — The most common system calls

*The most common system calls (normally used via module `os`).*\
This module provides access to operating system functionality that is standardized by the C Standard and the standard (a thinly disguised Unix interface).

**Do not import this module directly.** Instead, import the module `os`, which provides a *portable* version of this interface. On Unix, the `os` module provides a superset of the `posix` interface. On non-Unix operating systems the `posix` module is not available, but a subset is always available through the `os` interface. Once `os` is imported, there is *no* performance penalty in using it instead of `posix`. In addition, `os`provides some additional functionality, such as automatically calling `putenv()` when an entry in `os.environ` is changed.

The descriptions below are very terse; refer to the corresponding Unix manual (or documentation) entry for more information. Arguments called *path* refer to a pathname given as a string.

Errors are reported as exceptions; the usual exceptions are given for type errors, while errors reported by the system calls raise `error` (a synonym for the standard exception `OSError`), described below.

## Large File Support <span id="posix-large-files" label="posix-large-files"></span>

Several operating systems (including AIX, HPUX, Irix and Solaris) provide support for files that are larger than 2 Gb from a C programming model where `int` and `long` are 32-bit values. This is typically accomplished by defining the relevant size and offset types as 64-bit values. Such files are sometimes referred to as *large files*.

Large file support is enabled in Python when the size of an `off_t` is larger than a `long` and the `long long` type is available and is at least as large as an `off_t`. Python longs are then used to represent file sizes, offsets and other values that can exceed the range of a Python int. It may be necessary to configure and compile Python with certain compiler flags to enable this mode. For example, it is enabled by default with recent versions of Irix, but with Solaris 2.6 and 2.7 you need to do something like:

    CFLAGS="`getconf LFS_CFLAGS`" OPT="-g -O2 $CFLAGS" \
            configure

## Module Contents <span id="posix-contents" label="posix-contents"></span>

Module `posix` defines the following data item:

<div class="datadesc">

environ A dictionary representing the string environment at the time the interpreter was started. For example, `environ[’HOME’]` is the pathname of your home directory, equivalent to `getenv("HOME")` in C.

Modifying this dictionary does not affect the string environment passed on by `execv()`, `popen()` or `system()`; if you need to change the environment, pass `environ` to `execve()` or add variable assignments and export statements to the command string for `system()` or `popen()`.

**Note:** The `os` module provides an alternate implementation of `environ` which updates the environment on modification. Note also that updating `os.environ` will render this dictionary obsolete. Use of the `os` for this is recommended over direct access to the `posix` module.

</div>

Additional contents of this module should only be accessed via the `os` module; refer to the documentation for that module for further information.
# `posixfile` — File-like objects with locking support

*A file-like object with support for locking.*\
**Note:** This module will become obsolete in a future release. The locking operation that it provides is done better and more portably by the `fcntl.lockf()` call. This module implements some additional functionality over the built-in file objects. In particular, it implements file locking, control over the file flags, and an easy interface to duplicate the file object. The module defines a new file object, the posixfile object. It has all the standard file object methods and adds the methods described below. This module only works for certain flavors of Unix, since it uses `fcntl.fcntl()` for file locking. To instantiate a posixfile object, use the `open()` function in the `posixfile` module. The resulting object looks and feels roughly the same as a standard file object.

The `posixfile` module defines the following constants:

<div class="datadesc">

SEEK_SET Offset is calculated from the start of the file.

</div>

<div class="datadesc">

SEEK_CUR Offset is calculated from the current position in the file.

</div>

<div class="datadesc">

SEEK_END Offset is calculated from the end of the file.

</div>

The `posixfile` module defines the following functions:

<div class="funcdesc">

openfilename Create a new posixfile object with the given filename and mode. The *filename*, *mode* and *bufsize* arguments are interpreted the same way as by the built-in `open()` function.

</div>

<div class="funcdesc">

fileopenfileobject Create a new posixfile object with the given standard file object. The resulting object has the same filename and mode as the original file object.

</div>

The posixfile object defines the following additional methods:

<div class="funcdesc">

lockfmt, Lock the specified section of the file that the file object is referring to. The format is explained below in a table. The *len* argument specifies the length of the section that should be locked. The default is `0`. *start* specifies the starting offset of the section, where the default is `0`. The *whence* argument specifies where the offset is relative to. It accepts one of the constants , or . The default is . For more information about the arguments refer to the manual page on your system.

</div>

<div class="funcdesc">

flags Set the specified flags for the file that the file object is referring to. The new flags are ORed with the old flags, unless specified otherwise. The format is explained below in a table. Without the *flags* argument a string indicating the current flags is returned (this is the same as the `?` modifier). For more information about the flags refer to the manual page on your system.

</div>

<div class="funcdesc">

dup Duplicate the file object and the underlying file pointer and file descriptor. The resulting object behaves as if it were newly opened.

</div>

<div class="funcdesc">

dup2fd Duplicate the file object and the underlying file pointer and file descriptor. The new object will have the given file descriptor. Otherwise the resulting object behaves as if it were newly opened.

</div>

<div class="funcdesc">

file Return the standard file object that the posixfile object is based on. This is sometimes necessary for functions that insist on a standard file object.

</div>

All methods raise `IOError` when the request fails.

Format characters for the `lock()` method have the following meaning:

|                 |                                                |
|:----------------|:-----------------------------------------------|
| FormatMeaning u | unlock the specified region                    |
| r               | request a read lock for the specified section  |
| w               | request a write lock for the specified section |
|                 |                                                |

In addition the following modifiers can be added to the format:

|  |  |  |
|:---|:---|:---|
| ModifierMeaningNotes \| | wait until the lock has been granted |  |
| ? | return the first lock conflicting with the requested lock, or |  |
| if there is no conflict. |  |  |

Note:

\(1\)  
The lock returned is in the format `(`*`mode`*`, `*`len`*`, `*`start`*`, `*`whence`*`, `*`pid`*`)` where *mode* is a character representing the type of lock (’r’ or ’w’). This modifier prevents a request from being granted; it is for query purposes only.

Format characters for the `flags()` method have the following meanings:

|                 |                                               |
|:----------------|:----------------------------------------------|
| FormatMeaning a | append only flag                              |
| c               | close on exec flag                            |
| n               | no delay flag (also called non-blocking flag) |
| s               | synchronization flag                          |
|                 |                                               |

In addition the following modifiers can be added to the format:

|  |  |  |
|:---|:---|:---|
| ModifierMeaningNotes ! | turn the specified flags ’off’, instead of the default ’on’ | \(1\) |
| = | replace the flags, instead of the default ’OR’ operation | \(1\) |
| ? | return a string in which the characters represent the flags that are set. | \(2\) |
|  |  |  |

Notes:

\(1\)  
The `!` and `=` modifiers are mutually exclusive.

\(2\)  
This string represents the flags after they may have been altered by the same call.

Examples:

    import posixfile

    file = posixfile.open('/tmp/test', 'w')
    file.lock('w|')
    ...
    file.lock('u')
    file.close()
# `os.path` — Common pathname manipulations

*Common pathname manipulations.*\
This module implements some useful functions on pathnames.

<div class="funcdesc">

abspathpath Return a normalized absolutized version of the pathname *path*. On most platforms, this is equivalent to `normpath(join(os.getcwd(), `*`path`*`))`. *New in version 1.5.2.*

</div>

<div class="funcdesc">

basenamepath Return the base name of pathname *path*. This is the second half of the pair returned by `split(`*`path`*`)`.

</div>

<div class="funcdesc">

commonprefixlist Return the longest path prefix (taken character-by-character) that is a prefix of all paths in *list*. If *list* is empty, return the empty string (`’’`). Note that this may return invalid paths because it works a character at a time.

</div>

<div class="funcdesc">

dirnamepath Return the directory name of pathname *path*. This is the first half of the pair returned by `split(`*`path`*`)`.

</div>

<div class="funcdesc">

existspath Return true if *path* refers to an existing path.

</div>

<div class="funcdesc">

expanduserpath Return the argument with an initial component of `~` or *`user`* replaced by that *user*’s home directory. An initial `~` is replaced by the environment variable ; an initial *`user`* is looked up in the password directory through the built-in module `pwd`. If the expansion fails, or if the path does not begin with a tilde, the path is returned unchanged. On the Macintosh, this always returns *path* unchanged.

</div>

<div class="funcdesc">

expandvarspath Return the argument with environment variables expanded. Substrings of the form `$`*`name`* or `${`*`name`*`}` are replaced by the value of environment variable *name*. Malformed variable names and references to non-existing variables are left unchanged. On the Macintosh, this always returns *path* unchanged.

</div>

<div class="funcdesc">

getatimepath Return the time of last access of *filename*. The return value is integer giving the number of seconds since the epoch (see the `time` module). Raise `os.error` if the file does not exist or is inaccessible. *New in version 1.5.2.*

</div>

<div class="funcdesc">

getmtimepath Return the time of last modification of *filename*. The return value is integer giving the number of seconds since the epoch (see the `time` module). Raise `os.error` if the file does not exist or is inaccessible. *New in version 1.5.2.*

</div>

<div class="funcdesc">

getsizepath Return the size, in bytes, of *filename*. Raise `os.error` if the file does not exist or is inaccessible. *New in version 1.5.2.*

</div>

<div class="funcdesc">

isabspath Return true if *path* is an absolute pathname (begins with a slash).

</div>

<div class="funcdesc">

isfilepath Return true if *path* is an existing regular file. This follows symbolic links, so both `islink()` and `isfile()` can be true for the same path.

</div>

<div class="funcdesc">

isdirpath Return true if *path* is an existing directory. This follows symbolic links, so both `islink()` and `isdir()` can be true for the same path.

</div>

<div class="funcdesc">

islinkpath Return true if *path* refers to a directory entry that is a symbolic link. Always false if symbolic links are not supported.

</div>

<div class="funcdesc">

ismountpath Return true if pathname *path* is a *mount point*: a point in a file system where a different file system has been mounted. The function checks whether *path*’s parent, *`path`*`/..`, is on a different device than *path*, or whether *`path`*`/..` and *path* point to the same i-node on the same device — this should detect mount points for all Unix and variants.

</div>

<div class="funcdesc">

joinpath1 Joins one or more path components intelligently. If any component is an absolute path, all previous components are thrown away, and joining continues. The return value is the concatenation of *path1*, and optionally *path2*, etc., with exactly one slash (`’/’`) inserted between components, unless *path* is empty.

</div>

<div class="funcdesc">

normcasepath Normalize the case of a pathname. On Unix, this returns the path unchanged; on case-insensitive filesystems, it converts the path to lowercase. On Windows, it also converts forward slashes to backward slashes.

</div>

<div class="funcdesc">

normpathpath Normalize a pathname. This collapses redundant separators and up-level references, e.g. `A//B`, `A/./B` and `A/foo/../B` all become `A/B`. It does not normalize the case (use `normcase()` for that). On Windows, it converts forward slashes to backward slashes.

</div>

<div class="funcdesc">

samefilepath1, path2 Return true if both pathname arguments refer to the same file or directory (as indicated by device number and i-node number). Raise an exception if a `os.stat()` call on either pathname fails. Availability: Macintosh, Unix.

</div>

<div class="funcdesc">

sameopenfilefp1, fp2 Return true if the file objects *fp1* and *fp2* refer to the same file. The two file objects may represent different file descriptors. Availability: Macintosh, Unix.

</div>

<div class="funcdesc">

samestatstat1, stat2 Return true if the stat tuples *stat1* and *stat2* refer to the same file. These structures may have been returned by `fstat()`, `lstat()`, or `stat()`. This function implements the underlying comparison used by `samefile()` and `sameopenfile()`. Availability: Macintosh, Unix.

</div>

<div class="funcdesc">

splitpath Split the pathname *path* into a pair, `(`*`head`*`, `*`tail`*`)` where *tail* is the last pathname component and *head* is everything leading up to that. The *tail* part will never contain a slash; if *path* ends in a slash, *tail* will be empty. If there is no slash in *path*, *head* will be empty. If *path* is empty, both *head* and *tail* are empty. Trailing slashes are stripped from *head* unless it is the root (one or more slashes only). In nearly all cases, `join(`*`head`*`, `*`tail`*`)` equals *path* (the only exception being when there were multiple slashes separating *head* from *tail*).

</div>

<div class="funcdesc">

splitdrivepath Split the pathname *path* into a pair `(`*`drive`*`, `*`tail`*`)` where *drive* is either a drive specification or the empty string. On systems which do not use drive specifications, *drive* will always be the empty string. In all cases, *`drive`*` + `*`tail`* will be the same as *path*.

</div>

<div class="funcdesc">

splitextpath Split the pathname *path* into a pair `(`*`root`*`, `*`ext`*`)` such that *`root`*` + `*`ext`*` == `*`path`*, and *ext* is empty or begins with a period and contains at most one period.

</div>

<div class="funcdesc">

walkpath, visit, arg Calls the function *visit* with arguments `(`*`arg`*`, `*`dirname`*`, `*`names`*`)` for each directory in the directory tree rooted at *path* (including *path* itself, if it is a directory). The argument *dirname* specifies the visited directory, the argument *names* lists the files in the directory (gotten from `os.listdir(`*`dirname`*`)`). The *visit* function may modify *names* to influence the set of directories visited below *dirname*, e.g., to avoid visiting certain parts of the tree. (The object referred to by *names* must be modified in place, using or slice assignment.)

</div>
# `pprint` — Data pretty printer.

*Data pretty printer.*\
The `pprint` module provides a capability to “pretty-print” arbitrary Python data structures in a form which can be used as input to the interpreter. If the formatted structures include objects which are not fundamental Python types, the representation may not be loadable. This may be the case if objects such as files, sockets, classes, or instances are included, as well as many other builtin objects which are not representable as Python constants.

The formatted representation keeps objects on a single line if it can, and breaks them onto multiple lines if they don’t fit within the allowed width. Construct `PrettyPrinter` objects explicitly if you need to adjust the width constraint.

The `pprint` module defines one class:

<div class="classdesc">

PrettyPrinter... Construct a `PrettyPrinter` instance. This constructor understands several keyword parameters. An output stream may be set using the *stream* keyword; the only method used on the stream object is the file protocol’s `write()` method. If not specified, the `PrettyPrinter` adopts `sys.stdout`. Three additional parameters may be used to control the formatted representation. The keywords are *indent*, *depth*, and *width*. The amount of indentation added for each recursive level is specified by *indent*; the default is one. Other values can cause output to look a little odd, but can make nesting easier to spot. The number of levels which may be printed is controlled by *depth*; if the data structure being printed is too deep, the next contained level is replaced by `...`. By default, there is no constraint on the depth of the objects being formatted. The desired output width is constrained using the *width* parameter; the default is eighty characters. If a structure cannot be formatted within the constrained width, a best effort will be made.

    >>> import pprint, sys
    >>> stuff = sys.path[:]
    >>> stuff.insert(0, stuff[:])
    >>> pp = pprint.PrettyPrinter(indent=4)
    >>> pp.pprint(stuff)
    [   [   '',
            '/usr/local/lib/python1.5',
            '/usr/local/lib/python1.5/test',
            '/usr/local/lib/python1.5/sunos5',
            '/usr/local/lib/python1.5/sharedmodules',
            '/usr/local/lib/python1.5/tkinter'],
        '',
        '/usr/local/lib/python1.5',
        '/usr/local/lib/python1.5/test',
        '/usr/local/lib/python1.5/sunos5',
        '/usr/local/lib/python1.5/sharedmodules',
        '/usr/local/lib/python1.5/tkinter']
    >>>
    >>> import parser
    >>> tup = parser.ast2tuple(
    ...     parser.suite(open('pprint.py').read()))[1][1][1]
    >>> pp = pprint.PrettyPrinter(depth=6)
    >>> pp.pprint(tup)
    (266, (267, (307, (287, (288, (...))))))

</div>

The `PrettyPrinter` class supports several derivative functions:

<div class="funcdesc">

pformatobject Return the formatted representation of *object* as a string. The default parameters for formatting are used.

</div>

<div class="funcdesc">

pprintobject Prints the formatted representation of *object* on *stream*, followed by a newline. If *stream* is omitted, `sys.stdout` is used. This may be used in the interactive interpreter instead of a statement for inspecting values. The default parameters for formatting are used.

    >>> stuff = sys.path[:]
    >>> stuff.insert(0, stuff)
    >>> pprint.pprint(stuff)
    [<Recursion on list with id=869440>,
     '',
     '/usr/local/lib/python1.5',
     '/usr/local/lib/python1.5/test',
     '/usr/local/lib/python1.5/sunos5',
     '/usr/local/lib/python1.5/sharedmodules',
     '/usr/local/lib/python1.5/tkinter']

</div>

<div class="funcdesc">

isreadableobject Determine if the formatted representation of *object* is “readable,” or can be used to reconstruct the value using `eval()`. This always returns false for recursive objects.

    >>> pprint.isreadable(stuff)
    0

</div>

<div class="funcdesc">

isrecursiveobject Determine if *object* requires a recursive representation.

</div>

One more support function is also defined:

<div class="funcdesc">

safereprobject Return a string representation of *object*, protected against recursive data structures. If the representation of *object* exposes a recursive entry, the recursive reference will be represented as `<Recursion on `*`typename`*` with id=`*`number`*`>`. The representation is not otherwise formatted.

</div>

    >>> pprint.saferepr(stuff)
    "[<Recursion on list with id=682968>, '', '/usr/local/lib/python1.5', '/usr/loca
    l/lib/python1.5/test', '/usr/local/lib/python1.5/sunos5', '/usr/local/lib/python
    1.5/sharedmodules', '/usr/local/lib/python1.5/tkinter']"

## PrettyPrinter Objects

`PrettyPrinter` instances have the following methods:

<div class="methoddesc">

pformatobject Return the formatted representation of *object*. This takes into Account the options passed to the `PrettyPrinter` constructor.

</div>

<div class="methoddesc">

pprintobject Print the formatted representation of *object* on the configured stream, followed by a newline.

</div>

The following methods provide the implementations for the corresponding functions of the same names. Using these methods on an instance is slightly more efficient since new `PrettyPrinter` objects don’t need to be created.

<div class="methoddesc">

isreadableobject Determine if the formatted representation of the object is “readable,” or can be used to reconstruct the value using `eval()`. Note that this returns false for recursive objects. If the *depth* parameter of the `PrettyPrinter` is set and the object is deeper than allowed, this returns false.

</div>

<div class="methoddesc">

isrecursiveobject Determine if the object requires a recursive representation.

</div>
# The Python Profiler <span id="profile" label="profile"></span>

Copyright © 1994, by InfoSeek Corporation, all rights reserved. Written by James Roskind.[^1]

Permission to use, copy, modify, and distribute this Python software and its associated documentation for any purpose (subject to the restriction in the following sentence) without fee is hereby granted, provided that the above copyright notice appears in all copies, and that both that copyright notice and this permission notice appear in supporting documentation, and that the name of InfoSeek not be used in advertising or publicity pertaining to distribution of the software without specific, written prior permission. This permission is explicitly restricted to the copying and modification of the software to remain in Python, compiled Python, or other languages (such as C) wherein the modified or derived code is exclusively imported into a Python module.

INFOSEEK CORPORATION DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL INFOSEEK CORPORATION BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

The profiler was written after only programming in Python for 3 weeks. As a result, it is probably clumsy code, but I don’t know for sure yet ’cause I’m a beginner :-). I did work hard to make the code run fast, so that profiling would be a reasonable thing to do. I tried not to repeat code fragments, but I’m sure I did some stuff in really awkward ways at times. Please send suggestions for improvements to: `jar@netscape.com`. I won’t promise *any* support. ...but I’d appreciate the feedback.

## Introduction to the profiler

A *profiler* is a program that describes the run time performance of a program, providing a variety of statistics. This documentation describes the profiler functionality provided in the modules `profile` and `pstats`. This profiler provides *deterministic profiling* of any Python programs. It also provides a series of report generation tools to allow users to rapidly examine the results of a profile operation.

## How Is This Profiler Different From The Old Profiler?

(This section is of historical importance only; the old profiler discussed here was last seen in Python 1.1.)

The big changes from old profiling module are that you get more information, and you pay less CPU time. It’s not a trade-off, it’s a trade-up.

To be specific:

Bugs removed:  
Local stack frame is no longer molested, execution time is now charged to correct functions.

Accuracy increased:  
Profiler execution time is no longer charged to user’s code, calibration for platform is supported, file reads are not done *by* profiler *during* profiling (and charged to user’s code!).

Speed increased:  
Overhead CPU cost was reduced by more than a factor of two (perhaps a factor of five), lightweight profiler module is all that must be loaded, and the report generating module (`pstats`) is not needed during profiling.

Recursive functions support:  
Cumulative times in recursive functions are correctly calculated; recursive entries are counted.

Large growth in report generating UI:  
Distinct profiles runs can be added together forming a comprehensive report; functions that import statistics take arbitrary lists of files; sorting criteria is now based on keywords (instead of 4 integer options); reports shows what functions were profiled as well as what profile file was referenced; output format has been improved.

## Instant Users Manual <span id="profile-instant" label="profile-instant"></span>

This section is provided for users that “don’t want to read the manual.” It provides a very brief overview, and allows a user to rapidly perform profiling on an existing application.

To profile an application with a main entry point of `foo()`, you would add the following to your module:

    import profile
    profile.run('foo()')

The above action would cause `foo()` to be run, and a series of informative lines (the profile) to be printed. The above approach is most useful when working with the interpreter. If you would like to save the results of a profile into a file for later examination, you can supply a file name as the second argument to the `run()` function:

    import profile
    profile.run('foo()', 'fooprof')

The file `profile.py` can also be invoked as a script to profile another script. For example:

    python /usr/local/lib/python1.5/profile.py myscript.py

When you wish to review the profile, you should use the methods in the `pstats` module. Typically you would load the statistics data as follows:

    import pstats
    p = pstats.Stats('fooprof')

The class `Stats` (the above code just created an instance of this class) has a variety of methods for manipulating and printing the data that was just read into `p`. When you ran `profile.run()` above, what was printed was the result of three method calls:

    p.strip_dirs().sort_stats(-1).print_stats()

The first method removed the extraneous path from all the module names. The second method sorted all the entries according to the standard module/line/name string that is printed (this is to comply with the semantics of the old profiler). The third method printed out all the statistics. You might try the following sort calls:

    p.sort_stats('name')
    p.print_stats()

The first call will actually sort the list by function name, and the second call will print out the statistics. The following are some interesting calls to experiment with:

    p.sort_stats('cumulative').print_stats(10)

This sorts the profile by cumulative time in a function, and then only prints the ten most significant lines. If you want to understand what algorithms are taking time, the above line is what you would use.

If you were looking to see what functions were looping a lot, and taking a lot of time, you would do:

    p.sort_stats('time').print_stats(10)

to sort according to time spent within each function, and then print the statistics for the top ten functions.

You might also try:

    p.sort_stats('file').print_stats('__init__')

This will sort all the statistics by file name, and then print out statistics for only the class init methods (’cause they are spelled with `__init__` in them). As one final example, you could try:

    p.sort_stats('time', 'cum').print_stats(.5, 'init')

This line sorts statistics with a primary key of time, and a secondary key of cumulative time, and then prints out some of the statistics. To be specific, the list is first culled down to 50% (re: `.5`) of its original size, then only lines containing `init` are maintained, and that sub-sub-list is printed.

If you wondered what functions called the above functions, you could now (`p` is still sorted according to the last criteria) do:

    p.print_callers(.5, 'init')

and you would get a list of callers for each of the listed functions.

If you want more functionality, you’re going to have to read the manual, or guess what the following functions do:

    p.print_callees()
    p.add('fooprof')

## What Is Deterministic Profiling?

*Deterministic profiling* is meant to reflect the fact that all *function call*, *function return*, and *exception* events are monitored, and precise timings are made for the intervals between these events (during which time the user’s code is executing). In contrast, *statistical profiling* (which is not done by this module) randomly samples the effective instruction pointer, and deduces where time is being spent. The latter technique traditionally involves less overhead (as the code does not need to be instrumented), but provides only relative indications of where time is being spent.

In Python, since there is an interpreter active during execution, the presence of instrumented code is not required to do deterministic profiling. Python automatically provides a *hook* (optional callback) for each event. In addition, the interpreted nature of Python tends to add so much overhead to execution, that deterministic profiling tends to only add small processing overhead in typical applications. The result is that deterministic profiling is not that expensive, yet provides extensive run time statistics about the execution of a Python program.

Call count statistics can be used to identify bugs in code (surprising counts), and to identify possible inline-expansion points (high call counts). Internal time statistics can be used to identify “hot loops” that should be carefully optimized. Cumulative time statistics should be used to identify high level errors in the selection of algorithms. Note that the unusual handling of cumulative times in this profiler allows statistics for recursive implementations of algorithms to be directly compared to iterative implementations.

## Reference Manual

*Python profiler*\
The primary entry point for the profiler is the global function `profile.run()`. It is typically used to create any profile information. The reports are formatted and printed using methods of the class `pstats.Stats`. The following is a description of all of these standard entry points and functions. For a more in-depth view of some of the code, consider reading the later section on Profiler Extensions, which includes discussion of how to derive “better” profilers from the classes presented, or reading the source code for these modules.

<div class="funcdesc">

runstring

This function takes a single argument that has can be passed to the statement, and an optional file name. In all cases this routine attempts to its first argument, and gather profiling statistics from the execution. If no file name is present, then this function automatically prints a simple profiling report, sorted by the standard name string (file/line/function-name) that is presented in each line. The following is a typical output from such a call:

          main()
          2706 function calls (2004 primitive calls) in 4.504 CPU seconds

    Ordered by: standard name

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
         2    0.006    0.003    0.953    0.477 pobject.py:75(save_objects)
      43/3    0.533    0.012    0.749    0.250 pobject.py:99(evaluate)
     ...

The first line indicates that this profile was generated by the call:\
`profile.run(’main()’)`, and hence the exec’ed string is `’main()’`. The second line indicates that 2706 calls were monitored. Of those calls, 2004 were *primitive*. We define *primitive* to mean that the call was not induced via recursion. The next line: `Ordered by: standard name`, indicates that the text string in the far right column was used to sort the output. The column headings include:

ncalls  
for the number of calls,

tottime  
for the total time spent in the given function (and excluding time made in calls to sub-functions),

percall  
is the quotient of `tottime` divided by `ncalls`

cumtime  
is the total time spent in this and all subfunctions (i.e., from invocation till exit). This figure is accurate *even* for recursive functions.

percall  
is the quotient of `cumtime` divided by primitive calls

filename:lineno(function)  
provides the respective data of each function

When there are two numbers in the first column (e.g.: `43/3`), then the latter is the number of primitive calls, and the former is the actual number of calls. Note that when the function does not recurse, these two values are the same, and only the single figure is printed.

</div>

Analysis of the profiler data is done using this class from the `pstats` module:

<div class="classdesc">

Statsfilename This class constructor creates an instance of a “statistics object” from a *filename* (or set of filenames). `Stats` objects are manipulated by methods, in order to print useful reports.

The file selected by the above constructor must have been created by the corresponding version of `profile`. To be specific, there is *no* file compatibility guaranteed with future versions of this profiler, and there is no compatibility with files produced by other profilers (e.g., the old system profiler).

If several files are provided, all the statistics for identical functions will be coalesced, so that an overall view of several processes can be considered in a single report. If additional files need to be combined with data in an existing `Stats` object, the `add()` method can be used.

</div>

### The `Stats` Class <span id="profile-stats" label="profile-stats"></span>

`Stats` objects have the following methods:

<div class="methoddesc">

strip_dirs This method for the `Stats` class removes all leading path information from file names. It is very useful in reducing the size of the printout to fit within (close to) 80 columns. This method modifies the object, and the stripped information is lost. After performing a strip operation, the object is considered to have its entries in a “random” order, as it was just after object initialization and loading. If `strip_dirs()` causes two function names to be indistinguishable (i.e., they are on the same line of the same filename, and have the same function name), then the statistics for these two entries are accumulated into a single entry.

</div>

<div class="methoddesc">

addfilename This method of the `Stats` class accumulates additional profiling information into the current profiling object. Its arguments should refer to filenames created by the corresponding version of `profile.run()`. Statistics for identically named (re: file, line, name) functions are automatically accumulated into single function statistics.

</div>

<div class="methoddesc">

sort_statskey This method modifies the `Stats` object by sorting it according to the supplied criteria. The argument is typically a string identifying the basis of a sort (example: `’time’` or `’name’`).

When more than one key is provided, then additional keys are used as secondary criteria when the there is equality in all keys selected before them. For example, `sort_stats(’name’, ’file’)` will sort all the entries according to their function name, and resolve all ties (identical function names) by sorting by file name.

Abbreviations can be used for any key names, as long as the abbreviation is unambiguous. The following are the keys currently defined:

|                          |                      |
|:-------------------------|:---------------------|
| Valid ArgMeaning ’calls’ | call count           |
| ’cumulative’             | cumulative time      |
| ’file’                   | file name            |
| ’module’                 | file name            |
| ’pcalls’                 | primitive call count |
| ’line’                   | line number          |
| ’name’                   | function name        |
| ’nfl’                    | name/file/line       |
| ’stdname’                | standard name        |
| ’time’                   | internal time        |
|                          |                      |

Note that all sorts on statistics are in descending order (placing most time consuming items first), where as name, file, and line number searches are in ascending order (i.e., alphabetical). The subtle distinction between `’nfl’` and `’stdname’` is that the standard name is a sort of the name as printed, which means that the embedded line numbers get compared in an odd way. For example, lines 3, 20, and 40 would (if the file names were the same) appear in the string order 20, 3 and 40. In contrast, `’nfl’` does a numeric compare of the line numbers. In fact, `sort_stats(’nfl’)` is the same as `sort_stats(’name’, ’file’, ’line’)`.

For compatibility with the old profiler, the numeric arguments `-1`, `0`, `1`, and `2` are permitted. They are interpreted as `’stdname’`, `’calls’`, `’time’`, and `’cumulative’` respectively. If this old style format (numeric) is used, only one sort key (the numeric key) will be used, and additional arguments will be silently ignored.

</div>

<div class="methoddesc">

reverse_order This method for the `Stats` class reverses the ordering of the basic list within the object. This method is provided primarily for compatibility with the old profiler. Its utility is questionable now that ascending vs descending order is properly selected based on the sort key of choice.

</div>

<div class="methoddesc">

print_statsrestriction This method for the `Stats` class prints out a report as described in the `profile.run()` definition.

The order of the printing is based on the last `sort_stats()` operation done on the object (subject to caveats in `add()` and `strip_dirs()`.

The arguments provided (if any) can be used to limit the list down to the significant entries. Initially, the list is taken to be the complete set of profiled functions. Each restriction is either an integer (to select a count of lines), or a decimal fraction between 0.0 and 1.0 inclusive (to select a percentage of lines), or a regular expression (to pattern match the standard name that is printed; as of Python 1.5b1, this uses the Perl-style regular expression syntax defined by the `re` module). If several restrictions are provided, then they are applied sequentially. For example:

    print_stats(.1, 'foo:')

would first limit the printing to first 10% of list, and then only print functions that were part of filename `.*foo:`. In contrast, the command:

    print_stats('foo:', .1)

would limit the list to all functions having file names `.*foo:`, and then proceed to only print the first 10% of them.

</div>

<div class="methoddesc">

print_callersrestrictions This method for the `Stats` class prints a list of all functions that called each function in the profiled database. The ordering is identical to that provided by `print_stats()`, and the definition of the restricting argument is also identical. For convenience, a number is shown in parentheses after each caller to show how many times this specific call was made. A second non-parenthesized number is the cumulative time spent in the function at the right.

</div>

<div class="methoddesc">

print_calleesrestrictions This method for the `Stats` class prints a list of all function that were called by the indicated function. Aside from this reversal of direction of calls (re: called vs was called by), the arguments and ordering are identical to the `print_callers()` method.

</div>

<div class="methoddesc">

ignore *Deprecated since version 1.5.1: This is not needed in modern versions of Python.[^2]*

</div>

## Limitations <span id="profile-limits" label="profile-limits"></span>

There are two fundamental limitations on this profiler. The first is that it relies on the Python interpreter to dispatch *call*, *return*, and *exception* events. Compiled C code does not get interpreted, and hence is “invisible” to the profiler. All time spent in C code (including built-in functions) will be charged to the Python function that invoked the C code. If the C code calls out to some native Python code, then those calls will be profiled properly.

The second limitation has to do with accuracy of timing information. There is a fundamental problem with deterministic profilers involving accuracy. The most obvious restriction is that the underlying “clock” is only ticking at a rate (typically) of about .001 seconds. Hence no measurements will be more accurate that that underlying clock. If enough measurements are taken, then the “error” will tend to average out. Unfortunately, removing this first error induces a second source of error...

The second problem is that it “takes a while” from when an event is dispatched until the profiler’s call to get the time actually *gets* the state of the clock. Similarly, there is a certain lag when exiting the profiler event handler from the time that the clock’s value was obtained (and then squirreled away), until the user’s code is once again executing. As a result, functions that are called many times, or call many functions, will typically accumulate this error. The error that accumulates in this fashion is typically less than the accuracy of the clock (i.e., less than one clock tick), but it *can* accumulate and become very significant. This profiler provides a means of calibrating itself for a given platform so that this error can be probabilistically (i.e., on the average) removed. After the profiler is calibrated, it will be more accurate (in a least square sense), but it will sometimes produce negative numbers (when call counts are exceptionally low, and the gods of probability work against you :-). ) Do *not* be alarmed by negative numbers in the profile. They should *only* appear if you have calibrated your profiler, and the results are actually better than without calibration.

## Calibration <span id="profile-calibration" label="profile-calibration"></span>

The profiler class has a hard coded constant that is added to each event handling time to compensate for the overhead of calling the time function, and socking away the results. The following procedure can be used to obtain this constant for a given platform (see discussion in section Limitations above).

    import profile
    pr = profile.Profile()
    print pr.calibrate(100)
    print pr.calibrate(100)
    print pr.calibrate(100)

The argument to `calibrate()` is the number of times to try to do the sample calls to get the CPU times. If your computer is *very* fast, you might have to do:

    pr.calibrate(1000)

or even:

    pr.calibrate(10000)

The object of this exercise is to get a fairly consistent result. When you have a consistent answer, you are ready to use that number in the source code. For a Sun Sparcstation 1000 running Solaris 2.3, the magical number is about .00053. If you have a choice, you are better off with a smaller constant, and your results will “less often” show up as negative in profile statistics.

The following shows how the trace_dispatch() method in the Profile class should be modified to install the calibration constant on a Sun Sparcstation 1000:

    def trace_dispatch(self, frame, event, arg):
        t = self.timer()
        t = t[0] + t[1] - self.t - .00053 # Calibration constant

        if self.dispatch[event](frame,t):
            t = self.timer()
            self.t = t[0] + t[1]
        else:
            r = self.timer()
            self.t = r[0] + r[1] - t # put back unrecorded delta
        return

Note that if there is no calibration constant, then the line containing the callibration constant should simply say:

    t = t[0] + t[1] - self.t  # no calibration constant

You can also achieve the same results using a derived class (and the profiler will actually run equally fast!!), but the above method is the simplest to use. I could have made the profiler “self calibrating”, but it would have made the initialization of the profiler class slower, and would have required some *very* fancy coding, or else the use of a variable where the constant `.00053` was placed in the code shown. This is a **VERY** critical performance section, and there is no reason to use a variable lookup at this point, when a constant can be used.

## Extensions — Deriving Better Profilers

The `Profile` class of module `profile` was written so that derived classes could be developed to extend the profiler. Rather than describing all the details of such an effort, I’ll just present the following two examples of derived classes that can be used to do profiling. If the reader is an avid Python programmer, then it should be possible to use these as a model and create similar (and perchance better) profile classes.

If all you want to do is change how the timer is called, or which timer function is used, then the basic class has an option for that in the constructor for the class. Consider passing the name of a function to call into the constructor:

    pr = profile.Profile(your_time_func)

The resulting profiler will call `your_time_func()` instead of `os.times()`. The function should return either a single number or a list of numbers (like what `os.times()` returns). If the function returns a single time number, or the list of returned numbers has length 2, then you will get an especially fast version of the dispatch routine.

Be warned that you *should* calibrate the profiler class for the timer function that you choose. For most machines, a timer that returns a lone integer value will provide the best results in terms of low overhead during profiling. (`os.times()` is *pretty* bad, ’cause it returns a tuple of floating point values, so all arithmetic is floating point in the profiler!). If you want to substitute a better timer in the cleanest fashion, you should derive a class, and simply put in the replacement dispatch method that better handles your timer call, along with the appropriate calibration constant :-).

### OldProfile Class <span id="profile-old" label="profile-old"></span>

The following derived profiler simulates the old style profiler, providing errant results on recursive functions. The reason for the usefulness of this profiler is that it runs faster (i.e., less overhead) than the old profiler. It still creates all the caller stats, and is quite useful when there is *no* recursion in the user’s code. It is also a lot more accurate than the old profiler, as it does not charge all its overhead time to the user’s code.

    class OldProfile(Profile):

        def trace_dispatch_exception(self, frame, t):
            rt, rtt, rct, rfn, rframe, rcur = self.cur
            if rcur and not rframe is frame:
                return self.trace_dispatch_return(rframe, t)
            return 0

        def trace_dispatch_call(self, frame, t):
            fn = `frame.f_code`
            
            self.cur = (t, 0, 0, fn, frame, self.cur)
            if self.timings.has_key(fn):
                tt, ct, callers = self.timings[fn]
                self.timings[fn] = tt, ct, callers
            else:
                self.timings[fn] = 0, 0, {}
            return 1

        def trace_dispatch_return(self, frame, t):
            rt, rtt, rct, rfn, frame, rcur = self.cur
            rtt = rtt + t
            sft = rtt + rct

            pt, ptt, pct, pfn, pframe, pcur = rcur
            self.cur = pt, ptt+rt, pct+sft, pfn, pframe, pcur

            tt, ct, callers = self.timings[rfn]
            if callers.has_key(pfn):
                callers[pfn] = callers[pfn] + 1
            else:
                callers[pfn] = 1
            self.timings[rfn] = tt+rtt, ct + sft, callers

            return 1


        def snapshot_stats(self):
            self.stats = {}
            for func in self.timings.keys():
                tt, ct, callers = self.timings[func]
                nor_func = self.func_normalize(func)
                nor_callers = {}
                nc = 0
                for func_caller in callers.keys():
                    nor_callers[self.func_normalize(func_caller)] = \
                        callers[func_caller]
                    nc = nc + callers[func_caller]
                self.stats[nor_func] = nc, nc, tt, ct, nor_callers

### HotProfile Class <span id="profile-HotProfile" label="profile-HotProfile"></span>

This profiler is the fastest derived profile example. It does not calculate caller-callee relationships, and does not calculate cumulative time under a function. It only calculates time spent in a function, so it runs very quickly (re: very low overhead). In truth, the basic profiler is so fast, that is probably not worth the savings to give up the data, but this class still provides a nice example.

    class HotProfile(Profile):

        def trace_dispatch_exception(self, frame, t):
            rt, rtt, rfn, rframe, rcur = self.cur
            if rcur and not rframe is frame:
                return self.trace_dispatch_return(rframe, t)
            return 0

        def trace_dispatch_call(self, frame, t):
            self.cur = (t, 0, frame, self.cur)
            return 1

        def trace_dispatch_return(self, frame, t):
            rt, rtt, frame, rcur = self.cur

            rfn = `frame.f_code`

            pt, ptt, pframe, pcur = rcur
            self.cur = pt, ptt+rt, pframe, pcur

            if self.timings.has_key(rfn):
                nc, tt = self.timings[rfn]
                self.timings[rfn] = nc + 1, rt + rtt + tt
            else:
                self.timings[rfn] =      1, rt + rtt

            return 1


        def snapshot_stats(self):
            self.stats = {}
            for func in self.timings.keys():
                nc, tt = self.timings[func]
                nor_func = self.func_normalize(func)
                self.stats[nor_func] = nc, nc, tt, 0, {}

[^1]: Updated and converted to LaTeX by Guido van Rossum. The references to the old profiler are left in the text, although it no longer exists.

[^2]: This was once necessary, when Python would print any unused expression result that was not `None`. The method is still defined for backward compatibility.
# `pty` — Pseudo-terminal utilities

*Pseudo-Terminal Handling for SGI and Linux.*\
The `pty` module defines operations for handling the pseudo-terminal concept: starting another process and being able to write to and read from its controlling terminal programmatically.

Because pseudo-terminal handling is highly platform dependant, there is code to do it only for SGI and Linux. (The Linux code is supposed to work on other platforms, but hasn’t been tested yet.)

The `pty` module defines the following functions:

<div class="funcdesc">

fork Fork. Connect the child’s controlling terminal to a pseudo-terminal. Return value is `(`*`pid`*`, `*`fd`*`)`. Note that the child gets *pid* 0, and the *fd* is *invalid*. The parent’s return value is the *pid* of the child, and *fd* is a file descriptor connected to the child’s controlling terminal (and also to the child’s standard input and output.

</div>

<div class="funcdesc">

openpty Open a new pseudo-terminal pair, using `os.openpty()` if possible, or emulation code for SGI and generic Unix systems. Return a pair of file descriptors `(`*`master`*`, `*`slave`*`)`, for the master and the slave end, respectively.

</div>

<div class="funcdesc">

spawnargv Spawn a process, and connect its controlling terminal with the current process’s standard io. This is often used to baffle programs which insist on reading from the controlling terminal.

The functions *master_read* and *stdin_read* should be functions which read from a file-descriptor. The defaults try to read 1024 bytes each time they are called.

</div>
# `pyclbr` — Python class browser support

*Supports information extraction for a Python class browser.*\
The `pyclbr` can be used to determine some limited information about the classes and methods defined in a module. The information provided is sufficient to implement a traditional three-pane class browser. The information is extracted from the source code rather than from an imported module, so this module is safe to use with untrusted source code. This restriction makes it impossible to use this module with modules not implemented in Python, including many standard and optional extension modules.

<div class="funcdesc">

readmodulemodule

Read a module and return a dictionary mapping class names to class descriptor objects. The parameter *module* should be the name of a module as a string; it may be the name of a module within a package. The *path* parameter should be a sequence, and is used to augment the value of `sys.path`, which is used to locate module source code.

</div>

## Class Descriptor Objects <span id="pyclbr-class-objects" label="pyclbr-class-objects"></span>

The class descriptor objects used as values in the dictionary returned by `readmodule()` provide the following data members:

<div class="memberdesc">

module The name of the module defining the class described by the class descriptor.

</div>

<div class="memberdesc">

name The name of the class.

</div>

<div class="memberdesc">

super A list of class descriptors which describe the immediate base classes of the class being described. Classes which are named as superclasses but which are not discoverable by `readmodule()` are listed as a string with the class name instead of class descriptors.

</div>

<div class="memberdesc">

methods A dictionary mapping method names to line numbers.

</div>

<div class="memberdesc">

file Name of the file containing the class statement defining the class.

</div>

<div class="memberdesc">

lineno The line number of the class statement within the file named by `file`.

</div>
# `xml.parsers.expat` — Fast XML parsing using the Expat library

*An interface to the Expat non-validating XML parser.*\
*New in version 2.0.*

The `xml.parsers.expat` module is a Python interface to the Expat non-validating XML parser. The module provides a single extension type, `xmlparser`, that represents the current state of an XML parser. After an `xmlparser` object has been created, various attributes of the object can be set to handler functions. When an XML document is then fed to the parser, the handler functions are called for the character data and markup in the XML document.

This module uses the `pyexpat`module to provide access to the Expat parser. Direct use of the `pyexpat` module is deprecated.

The `xml.parsers.expat` module contains two functions:

<div class="funcdesc">

ErrorStringerrno Returns an explanatory string for a given error number *errno*.

</div>

<div class="funcdesc">

ParserCreate Creates and returns a new `xmlparser` object. *encoding*, if specified, must be a string naming the encoding used by the XML data. Expat doesn’t support as many encodings as Python does, and its repertoire of encodings can’t be extended; it supports UTF-8, UTF-16, ISO-8859-1 (Latin1), and ASCII.

Expat can optionally do XML namespace processing for you, enabled by providing a value for *namespace_separator*. When namespace processing is enabled, element type names and attribute names that belong to a namespace will be expanded. The element name passed to the element handlers `StartElementHandler()` and `EndElementHandler()` will be the concatenation of the namespace URI, the namespace separator character, and the local part of the name. If the namespace separator is a zero byte (`chr(0)`) then the namespace URI and the local part will be concatenated without any separator.

For example, if *namespace_separator* is set to ` `, and the following document is parsed:

    <?xml version="1.0"?>
    <root xmlns    = "http://default-namespace.org/"
          xmlns:py = "http://www.python.org/ns/">
      <py:elem1 />
      <elem2 xmlns="" />
    </root>

`StartElementHandler()` will receive the following strings for each element:

    http://default-namespace.org/ root
    http://www.python.org/ns/ elem1
    elem2

</div>

`xmlparser` objects have the following methods:

<div class="methoddesc">

Parsedata Parses the contents of the string *data*, calling the appropriate handler functions to process the parsed data. *isfinal* must be true on the final call to this method. *data* can be the empty string at any time.

</div>

<div class="methoddesc">

ParseFilefile Parse XML data reading from the object *file*. *file* only needs to provide the `read(`*`nbytes`*`)` method, returning the empty string when there’s no more data.

</div>

<div class="methoddesc">

SetBasebase Sets the base to be used for resolving relative URIs in system identifiers in declarations. Resolving relative identifiers is left to the application: this value will be passed through as the base argument to the `ExternalEntityRefHandler`, `NotationDeclHandler`, and `UnparsedEntityDeclHandler` functions.

</div>

<div class="methoddesc">

GetBase Returns a string containing the base set by a previous call to `SetBase()`, or `None` if `SetBase()` hasn’t been called.

</div>

`xmlparser` objects have the following attributes:

<div class="datadesc">

returns_unicode If this attribute is set to 1, the handler functions will be passed Unicode strings. If `returns_unicode` is 0, 8-bit strings containing UTF-8 encoded data will be passed to the handlers.

</div>

The following attributes contain values relating to the most recent error encountered by an `xmlparser` object, and will only have correct values once a call to `Parse()` or `ParseFile()` has raised a `xml.parsers.expat.error` exception.

<div class="datadesc">

ErrorByteIndex Byte index at which an error occurred.

</div>

<div class="datadesc">

ErrorCode Numeric code specifying the problem. This value can be passed to the `ErrorString()` function, or compared to one of the constants defined in the `errors` object.

</div>

<div class="datadesc">

ErrorColumnNumber Column number at which an error occurred.

</div>

<div class="datadesc">

ErrorLineNumber Line number at which an error occurred.

</div>

Here is the list of handlers that can be set. To set a handler on an `xmlparser` object *o*, use *`o`*`.`*`handlername`*` = `*`func`*. *handlername* must be taken from the following list, and *func* must be a callable object accepting the correct number of arguments. The arguments are all strings, unless otherwise stated.

<div class="methoddesc">

StartElementHandlername, attributes Called for the start of every element. *name* is a string containing the element name, and *attributes* is a dictionary mapping attribute names to their values.

</div>

<div class="methoddesc">

EndElementHandlername Called for the end of every element.

</div>

<div class="methoddesc">

ProcessingInstructionHandlertarget, data Called for every processing instruction.

</div>

<div class="methoddesc">

CharacterDataHandler*data* Called for character data.

</div>

<div class="methoddesc">

UnparsedEntityDeclHandlerentityName, base, systemId, publicId, notationName Called for unparsed (NDATA) entity declarations.

</div>

<div class="methoddesc">

NotationDeclHandlernotationName, base, systemId, publicId Called for notation declarations.

</div>

<div class="methoddesc">

StartNamespaceDeclHandlerprefix, uri Called when an element contains a namespace declaration.

</div>

<div class="methoddesc">

EndNamespaceDeclHandlerprefix Called when the closing tag is reached for an element that contained a namespace declaration.

</div>

<div class="methoddesc">

CommentHandlerdata Called for comments.

</div>

<div class="methoddesc">

StartCdataSectionHandler Called at the start of a CDATA section.

</div>

<div class="methoddesc">

EndCdataSectionHandler Called at the end of a CDATA section.

</div>

<div class="methoddesc">

DefaultHandlerdata Called for any characters in the XML document for which no applicable handler has been specified. This means characters that are part of a construct which could be reported, but for which no handler has been supplied.

</div>

<div class="methoddesc">

DefaultHandlerExpanddata This is the same as the `DefaultHandler`, but doesn’t inhibit expansion of internal entities. The entity reference will not be passed to the default handler.

</div>

<div class="methoddesc">

NotStandaloneHandler Called if the XML document hasn’t been declared as being a standalone document.

</div>

<div class="methoddesc">

ExternalEntityRefHandlercontext, base, systemId, publicId Called for references to external entities.

</div>

## Example <span id="expat-example" label="expat-example"></span>

The following program defines three handlers that just print out their arguments.

    import xml.parsers.expat

    # 3 handler functions
    def start_element(name, attrs):
        print 'Start element:', name, attrs
    def end_element(name):
        print 'End element:', name
    def char_data(data):
        print 'Character data:', repr(data)

    p = xml.parsers.expat.ParserCreate()

    p.StartElementHandler = start_element
    p.EndElementHandler = end_element
    p.CharacterDataHandler = char_data

    p.Parse("""<?xml version="1.0"?>
    <parent id="top"><child1 name="paul">Text goes here</child1>
    <child2 name="fred">More text</child2>
    </parent>""")

The output from this program is:

    Start element: parent {'id': 'top'}
    Start element: child1 {'name': 'paul'}
    Character data: 'Text goes here'
    End element: child1
    Character data: '\012'
    Start element: child2 {'name': 'fred'}
    Character data: 'More text'
    End element: child2
    Character data: '\012'
    End element: parent

## Expat error constants <span id="expat-errors" label="expat-errors"></span>

The following table lists the error constants in the `errors` object of the `xml.parsers.expat` module. These constants are useful in interpreting some of the attributes of the parser object after an error has occurred.

The `errors` object has the following attributes:

<div class="datadesc">

XML_ERROR_ASYNC_ENTITY

</div>

<div class="datadesc">

XML_ERROR_ATTRIBUTE_EXTERNAL_ENTITY_REF

</div>

<div class="datadesc">

XML_ERROR_BAD_CHAR_REF

</div>

<div class="datadesc">

XML_ERROR_BINARY_ENTITY_REF

</div>

<div class="datadesc">

XML_ERROR_DUPLICATE_ATTRIBUTE An attribute was used more than once in a start tag.

</div>

<div class="datadesc">

XML_ERROR_INCORRECT_ENCODING

</div>

<div class="datadesc">

XML_ERROR_INVALID_TOKEN

</div>

<div class="datadesc">

XML_ERROR_JUNK_AFTER_DOC_ELEMENT Something other than whitespace occurred after the document element.

</div>

<div class="datadesc">

XML_ERROR_MISPLACED_XML_PI

</div>

<div class="datadesc">

XML_ERROR_NO_ELEMENTS

</div>

<div class="datadesc">

XML_ERROR_NO_MEMORY Expat was not able to allocate memory internally.

</div>

<div class="datadesc">

XML_ERROR_PARAM_ENTITY_REF

</div>

<div class="datadesc">

XML_ERROR_PARTIAL_CHAR

</div>

<div class="datadesc">

XML_ERROR_RECURSIVE_ENTITY_REF

</div>

<div class="datadesc">

XML_ERROR_SYNTAX Some unspecified syntax error was encountered.

</div>

<div class="datadesc">

XML_ERROR_TAG_MISMATCH An end tag did not match the innermost open start tag.

</div>

<div class="datadesc">

XML_ERROR_UNCLOSED_TOKEN

</div>

<div class="datadesc">

XML_ERROR_UNDEFINED_ENTITY A reference was made to a entity which was not defined.

</div>

<div class="datadesc">

XML_ERROR_UNKNOWN_ENCODING The document encoding is not supported by Expat.

</div>
# Python Runtime Services <span id="python" label="python"></span>

The modules described in this chapter provide a wide range of services related to the Python interpreter and its interaction with its environment. Here’s an overview:
# `Queue` — A synchronized queue class.

*A synchronized queue class.*\
The `Queue` module implements a multi-producer, multi-consumer FIFO queue. It is especially useful in threads programming when information must be exchanged safely between multiple threads. The `Queue` class in this module implements all the required locking semantics. It depends on the availability of thread support in Python.

The `Queue` module defines the following class and exception:

<div class="classdesc">

Queuemaxsize Constructor for the class. *maxsize* is an integer that sets the upperbound limit on the number of items that can be placed in the queue. Insertion will block once this size has been reached, until queue items are consumed. If *maxsize* is less than or equal to zero, the queue size is infinite.

</div>

<div class="excdesc">

Empty Exception raised when non-blocking `get()` (or `get_nowait()`) is called on a `Queue` object which is empty or locked.

</div>

<div class="excdesc">

Full Exception raised when non-blocking `put()` (or `put_nowait()`) is called on a `Queue` object which is full or locked.

</div>

## Queue Objects

Class `Queue` implements queue objects and has the methods described below. This class can be derived from in order to implement other queue organizations (e.g. stack) but the inheritable interface is not described here. See the source code for details. The public methods are:

<div class="methoddesc">

qsize Return the approximate size of the queue. Because of multithreading semantics, this number is not reliable.

</div>

<div class="methoddesc">

empty Return `1` if the queue is empty, `0` otherwise. Because of multithreading semantics, this is not reliable.

</div>

<div class="methoddesc">

full Return `1` if the queue is full, `0` otherwise. Because of multithreading semantics, this is not reliable.

</div>

<div class="methoddesc">

putitem Put *item* into the queue. If optional argument *block* is 1 (the default), block if necessary until a free slot is available. Otherwise (*block* is 0), put *item* on the queue if a free slot is immediately available, else raise the `Full` exception.

</div>

<div class="methoddesc">

put_nowaititem Equivalent to `put(`*`item`*`, 0)`.

</div>

<div class="methoddesc">

get Remove and return an item from the queue. If optional argument *block* is 1 (the default), block if necessary until an item is available. Otherwise (*block* is 0), return an item if one is immediately available, else raise the `Empty` exception.

</div>

<div class="methoddesc">

get_nowait Equivalent to `get(0)`.

</div>
# `regex` — Regular expression operations

*Regular expression search and match operations. **Obsolete!***\
This module provides regular expression matching operations similar to those found in Emacs.

**Obsolescence note:** This module is obsolete as of Python version 1.5; it is still being maintained because much existing code still uses it. All new code in need of regular expressions should use the new `re`module, which supports the more powerful and regular Perl-style regular expressions. Existing code should be converted. The standard library module `reconvert`helps in converting `regex` style regular expressions to `re`style regular expressions. (For more conversion help, see Andrew Kuchling’s“`regex-to-re` HOWTO” at `http://www.python.org/doc/howto/regex-to-re/`.)

By default the patterns are Emacs-style regular expressions (with one exception). There is a way to change the syntax to match that of several well-known Unix utilities. The exception is that Emacs’ `s` pattern is not supported, since the original implementation references the Emacs syntax tables.

This module is 8-bit clean: both patterns and strings may contain null bytes and characters whose high bit is set.

**Please note:** There is a little-known fact about Python string literals which means that you don’t usually have to worry about doubling backslashes, even though they are used to escape special characters in string literals as well as in regular expressions. This is because Python doesn’t remove backslashes from string literals if they are followed by an unrecognized escape character. *However*, if you want to include a literal *backslash* in a regular expression represented as a string literal, you have to *quadruple* it or enclose it in a singleton character class. E.g. to extract LaTeX `section{`<span class="roman">`…`</span>`}` headers from a document, you can use this pattern: `’[]section{(.*)}’`. *Another exception:* the escape sequece `b` is significant in string literals (where it means the ASCII bell character) as well as in Emacs regular expressions (where it stands for a word boundary), so in order to search for a word boundary, you should use the pattern `’b’`. Similarly, a backslash followed by a digit 0-7 should be doubled to avoid interpretation as an octal escape.

## Regular Expressions

A regular expression (or RE) specifies a set of strings that matches it; the functions in this module let you check if a particular string matches a given regular expression (or if a given regular expression matches a particular string, which comes down to the same thing).

Regular expressions can be concatenated to form new regular expressions; if *A* and *B* are both regular expressions, then *AB* is also an regular expression. If a string *p* matches A and another string *q* matches B, the string *pq* will match AB. Thus, complex expressions can easily be constructed from simpler ones like the primitives described here. For details of the theory and implementation of regular expressions, consult almost any textbook about compiler construction.

A brief explanation of the format of regular expressions follows.

Regular expressions can contain both special and ordinary characters. Ordinary characters, like ’`A`’, ’`a`’, or ’`0`’, are the simplest regular expressions; they simply match themselves. You can concatenate ordinary characters, so ’`last`’ matches the characters ’last’. (In the rest of this section, we’ll write RE’s in `this special font`, usually without quotes, and strings to be matched ’in single quotes’.)

Special characters either stand for classes of ordinary characters, or affect how the regular expressions around them are interpreted.

The special characters are:

- (Dot.) Matches any character except a newline.

- (Caret.) Matches the start of the string.

- Matches the end of the string. `foo` matches both ’foo’ and ’foobar’, while the regular expression ’`foo$`’ matches only ’foo’.

- Causes the resulting RE to match 0 or more repetitions of the preceding RE. `ab*` will match ’a’, ’ab’, or ’a’ followed by any number of ’b’s.

- Causes the resulting RE to match 1 or more repetitions of the preceding RE. `ab+` will match ’a’ followed by any non-zero number of ’b’s; it will not match just ’a’.

- Causes the resulting RE to match 0 or 1 repetitions of the preceding RE. `ab?` will match either ’a’ or ’ab’.

- Either escapes special characters (permitting you to match characters like ’\*?+&\$’), or signals a special sequence; special sequences are discussed below. Remember that Python also uses the backslash as an escape sequence in string literals; if the escape sequence isn’t recognized by Python’s parser, the backslash and subsequent character are included in the resulting string. However, if Python would recognize the resulting sequence, the backslash should be repeated twice.

- Used to indicate a set of characters. Characters can be listed individually, or a range is indicated by giving two characters and separating them by a ’-’. Special characters are not active inside sets. For example, `[akm$]` will match any of the characters ’a’, ’k’, ’m’, or ’\$’; `[a-z]` will match any lowercase letter.

  If you want to include a `]` inside a set, it must be the first character of the set; to include a `-`, place it as the first or last character.

  Characters *not* within a range can be matched by including a `^` as the first character of the set; `^` elsewhere will simply match the ’`^`’ character.

The special sequences consist of ’’ and a character from the list below. If the ordinary character is not on the list, then the resulting RE will match the second character. For example, `$` matches the character ’\$’. Ones where the backslash should be doubled in string literals are indicated.

- `A|B`, where A and B can be arbitrary REs, creates a regular expression that will match either A or B. This can be used inside groups (see below) as well.

- Indicates the start and end of a group; the contents of a group can be matched later in the string with the special sequence, described next.

<div class="fulllineitems">

Matches the contents of the group of the same number. For example, `(.+) ` matches ’the the’ or ’55 55’, but not ’the end’ (note the space after the group). This special sequence can only be used to match one of the first 9 groups; groups with higher numbers can be matched using the `v` sequence. ( and don’t need a double backslash because they are not octal digits.)

</div>

- Matches the empty string, but only at the beginning or end of a word. A word is defined as a sequence of alphanumeric characters, so the end of a word is indicated by whitespace or a non-alphanumeric character.

- Matches the empty string, but when it is *not* at the beginning or end of a word.

- Must be followed by a two digit decimal number, and matches the contents of the group of the same number. The group number must be between 1 and 99, inclusive.

- Matches any alphanumeric character; this is equivalent to the set `[a-zA-Z0-9]`.

- Matches any non-alphanumeric character; this is equivalent to the set `[â-zA-Z0-9]`.

- Matches the empty string, but only at the beginning of a word. A word is defined as a sequence of alphanumeric characters, so the end of a word is indicated by whitespace or a non-alphanumeric character.

- Matches the empty string, but only at the end of a word.

- Matches a literal backslash.

- Like `^`, this only matches at the start of the string.

- Like `$`, this only matches at the end of the string.

## Module Contents

The module defines these functions, and an exception:

<div class="funcdesc">

matchpattern, string Return how many characters at the beginning of *string* match the regular expression *pattern*. Return `-1` if the string does not match the pattern (this is different from a zero-length match!).

</div>

<div class="funcdesc">

searchpattern, string Return the first position in *string* that matches the regular expression *pattern*. Return `-1` if no position in the string matches the pattern (this is different from a zero-length match anywhere!).

</div>

<div class="funcdesc">

compilepattern Compile a regular expression pattern into a regular expression object, which can be used for matching using its `match()` and `search()` methods, described below. The optional argument *translate*, if present, must be a 256-character string indicating how characters (both of the pattern and of the strings to be matched) are translated before comparing them; the *i*-th element of the string gives the translation for the character with code *i*. This can be used to implement case-insensitive matching; see the `casefold` data item below.

The sequence

    prog = regex.compile(pat)
    result = prog.match(str)

is equivalent to

    result = regex.match(pat, str)

but the version using `compile()` is more efficient when multiple regular expressions are used concurrently in a single program. (The compiled version of the last pattern passed to `regex.match()` or `regex.search()` is cached, so programs that use only a single regular expression at a time needn’t worry about compiling regular expressions.)

</div>

<div class="funcdesc">

set_syntaxflags Set the syntax to be used by future calls to `compile()`, `match()` and `search()`. (Already compiled expression objects are not affected.) The argument is an integer which is the OR of several flag bits. The return value is the previous value of the syntax flags. Names for the flags are defined in the standard module `regex_syntax`; read the file `regex_syntax.py` for more information.

</div>

<div class="funcdesc">

get_syntax Returns the current value of the syntax flags as an integer.

</div>

<div class="funcdesc">

symcomppattern This is like `compile()`, but supports symbolic group names: if a parenthesis-enclosed group begins with a group name in angular brackets, e.g. `’(<id>[a-z][a-z0-9]*)’`, the group can be referenced by its name in arguments to the `group()` method of the resulting compiled regular expression object, like this: `p.group(’id’)`. Group names may contain alphanumeric characters and `’_’` only.

</div>

<div class="excdesc">

error Exception raised when a string passed to one of the functions here is not a valid regular expression (e.g., unmatched parentheses) or when some other error occurs during compilation or matching. (It is never an error if a string contains no match for a pattern.)

</div>

<div class="datadesc">

casefold A string suitable to pass as the *translate* argument to `compile()` to map all upper case characters to their lowercase equivalents.

</div>

Compiled regular expression objects support these methods:

<div class="funcdesc">

matchstring Return how many characters at the beginning of *string* match the compiled regular expression. Return `-1` if the string does not match the pattern (this is different from a zero-length match!).

The optional second parameter, *pos*, gives an index in the string where the search is to start; it defaults to `0`. This is not completely equivalent to slicing the string; the `’'̂` pattern character matches at the real beginning of the string and at positions just after a newline, not necessarily at the index where the search is to start.

</div>

<div class="funcdesc">

searchstring Return the first position in *string* that matches the regular expression `pattern`. Return `-1` if no position in the string matches the pattern (this is different from a zero-length match anywhere!).

The optional second parameter has the same meaning as for the `match()` method.

</div>

<div class="funcdesc">

groupindex, index, ... This method is only valid when the last call to the `match()` or `search()` method found a match. It returns one or more groups of the match. If there is a single *index* argument, the result is a single string; if there are multiple arguments, the result is a tuple with one item per argument. If the *index* is zero, the corresponding return value is the entire matching string; if it is in the inclusive range \[1..99\], it is the string matching the the corresponding parenthesized group (using the default syntax, groups are parenthesized using `(` and `)`). If no such group exists, the corresponding result is `None`.

If the regular expression was compiled by `symcomp()` instead of `compile()`, the *index* arguments may also be strings identifying groups by their group name.

</div>

Compiled regular expressions support these data attributes:

<div class="datadesc">

regs When the last call to the `match()` or `search()` method found a match, this is a tuple of pairs of indexes corresponding to the beginning and end of all parenthesized groups in the pattern. Indices are relative to the string argument passed to `match()` or `search()`. The 0-th tuple gives the beginning and end or the whole pattern. When the last match or search failed, this is `None`.

</div>

<div class="datadesc">

last When the last call to the `match()` or `search()` method found a match, this is the string argument passed to that method. When the last match or search failed, this is `None`.

</div>

<div class="datadesc">

translate This is the value of the *translate* argument to `regex.compile()` that created this regular expression object. If the *translate* argument was omitted in the `regex.compile()` call, this is `None`.

</div>

<div class="datadesc">

givenpat The regular expression pattern as passed to `compile()` or `symcomp()`.

</div>

<div class="datadesc">

realpat The regular expression after stripping the group names for regular expressions compiled with `symcomp()`. Same as `givenpat` otherwise.

</div>

<div class="datadesc">

groupindex A dictionary giving the mapping from symbolic group names to numerical group indexes for regular expressions compiled with `symcomp()`. `None` otherwise.

</div>
# `regsub` — String operations using regular expressions

*Substitution and splitting operations that use regular expressions. **Obsolete!***\
This module defines a number of functions useful for working with regular expressions (see built-in module `regex`).

Warning: these functions are not thread-safe.

**Obsolescence note:** This module is obsolete as of Python version 1.5; it is still being maintained because much existing code still uses it. All new code in need of regular expressions should use the new `re` module, which supports the more powerful and regular Perl-style regular expressions. Existing code should be converted. The standard library module `reconvert` helps in converting `regex` style regular expressions to `re` style regular expressions. (For more conversion help, see Andrew Kuchling’s“regex-to-re HOWTO” at `http://www.python.org/doc/howto/regex-to-re/`.)

<div class="funcdesc">

subpat, repl, str Replace the first occurrence of pattern *pat* in string *str* by replacement *repl*. If the pattern isn’t found, the string is returned unchanged. The pattern may be a string or an already compiled pattern. The replacement may contain references *`digit`* to subpatterns and escaped backslashes.

</div>

<div class="funcdesc">

gsubpat, repl, str Replace all (non-overlapping) occurrences of pattern *pat* in string *str* by replacement *repl*. The same rules as for `sub()` apply. Empty matches for the pattern are replaced only when not adjacent to a previous match, so e.g. `gsub(’’, ’-’, ’abc’)` returns `’-a-b-c-’`.

</div>

<div class="funcdesc">

splitstr, pat Split the string *str* in fields separated by delimiters matching the pattern *pat*, and return a list containing the fields. Only non-empty matches for the pattern are considered, so e.g. `split(’a:b’, ’:*’)` returns `[’a’, ’b’]` and `split(’abc’, ’’)` returns `[’abc’]`. The *maxsplit* defaults to 0. If it is nonzero, only *maxsplit* number of splits occur, and the remainder of the string is returned as the final element of the list.

</div>

<div class="funcdesc">

splitxstr, pat Split the string *str* in fields separated by delimiters matching the pattern *pat*, and return a list containing the fields as well as the separators. For example, `splitx(’a:::b’, ’:*’)` returns `[’a’, ’:::’, ’b’]`. Otherwise, this function behaves the same as `split`.

</div>

<div class="funcdesc">

capwordss Capitalize words separated by optional pattern *pat*. The default pattern uses any characters except letters, digits and underscores as word delimiters. Capitalization is done by changing the first character of each word to upper case.

</div>

<div class="funcdesc">

clear_cache The regsub module maintains a cache of compiled regular expressions, keyed on the regular expression string and the syntax of the regex module at the time the expression was compiled. This function clears that cache.

</div>
# `repr` — Alternate `repr()` implementation.

*Alternate `repr()` implementation with size limits.*\
The `repr` module provides a means for producing object representations with limits on the size of the resulting strings. This is used in the Python debugger and may be useful in other contexts as well.

This module provides a class, an instance, and a function:

<div class="classdesc">

Repr Class which provides formatting services useful in implementing functions similar to the built-in `repr()`; size limits for different object types are added to avoid the generation of representations which are excessively long.

</div>

<div class="datadesc">

aRepr This is an instance of `Repr` which is used to provide the `repr()` function described below. Changing the attributes of this object will affect the size limits used by `repr()` and the Python debugger.

</div>

<div class="funcdesc">

reprobj This is the `repr()` method of `aRepr`. It returns a string similar to that returned by the built-in function of the same name, but with limits on most sizes.

</div>

## Repr Objects <span id="Repr-objects" label="Repr-objects"></span>

`Repr` instances provide several members which can be used to provide size limits for the representations of different object types, and methods which format specific object types.

<div class="memberdesc">

maxlevel Depth limit on the creation of recursive representations. The default is `6`.

</div>

<div class="memberdesc">

maxdict Limits on the number of entries represented for the named object type. The default for `maxdict` is `4`, for the others, `6`.

</div>

<div class="memberdesc">

maxlong Maximum number of characters in the representation for a long integer. Digits are dropped from the middle. The default is `40`.

</div>

<div class="memberdesc">

maxstring Limit on the number of characters in the representation of the string. Note that the “normal” representation of the string is used as the character source: if escape sequences are needed in the representation, these may be mangled when the representation is shortened. The default is `30`.

</div>

<div class="memberdesc">

maxother This limit is used to control the size of object types for which no specific formatting method is available on the `Repr` object. It is applied in a similar manner as `maxstring`. The default is `20`.

</div>

<div class="methoddesc">

reprobj The equivalent to the built-in `repr()` that uses the formatting imposed by the instance.

</div>

<div class="methoddesc">

repr1obj, level Recursive implementation used by `repr()`. This uses the type of *obj* to determine which formatting method to call, passing it *obj* and *level*. The type-specific methods should call `repr1()` to perform recursive formatting, with *`level`*` - 1` for the value of *level* in the recursive call.

</div>

<div class="methoddescni">

repr\_*type*obj, level Formatting methods for specific types are implemented as methods with a name based on the type name. In the method name, *type* is replaced by `string.join(string.split(type(`*`obj`*`).__name__, ’_’)`. Dispatch to these methods is handled by `repr1()`. Type-specific methods which need to recursively format a value should call `self.repr1(`*`subobj`*`, `*`level`*` - 1)`.

</div>

## Subclassing Repr Objects <span id="subclassing-reprs" label="subclassing-reprs"></span>

The use of dynamic dispatching by `Repr.repr1()` allows subclasses of `Repr` to add support for additional built-in object types or to modify the handling of types already supported. This example shows how special support for file objects could be added:

    import repr
    import sys

    class MyRepr(repr.Repr):
        def repr_file(self, obj, level):
            if obj.name in ['<stdin>', '<stdout>', '<stderr>']:
                return obj.name
            else:
                return `obj`

    aRepr = MyRepr()
    print aRepr.repr(sys.stdin)          # prints '<stdin>'
# `resource` — Resource usage information

*An interface to provide resource usage information on the current process.*\
This module provides basic mechanisms for measuring and controlling system resources utilized by a program.

Symbolic constants are used to specify particular system resources and to request usage information about either the current process or its children.

A single exception is defined for errors:

<div class="excdesc">

error The functions described below may raise this error if the underlying system call failures unexpectedly.

</div>

## Resource Limits

Resources usage can be limited using the `setrlimit()` function described below. Each resource is controlled by a pair of limits: a soft limit and a hard limit. The soft limit is the current limit, and may be lowered or raised by a process over time. The soft limit can never exceed the hard limit. The hard limit can be lowered to any value greater than the soft limit, but not raised. (Only processes with the effective UID of the super-user can raise a hard limit.)

The specific resources that can be limited are system dependent. They are described in the man page. The resources listed below are supported when the underlying operating system supports them; resources which cannot be checked or controlled by the operating system are not defined in this module for those platforms.

<div class="funcdesc">

getrlimitresource Returns a tuple `(`*`soft`*`, `*`hard`*`)` with the current soft and hard limits of *resource*. Raises `ValueError` if an invalid resource is specified, or `error` if the underyling system call fails unexpectedly.

</div>

<div class="funcdesc">

setrlimitresource, limits Sets new limits of consumption of *resource*. The *limits* argument must be a tuple `(`*`soft`*`, `*`hard`*`)` of two integers describing the new limits. A value of `-1` can be used to specify the maximum possible upper limit.

Raises `ValueError` if an invalid resource is specified, if the new soft limit exceeds the hard limit, or if a process tries to raise its hard limit (unless the process has an effective UID of super-user). Can also raise `error` if the underyling system call fails.

</div>

These symbols define resources whose consumption can be controlled using the `setrlimit()` and `getrlimit()` functions described below. The values of these symbols are exactly the constants used by C programs.

The Unix man page for lists the available resources. Note that not all systems use the same symbol or same value to denote the same resource.

<div class="datadesc">

RLIMIT_CORE The maximum size (in bytes) of a core file that the current process can create. This may result in the creation of a partial core file if a larger core would be required to contain the entire process image.

</div>

<div class="datadesc">

RLIMIT_CPU The maximum amount of CPU time (in seconds) that a process can use. If this limit is exceeded, a signal is sent to the process. (See the `signal` module documentation for information about how to catch this signal and do something useful, e.g. flush open files to disk.)

</div>

<div class="datadesc">

RLIMIT_FSIZE The maximum size of a file which the process may create. This only affects the stack of the main thread in a multi-threaded process.

</div>

<div class="datadesc">

RLIMIT_DATA The maximum size (in bytes) of the process’s heap.

</div>

<div class="datadesc">

RLIMIT_STACK The maximum size (in bytes) of the call stack for the current process.

</div>

<div class="datadesc">

RLIMIT_RSS The maximum resident set size that should be made available to the process.

</div>

<div class="datadesc">

RLIMIT_NPROC The maximum number of processes the current process may create.

</div>

<div class="datadesc">

RLIMIT_NOFILE The maximum number of open file descriptors for the current process.

</div>

<div class="datadesc">

RLIMIT_OFILE The BSD name for .

</div>

<div class="datadesc">

RLIMIT_MEMLOC The maximm address space which may be locked in memory.

</div>

<div class="datadesc">

RLIMIT_VMEM The largest area of mapped memory which the process may occupy.

</div>

<div class="datadesc">

RLIMIT_AS The maximum area (in bytes) of address space which may be taken by the process.

</div>

## Resource Usage

These functiona are used to retrieve resource usage information:

<div class="funcdesc">

getrusagewho This function returns a large tuple that describes the resources consumed by either the current process or its children, as specified by the *who* parameter. The *who* parameter should be specified using one of the constants described below.

The elements of the return value each describe how a particular system resource has been used, e.g. amount of time spent running is user mode or number of times the process was swapped out of main memory. Some values are dependent on the clock tick internal, e.g. the amount of memory the process is using.

The first two elements of the return value are floating point values representing the amount of time spent executing in user mode and the amount of time spent executing in system mode, respectively. The remaining values are integers. Consult the man page for detailed information about these values. A brief summary is presented here:

|                  |                               |
|:-----------------|:------------------------------|
| OffsetResource 0 | time in user mode (float)     |
| 1                | time in system mode (float)   |
| 2                | maximum resident set size     |
| 3                | shared memory size            |
| 4                | unshared memory size          |
| 5                | unshared stack size           |
| 6                | page faults not requiring I/O |
| 7                | page faults requiring I/O     |
| 8                | number of swap outs           |
| 9                | block input operations        |
| 10               | block output operations       |
| 11               | messages sent                 |
| 12               | messages received             |
| 13               | signals received              |
| 14               | voluntary context switches    |
| 15               | involuntary context switches  |
|                  |                               |

This function will raise a `ValueError` if an invalid *who* parameter is specified. It may also raise `error` exception in unusual circumstances.

</div>

<div class="funcdesc">

getpagesize Returns the number of bytes in a system page. (This need not be the same as the hardware page size.) This function is useful for determining the number of bytes of memory a process is using. The third element of the tuple returned by `getrusage()` describes memory usage in pages; multiplying by page size produces number of bytes.

</div>

The following symbols are passed to the `getrusage()` function to specify which processes information should be provided for.

<div class="datadesc">

RUSAGE_SELF should be used to request information pertaining only to the process itself.

</div>

<div class="datadesc">

RUSAGE_CHILDREN Pass to `getrusage()` to request resource information for child processes of the calling process.

</div>

<div class="datadesc">

RUSAGE_BOTH Pass to `getrusage()` to request resources consumed by both the current process and child processes. May not be available on all systems.

</div>
# `rexec` — Restricted execution framework

*Basic restricted execution framework.*\
This module contains the `RExec` class, which supports `r_eval()`, `r_execfile()`, `r_exec()`, and `r_import()` methods, which are restricted versions of the standard Python functions `eval()`, `execfile()` and the and statements. Code executed in this restricted environment will only have access to modules and functions that are deemed safe; you can subclass `RExec` to add or remove capabilities as desired.

*Note:* The `RExec` class can prevent code from performing unsafe operations like reading or writing disk files, or using TCP/IP sockets. However, it does not protect against code using extremely large amounts of memory or CPU time.

<div class="classdesc">

RExec Returns an instance of the `RExec` class.

*hooks* is an instance of the `RHooks` class or a subclass of it. If it is omitted or `None`, the default `RHooks` class is instantiated. Whenever the `rexec` module searches for a module (even a built-in one) or reads a module’s code, it doesn’t actually go out to the file system itself. Rather, it calls methods of an `RHooks` instance that was passed to or created by its constructor. (Actually, the `RExec` object doesn’t make these calls — they are made by a module loader object that’s part of the `RExec` object. This allows another level of flexibility, e.g. using packages.)

By providing an alternate `RHooks` object, we can control the file system accesses made to import a module, without changing the actual algorithm that controls the order in which those accesses are made. For instance, we could substitute an `RHooks` object that passes all filesystem requests to a file server elsewhere, via some RPC mechanism such as ILU. Grail’s applet loader uses this to support importing applets from a URL for a directory.

If *verbose* is true, additional debugging output may be sent to standard output.

</div>

The `RExec` class has the following class attributes, which are used by the `__init__()` method. Changing them on an existing instance won’t have any effect; instead, create a subclass of `RExec` and assign them new values in the class definition. Instances of the new class will then use those new values. All these attributes are tuples of strings.

<div class="memberdesc">

nok_builtin_names Contains the names of built-in functions which will *not* be available to programs running in the restricted environment. The value for `RExec` is `(’open’,` `’reload’,` `’__import__’)`. (This gives the exceptions, because by far the majority of built-in functions are harmless. A subclass that wants to override this variable should probably start with the value from the base class and concatenate additional forbidden functions — when new dangerous built-in functions are added to Python, they will also be added to this module.)

</div>

<div class="memberdesc">

ok_builtin_modules Contains the names of built-in modules which can be safely imported. The value for `RExec` is `(’audioop’,` `’array’,` `’binascii’,` `’cmath’,` `’errno’,` `’imageop’,` `’marshal’,` `’math’,` `’md5’,` `’operator’,` `’parser’,` `’regex’,` `’rotor’,` `’select’,` `’strop’,` `’struct’,` `’time’)`. A similar remark about overriding this variable applies — use the value from the base class as a starting point.

</div>

<div class="memberdesc">

ok_path Contains the directories which will be searched when an is performed in the restricted environment. The value for `RExec` is the same as `sys.path` (at the time the module is loaded) for unrestricted code.

</div>

<div class="memberdesc">

ok_posix_names

Contains the names of the functions in the `os` module which will be available to programs running in the restricted environment. The value for `RExec` is `(’error’,` `’fstat’,` `’listdir’,` `’lstat’,` `’readlink’,` `’stat’,` `’times’,` `’uname’,` `’getpid’,` `’getppid’,` `’getcwd’,` `’getuid’,` `’getgid’,` `’geteuid’,` `’getegid’)`.

</div>

<div class="memberdesc">

ok_sys_names Contains the names of the functions and variables in the `sys` module which will be available to programs running in the restricted environment. The value for `RExec` is `(’ps1’,` `’ps2’,` `’copyright’,` `’version’,` `’platform’,` `’exit’,` `’maxint’)`.

</div>

`RExec` instances support the following methods:

<div class="methoddesc">

r_evalcode *code* must either be a string containing a Python expression, or a compiled code object, which will be evaluated in the restricted environment’s `__main__` module. The value of the expression or code object will be returned.

</div>

<div class="methoddesc">

r_execcode *code* must either be a string containing one or more lines of Python code, or a compiled code object, which will be executed in the restricted environment’s `__main__` module.

</div>

<div class="methoddesc">

r_execfilefilename Execute the Python code contained in the file *filename* in the restricted environment’s `__main__` module.

</div>

Methods whose names begin with `s_` are similar to the functions beginning with `r_`, but the code will be granted access to restricted versions of the standard I/O streams `sys.stdin`, `sys.stderr`, and `sys.stdout`.

<div class="methoddesc">

s_evalcode *code* must be a string containing a Python expression, which will be evaluated in the restricted environment.

</div>

<div class="methoddesc">

s_execcode *code* must be a string containing one or more lines of Python code, which will be executed in the restricted environment.

</div>

<div class="methoddesc">

s_execfilecode Execute the Python code contained in the file *filename* in the restricted environment.

</div>

`RExec` objects must also support various methods which will be implicitly called by code executing in the restricted environment. Overriding these methods in a subclass is used to change the policies enforced by a restricted environment.

<div class="methoddesc">

r_importmodulename Import the module *modulename*, raising an `ImportError` exception if the module is considered unsafe.

</div>

<div class="methoddesc">

r_openfilename Method called when `open()` is called in the restricted environment. The arguments are identical to those of `open()`, and a file object (or a class instance compatible with file objects) should be returned. `RExec`’s default behaviour is allow opening any file for reading, but forbidding any attempt to write a file. See the example below for an implementation of a less restrictive `r_open()`.

</div>

<div class="methoddesc">

r_reloadmodule Reload the module object *module*, re-parsing and re-initializing it.

</div>

<div class="methoddesc">

r_unloadmodule Unload the module object *module* (i.e., remove it from the restricted environment’s `sys.modules` dictionary).

</div>

And their equivalents with access to restricted standard I/O streams:

<div class="methoddesc">

s_importmodulename Import the module *modulename*, raising an `ImportError` exception if the module is considered unsafe.

</div>

<div class="methoddesc">

s_reloadmodule Reload the module object *module*, re-parsing and re-initializing it.

</div>

<div class="methoddesc">

s_unloadmodule Unload the module object *module*.

</div>

## An example

Let us say that we want a slightly more relaxed policy than the standard `RExec` class. For example, if we’re willing to allow files in `/tmp` to be written, we can subclass the `RExec` class:

    class TmpWriterRExec(rexec.RExec):
        def r_open(self, file, mode='r', buf=-1):
            if mode in ('r', 'rb'):
                pass
            elif mode in ('w', 'wb', 'a', 'ab'):
                # check filename : must begin with /tmp/
                if file[:5]!='/tmp/': 
                    raise IOError, "can't write outside /tmp"
                elif (string.find(file, '/../') >= 0 or
                     file[:3] == '../' or file[-3:] == '/..'):
                    raise IOError, "'..' in filename forbidden"
            else: raise IOError, "Illegal open() mode"
            return open(file, mode, buf)

Notice that the above code will occasionally forbid a perfectly valid filename; for example, code in the restricted environment won’t be able to open a file called `/tmp/foo/../bar`. To fix this, the `r_open()` method would have to simplify the filename to `/tmp/bar`, which would require splitting apart the filename and performing various operations on it. In cases where security is at stake, it may be preferable to write simple code which is sometimes overly restrictive, instead of more general code that is also more complex and may harbor a subtle security hole.
# `rgbimg` — Read and write “SGI RGB” files

*Read and write image files in “SGI RGB” format (the module is *not* SGI specific though!).*\
The `rgbimg` module allows Python programs to access SGI imglib image files (also known as `.rgb` files). The module is far from complete, but is provided anyway since the functionality that there is enough in some cases. Currently, colormap files are not supported.

The module defines the following variables and functions:

<div class="excdesc">

error This exception is raised on all errors, such as unsupported file type, etc.

</div>

<div class="funcdesc">

sizeofimagefile This function returns a tuple `(`*`x`*`, `*`y`*`)` where *x* and *y* are the size of the image in pixels. Only 4 byte RGBA pixels, 3 byte RGB pixels, and 1 byte greyscale pixels are currently supported.

</div>

<div class="funcdesc">

longimagedatafile This function reads and decodes the image on the specified file, and returns it as a Python string. The string has 4 byte RGBA pixels. The bottom left pixel is the first in the string. This format is suitable to pass to `gl.lrectwrite()`, for instance.

</div>

<div class="funcdesc">

longstoimagedata, x, y, z, file This function writes the RGBA data in *data* to image file *file*. *x* and *y* give the size of the image. *z* is 1 if the saved image should be 1 byte greyscale, 3 if the saved image should be 3 byte RGB data, or 4 if the saved images should be 4 byte RGBA data. The input data always contains 4 bytes per pixel. These are the formats returned by `gl.lrectread()`.

</div>

<div class="funcdesc">

ttobflag This function sets a global flag which defines whether the scan lines of the image are read or written from bottom to top (flag is zero, compatible with SGI GL) or from top to bottom(flag is one, compatible with X). The default is zero.

</div>
# `rlcompleter` — Completion function for readline

*Python identifier completion in the readline library.*\
The `rlcompleter` module defines a completion function for the `readline` module by completing valid Python identifiers and keywords.

This module is Unix-specific due to it’s dependence on the `readline` module.

The `rlcompleter` module defines the `Completer` class.

Example:

    >>> import rlcompleter
    >>> import readline
    >>> readline.parse_and_bind("tab: complete")
    >>> readline. <TAB PRESSED>
    readline.__doc__          readline.get_line_buffer  readline.read_init_file
    readline.__file__         readline.insert_text      readline.set_completer
    readline.__name__         readline.parse_and_bind
    >>> readline.

The `rlcompleter` module is designed for use with Python’s interactive mode. A user can add the following lines to his or her initialization file (identified by the environment variable) to get automatic `Tab` completion:

    try:
        import readline
    except ImportError:
        print "Module readline not available."
    else:
        import rlcompleter
        readline.parse_and_bind("tab: complete")

## Completer Objects <span id="completer-objects" label="completer-objects"></span>

Completer objects have the following method:

<div class="methoddesc">

completetext, state Return the *state*th completion for *text*.

If called for *text* that doesn’t include a period character (), it will complete from names currently defined in `__main__`, `__builtin__` and keywords (as defined by the `keyword` module).

If called for a dotted name, it will try to evaluate anything without obvious side-effects (i.e., functions will not be evaluated, but it can generate calls to `__getattr__()`) upto the last part, and find matches for the rest via the `dir()` function.

</div>
# `robotparser` — Parser for robots.txt

*Accepts as input a list of lines or URL that refers to a robots.txt file, parses the file, then builds a set of rules from that list and answers questions about fetchability of other URLs.*\
This module provides a single class, `RobotFileParser`, which answers questions about whether or not a particular user agent can fetch a URL on the web site that published the `robots.txt` file. For more details on the structure of `robots.txt` files, see `http://info.webcrawler.com/mak/projects/robots/norobots.html`.

<div class="classdesc">

RobotFileParser

This class provides a set of methods to read, parse and answer questions about a single `robots.txt` file.

<div class="methoddesc">

set_urlurl Sets the URL referring to a `robots.txt` file.

</div>

<div class="methoddesc">

read Reads the `robots.txt` URL and feeds it to the parser.

</div>

<div class="methoddesc">

parselines Parses the lines argument.

</div>

<div class="methoddesc">

can_fetchuseragent, url Returns true if the *useragent* is allowed to fetch the *url* according to the rules contained in the parsed `robots.txt` file.

</div>

<div class="methoddesc">

mtime Returns the time the `robots.txt` file was last fetched. This is useful for long-running web spiders that need to check for new `robots.txt` files periodically.

</div>

<div class="methoddesc">

modified Sets the time the `robots.txt` file was last fetched to the current time.

</div>

</div>

The following example demonstrates basic use of the RobotFileParser class.

    >>> import robotparser
    >>> rp = robotparser.RobotFileParser()
    >>> rp.set_url("http://www.musi-cal.com/robots.txt")
    >>> rp.read()
    >>> rp.can_fetch("*", "http://www.musi-cal.com/cgi-bin/search?city=San+Francisco")
    0
    >>> rp.can_fetch("*", "http://www.musi-cal.com/")
    1
# `rotor` — Enigma-like encryption and decryption.

*Enigma-like encryption and decryption.*\
This module implements a rotor-based encryption algorithm, contributed by Lance Ellinghouse. The design is derived from the Enigma device, a machine used during World War II to encipher messages. A rotor is simply a permutation. For example, if the character ‘A’ is the origin of the rotor, then a given rotor might map ‘A’ to ‘L’, ‘B’ to ‘Z’, ‘C’ to ‘G’, and so on. To encrypt, we choose several different rotors, and set the origins of the rotors to known positions; their initial position is the ciphering key. To encipher a character, we permute the original character by the first rotor, and then apply the second rotor’s permutation to the result. We continue until we’ve applied all the rotors; the resulting character is our ciphertext. We then change the origin of the final rotor by one position, from ‘A’ to ‘B’; if the final rotor has made a complete revolution, then we rotate the next-to-last rotor by one position, and apply the same procedure recursively. In other words, after enciphering one character, we advance the rotors in the same fashion as a car’s odometer. Decoding works in the same way, except we reverse the permutations and apply them in the opposite order. The available functions in this module are:

<div class="funcdesc">

newrotorkey Return a rotor object. *key* is a string containing the encryption key for the object; it can contain arbitrary binary data. The key will be used to randomly generate the rotor permutations and their initial positions. *numrotors* is the number of rotor permutations in the returned object; if it is omitted, a default value of 6 will be used.

</div>

Rotor objects have the following methods:

<div class="methoddesc">

setkeykey Sets the rotor’s key to *key*.

</div>

<div class="methoddesc">

encryptplaintext Reset the rotor object to its initial state and encrypt *plaintext*, returning a string containing the ciphertext. The ciphertext is always the same length as the original plaintext.

</div>

<div class="methoddesc">

encryptmoreplaintext Encrypt *plaintext* without resetting the rotor object, and return a string containing the ciphertext.

</div>

<div class="methoddesc">

decryptciphertext Reset the rotor object to its initial state and decrypt *ciphertext*, returning a string containing the ciphertext. The plaintext string will always be the same length as the ciphertext.

</div>

<div class="methoddesc">

decryptmoreciphertext Decrypt *ciphertext* without resetting the rotor object, and return a string containing the ciphertext.

</div>

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

The module’s code is not an exact simulation of the original Enigma device; it implements the rotor encryption scheme differently from the original. The most important difference is that in the original Enigma, there were only 5 or 6 different rotors in existence, and they were applied twice to each character; the cipher key was the order in which they were placed in the machine. The Python `rotor` module uses the supplied key to initialize a random number generator; the rotor permutations and their initial positions are then randomly generated. The original device only enciphered the letters of the alphabet, while this module can handle any 8-bit binary data; it also produces binary output. This module can also operate with an arbitrary number of rotors.

The original Enigma cipher was broken in 1944. The version implemented here is probably a good deal more difficult to crack (especially if you use many rotors), but it won’t be impossible for a truly skillful and determined attacker to break the cipher. So if you want to keep the NSA out of your files, this rotor cipher may well be unsafe, but for discouraging casual snooping through your files, it will probably be just fine, and may be somewhat safer than using the Unix command.
# `sched` — Event scheduler

*General purpose event scheduler.*\
The `sched` module defines a class which implements a general purpose event scheduler:

<div class="classdesc">

schedulertimefunc, delayfunc The `scheduler` class defines a generic interface to scheduling events. It needs two functions to actually deal with the “outside world” — *timefunc* should be callable without arguments, and return a number (the “time”, in any units whatsoever). The *delayfunc* function should be callable with one argument, compatible with the output of *timefunc*, and should delay that many time units. *delayfunc* will also be called with the argument `0` after each event is run to allow other threads an opportunity to run in multi-threaded applications.

</div>

Example:

    >>> import sched, time
    >>> s=sched.scheduler(time.time, time.sleep)
    >>> def print_time(): print "From print_time", time.time()
    ...
    >>> def print_some_times():
    ...     print time.time()
    ...     s.enter(5, 1, print_time, ())
    ...     s.enter(10, 1, print_time, ())
    ...     s.run()
    ...     print time.time()
    ...
    >>> print_some_times()
    930343690.257
    From print_time 930343695.274
    From print_time 930343700.273
    930343700.276

## Scheduler Objects <span id="scheduler-objects" label="scheduler-objects"></span>

`scheduler` instances have the following methods:

<div class="methoddesc">

enterabstime, priority, action, argument Schedule a new event. The *time* argument should be a numeric type compatible with the return value of the *timefunc* function passed to the constructor. Events scheduled for the same *time* will be executed in the order of their *priority*.

Executing the event means executing `apply(`*`action`*`, `*`argument`*`)`. *argument* must be a tuple holding the parameters for *action*.

Return value is an event which may be used for later cancellation of the event (see `cancel()`).

</div>

<div class="methoddesc">

enterdelay, priority, action, argument Schedule an event for *delay* more time units. Other then the relative time, the other arguments, the effect and the return value are the same as those for `enterabs()`.

</div>

<div class="methoddesc">

cancelevent Remove the event from the queue. If *event* is not an event currently in the queue, this method will raise a `RuntimeError`.

</div>

<div class="methoddesc">

empty Return true if the event queue is empty.

</div>

<div class="methoddesc">

run Run all scheduled events. This function will wait (using the `delayfunc` function passed to the constructor) for the next event, then execute it and so on until there are no more scheduled events.

Either *action* or *delayfunc* can raise an exception. In either case, the scheduler will maintain a consistent state and propagate the exception. If an exception is raised by *action*, the event will not be attempted in future calls to `run()`.

If a sequence of events takes longer to run than the time available before the next event, the scheduler will simply fall behind. No events will be dropped; the calling code is responsible for canceling events which are no longer pertinent.

</div>
# `select` — Waiting for I/O completion

*Wait for I/O completion on multiple streams.*\
This module provides access to the and functions available in most operating systems. Note that on Windows, it only works for sockets; on other operating systems, it also works for other file types (in particular, on Unix, it works on pipes). It cannot be used on regular files to determine whether a file has grown since it was last read.

The module defines the following:

<div class="excdesc">

error The exception raised when an error occurs. The accompanying value is a pair containing the numeric error code from and the corresponding string, as would be printed by the C function .

</div>

<div class="funcdesc">

poll (Not supported by all operating systems.) Returns a polling object, which supports registering and unregistering file descriptors, and then polling them for I/O events; see section <a href="#poll-objects" data-reference-type="ref" data-reference="poll-objects">[poll-objects]</a> below for the methods supported by polling objects.

</div>

<div class="funcdesc">

selectiwtd, owtd, ewtd This is a straightforward interface to the Unix system call. The first three arguments are lists of ‘waitable objects’: either integers representing Unix file descriptors or objects with a parameterless method named `fileno()` returning such an integer. The three lists of waitable objects are for input, output and ‘exceptional conditions’, respectively. Empty lists are allowed. The optional *timeout* argument specifies a time-out as a floating point number in seconds. When the *timeout* argument is omitted the function blocks until at least one file descriptor is ready. A time-out value of zero specifies a poll and never blocks.

The return value is a triple of lists of objects that are ready: subsets of the first three arguments. When the time-out is reached without a file descriptor becoming ready, three empty lists are returned.

Amongst the acceptable object types in the lists are Python file objects (e.g. `sys.stdin`, or objects returned by `open()` or `os.popen()`), socket objects returned by `socket.socket()`, and the module `stdwin`which happens to define a function `fileno()`for just this purpose. You may also define a *wrapper* class yourself, as long as it has an appropriate `fileno()` method (that really returns a Unix file descriptor, not just a random integer).

</div>

## Polling Objects <span id="poll-objects" label="poll-objects"></span>

The system call, supported on most Unix systems, provides better scalability for network servers that service many, many clients at the same time. scales better because the system call only requires listing the file descriptors of interest, while builds a bitmap, turns on bits for the fds of interest, and then afterward the whole bitmap has to be linearly scanned again. is O(highest file descriptor), while is O(number of file descriptors).

<div class="methoddesc">

registerfd Register a file descriptor with the polling object. Future calls to the `poll()` method will then check whether the file descriptor has any pending I/O events. *fd* can be either an integer, or an object with a `fileno()` method that returns an integer. File objects implement `fileno()`, so they can also be used as the argument.

*eventmask* is an optional bitmask describing the type of events you want to check for, and can be a combination of the constants , , and , described in the table below. If not specified, the default value used will check for all 3 types of events.

|                        |                                          |
|:-----------------------|:-----------------------------------------|
| ConstantMeaning POLLIN | There is data to read                    |
| POLLPRI                | There is urgent data to read             |
| POLLOUT                | Ready for output: writing will not block |
| POLLERR                | Error condition of some sort             |
| POLLHUP                | Hung up                                  |
| POLLNVAL               | Invalid request: descriptor not open     |
|                        |                                          |

Registering a file descriptor that’s already registered is not an error, and has the same effect as registering the descriptor exactly once.

</div>

<div class="methoddesc">

unregisterfd Remove a file descriptor being tracked by a polling object. Just like the `register()` method, *fd* can be an integer or an object with a `fileno()` method that returns an integer.

Attempting to remove a file descriptor that was never registered causes a `KeyError` exception to be raised.

</div>

<div class="methoddesc">

poll Polls the set of registered file descriptors, and returns a possibly-empty list containing `(`*`fd`*`, `*`event`*`)` 2-tuples for the descriptors that have events or errors to report. *fd* is the file descriptor, and *event* is a bitmask with bits set for the reported events for that descriptor — for waiting input, to indicate that the descriptor can be written to, and so forth. An empty list indicates that the call timed out and no file descriptors had any events to report.

</div>
# SGI IRIX Specific Services

The modules described in this chapter provide interfaces to features that are unique to SGI’s IRIX operating system (versions 4 and 5).
# `sgmllib` — Simple SGML parser

*Only as much of an SGML parser as needed to parse HTML.*\
This module defines a class `SGMLParser` which serves as the basis for parsing text files formatted in SGML (Standard Generalized Mark-up Language). In fact, it does not provide a full SGML parser — it only parses SGML insofar as it is used by HTML, and the module only exists as a base for the `htmllib`module.

<div class="classdesc">

SGMLParser The `SGMLParser` class is instantiated without arguments. The parser is hardcoded to recognize the following constructs:

- Opening and closing tags of the form `<`*`tag`*` `*`attr`*`="`*`value`*`" ...>` and `</`*`tag`*`>`, respectively.

- Numeric character references of the form `&#`*`name`*`;`.

- Entity references of the form `&`*`name`*`;`.

- SGML comments of the form `<!--`*`text`*`-->`. Note that spaces, tabs, and newlines are allowed between the trailing `>` and the immediately preceding `--`.

</div>

`SGMLParser` instances have the following interface methods:

<div class="methoddesc">

reset Reset the instance. Loses all unprocessed data. This is called implicitly at instantiation time.

</div>

<div class="methoddesc">

setnomoretags Stop processing tags. Treat all following input as literal input (CDATA). (This is only provided so the HTML tag `<PLAINTEXT>` can be implemented.)

</div>

<div class="methoddesc">

setliteral Enter literal mode (CDATA mode).

</div>

<div class="methoddesc">

feeddata Feed some text to the parser. It is processed insofar as it consists of complete elements; incomplete data is buffered until more data is fed or `close()` is called.

</div>

<div class="methoddesc">

close Force processing of all buffered data as if it were followed by an end-of-file mark. This method may be redefined by a derived class to define additional processing at the end of the input, but the redefined version should always call `close()`.

</div>

<div class="methoddesc">

get_starttag_text Return the text of the most recently opened start tag. This should not normally be needed for structured processing, but may be useful in dealing with HTML “as deployed” or for re-generating input with minimal changes (whitespace between attributes can be preserved, etc.).

</div>

<div class="methoddesc">

handle_starttagtag, method, attributes This method is called to handle start tags for which either a `start_`*`tag`*`()` or `do_`*`tag`*`()` method has been defined. The *tag* argument is the name of the tag converted to lower case, and the *method* argument is the bound method which should be used to support semantic interpretation of the start tag. The *attributes* argument is a list of `(`*`name`*`, `*`value`*`)` pairs containing the attributes found inside the tag’s `<>` brackets. The *name* has been translated to lower case and double quotes and backslashes in the *value* have been interpreted. For instance, for the tag `<A HREF="http://www.cwi.nl/">`, this method would be called as `unknown_starttag(’a’, [(’href’, ’http://www.cwi.nl/’)])`. The base implementation simply calls *method* with *attributes* as the only argument.

</div>

<div class="methoddesc">

handle_endtagtag, method This method is called to handle endtags for which an `end_`*`tag`*`()` method has been defined. The *tag* argument is the name of the tag converted to lower case, and the *method* argument is the bound method which should be used to support semantic interpretation of the end tag. If no `end_`*`tag`*`()` method is defined for the closing element, this handler is not called. The base implementation simply calls *method*.

</div>

<div class="methoddesc">

handle_datadata This method is called to process arbitrary data. It is intended to be overridden by a derived class; the base class implementation does nothing.

</div>

<div class="methoddesc">

handle_charrefref This method is called to process a character reference of the form `&#`*`ref`*`;`. In the base implementation, *ref* must be a decimal number in the range 0-255. It translates the character to and calls the method `handle_data()` with the character as argument. If *ref* is invalid or out of range, the method `unknown_charref(`*`ref`*`)` is called to handle the error. A subclass must override this method to provide support for named character entities.

</div>

<div class="methoddesc">

handle_entityrefref This method is called to process a general entity reference of the form `&`*`ref`*`;` where *ref* is an general entity reference. It looks for *ref* in the instance (or class) variable `entitydefs` which should be a mapping from entity names to corresponding translations. If a translation is found, it calls the method `handle_data()` with the translation; otherwise, it calls the method `unknown_entityref(`*`ref`*`)`. The default `entitydefs` defines translations for `&amp;`, `&apos`, `&gt;`, `&lt;`, and `&quot;`.

</div>

<div class="methoddesc">

handle_commentcomment This method is called when a comment is encountered. The *comment* argument is a string containing the text between the `<!--` and `-->` delimiters, but not the delimiters themselves. For example, the comment `<!--text-->` will cause this method to be called with the argument `’text’`. The default method does nothing.

</div>

<div class="methoddesc">

report_unbalancedtag This method is called when an end tag is found which does not correspond to any open element.

</div>

<div class="methoddesc">

unknown_starttagtag, attributes This method is called to process an unknown start tag. It is intended to be overridden by a derived class; the base class implementation does nothing.

</div>

<div class="methoddesc">

unknown_endtagtag This method is called to process an unknown end tag. It is intended to be overridden by a derived class; the base class implementation does nothing.

</div>

<div class="methoddesc">

unknown_charrefref This method is called to process unresolvable numeric character references. Refer to `handle_charref()` to determine what is handled by default. It is intended to be overridden by a derived class; the base class implementation does nothing.

</div>

<div class="methoddesc">

unknown_entityrefref This method is called to process an unknown entity reference. It is intended to be overridden by a derived class; the base class implementation does nothing.

</div>

Apart from overriding or extending the methods listed above, derived classes may also define methods of the following form to define processing of specific tags. Tag names in the input stream are case independent; the *tag* occurring in method names must be in lower case:

<div class="methoddescni">

start\_*tag*attributes This method is called to process an opening tag *tag*. It has preference over `do_`*`tag`*`()`. The *attributes* argument has the same meaning as described for `handle_starttag()` above.

</div>

<div class="methoddescni">

do\_*tag*attributes This method is called to process an opening tag *tag* that does not come with a matching closing tag. The *attributes* argument has the same meaning as described for `handle_starttag()` above.

</div>

<div class="methoddescni">

end\_*tag* This method is called to process a closing tag *tag*.

</div>

Note that the parser maintains a stack of open elements for which no end tag has been found yet. Only tags processed by `start_`*`tag`*`()` are pushed on this stack. Definition of an `end_`*`tag`*`()` method is optional for these tags. For tags processed by `do_`*`tag`*`()` or by `unknown_tag()`, no `end_`*`tag`*`()` method must be defined; if defined, it will not be used. If both `start_`*`tag`*`()` and `do_`*`tag`*`()` methods exist for a tag, the `start_`*`tag`*`()` method takes precedence.
# `shutil` — High-level file operations

*High-level file operations, including copying.*\
The `shutil` module offers a number of high-level operations on files and collections of files. In particular, functions are provided which support file copying and removal. **Caveat:** On MacOS, the resource fork and other metadata are not used. For file copies, this means that resources will be lost and file type and creator codes will not be correct.

<div class="funcdesc">

copyfilesrc, dst Copy the contents of *src* to *dst*. If *dst* exists, it will be replaced, otherwise it will be created.

</div>

<div class="funcdesc">

copyfileobjfsrc, fdst Copy the contents of the file-like object *fsrc* to the file-like object *fdst*. The integer *length*, if given, is the buffer size. In particular, a negative *length* value means to copy the data without looping over the source data in chunks; by default the data is read in chunks to avoid uncontrolled memory consumption.

</div>

<div class="funcdesc">

copymodesrc, dst Copy the permission bits from *src* to *dst*. The file contents, owner, and group are unaffected.

</div>

<div class="funcdesc">

copystatsrc, dst Copy the permission bits, last access time, and last modification time from *src* to *dst*. The file contents, owner, and group are unaffected.

</div>

<div class="funcdesc">

copysrc, dst Copy the file *src* to the file or directory *dst*. If *dst* is a directory, a file with the same basename as *src* is created (or overwritten) in the directory specified. Permission bits are copied.

</div>

<div class="funcdesc">

copy2src, dst Similar to `copy()`, but last access time and last modification time are copied as well. This is similar to the Unix command `-p`.

</div>

<div class="funcdesc">

copytreesrc, dst Recursively copy an entire directory tree rooted at *src*. The destination directory, named by *dst*, must not already exist; it will be created. Individual files are copied using `copy2()`. If *symlinks* is true, symbolic links in the source tree are represented as symbolic links in the new tree; if false or omitted, the contents of the linked files are copied to the new tree. Errors are reported to standard output.

The source code for this should be considered an example rather than a tool.

</div>

<div class="funcdesc">

rmtreepath Delete an entire directory tree. If *ignore_errors* is true, errors will be ignored; if false or omitted, errors are handled by calling a handler specified by *onerror* or raise an exception.

If *onerror* is provided, it must be a callable that accepts three parameters: *function*, *path*, and *excinfo*. The first parameter, *function*, is the function which raised the exception; it will be `os.remove()` or `os.rmdir()`. The second parameter, *path*, will be the path name passed to *function*. The third parameter, *excinfo*, will be the exception information return by `sys.exc_info()`. Exceptions raised by *onerror* will not be caught.

</div>

## Example <span id="shutil-example" label="shutil-example"></span>

This example is the implementation of the `copytree()` function, described above, with the docstring omitted. It demonstrates many of the other functions provided by this module.

    def copytree(src, dst, symlinks=0):
        names = os.listdir(src)
        os.mkdir(dst)
        for name in names:
            srcname = os.path.join(src, name)
            dstname = os.path.join(dst, name)
            try:
                if symlinks and os.path.islink(srcname):
                    linkto = os.readlink(srcname)
                    os.symlink(linkto, dstname)
                elif os.path.isdir(srcname):
                    copytree(srcname, dstname)
                else:
                    copy2(srcname, dstname)
                # XXX What about devices, sockets etc.?
            except (IOError, os.error), why:
                print "Can't copy %s to %s: %s" % (`srcname`, `dstname`, str(why))
# `signal` — Set handlers for asynchronous events.

*Set handlers for asynchronous events.*\
This module provides mechanisms to use signal handlers in Python. Some general rules for working with signals and their handlers:

- A handler for a particular signal, once set, remains installed until it is explicitly reset (i.e. Python emulates the BSD style interface regardless of the underlying implementation), with the exception of the handler for , which follows the underlying implementation.

- There is no way to “block” signals temporarily from critical sections (since this is not supported by all Unix flavors).

- Although Python signal handlers are called asynchronously as far as the Python user is concerned, they can only occur between the “atomic” instructions of the Python interpreter. This means that signals arriving during long calculations implemented purely in C (e.g. regular expression matches on large bodies of text) may be delayed for an arbitrary amount of time.

- When a signal arrives during an I/O operation, it is possible that the I/O operation raises an exception after the signal handler returns. This is dependent on the underlying Unix system’s semantics regarding interrupted system calls.

- Because the C signal handler always returns, it makes little sense to catch synchronous errors like or .

- Python installs a small number of signal handlers by default: is ignored (so write errors on pipes and sockets can be reported as ordinary Python exceptions) and is translated into a `KeyboardInterrupt` exception. All of these can be overridden.

- Some care must be taken if both signals and threads are used in the same program. The fundamental thing to remember in using signals and threads simultaneously is: always perform `signal()` operations in the main thread of execution. Any thread can perform an `alarm()`, `getsignal()`, or `pause()`; only the main thread can set a new signal handler, and the main thread will be the only one to receive signals (this is enforced by the Python `signal` module, even if the underlying thread implementation supports sending signals to individual threads). This means that signals can’t be used as a means of inter-thread communication. Use locks instead.

The variables defined in the `signal` module are:

<div class="datadesc">

SIG_DFL This is one of two standard signal handling options; it will simply perform the default function for the signal. For example, on most systems the default action for is to dump core and exit, while the default action for is to simply ignore it.

</div>

<div class="datadesc">

SIG_IGN This is another standard signal handler, which will simply ignore the given signal.

</div>

<div class="datadesc">

SIG\* All the signal numbers are defined symbolically. For example, the hangup signal is defined as ; the variable names are identical to the names used in C programs, as found in `<signal.h>`. The Unix man page for ‘’ lists the existing signals (on some systems this is , on others the list is in ). Note that not all systems define the same set of signal names; only those names defined by the system are defined by this module.

</div>

<div class="datadesc">

NSIG One more than the number of the highest signal number.

</div>

The `signal` module defines the following functions:

<div class="funcdesc">

alarmtime If *time* is non-zero, this function requests that a signal be sent to the process in *time* seconds. Any previously scheduled alarm is canceled (i.e. only one alarm can be scheduled at any time). The returned value is then the number of seconds before any previously set alarm was to have been delivered. If *time* is zero, no alarm id scheduled, and any scheduled alarm is canceled. The return value is the number of seconds remaining before a previously scheduled alarm. If the return value is zero, no alarm is currently scheduled. (See the Unix man page .)

</div>

<div class="funcdesc">

getsignalsignalnum Return the current signal handler for the signal *signalnum*. The returned value may be a callable Python object, or one of the special values , or . Here, means that the signal was previously ignored, means that the default way of handling the signal was previously in use, and `None` means that the previous signal handler was not installed from Python.

</div>

<div class="funcdesc">

pause Cause the process to sleep until a signal is received; the appropriate handler will then be called. Returns nothing. (See the Unix man page .)

</div>

<div class="funcdesc">

signalsignalnum, handler Set the handler for signal *signalnum* to the function *handler*. *handler* can be a callable Python object taking two arguments (see below), or one of the special values or . The previous signal handler will be returned (see the description of `getsignal()` above). (See the Unix man page .)

When threads are enabled, this function can only be called from the main thread; attempting to call it from other threads will cause a `ValueError` exception to be raised.

The *handler* is called with two arguments: the signal number and the current stack frame (`None` or a frame object; see the reference manual for a description of frame objects).

</div>

## Example

Here is a minimal example program. It uses the `alarm()` function to limit the time spent waiting to open a file; this is useful if the file is for a serial device that may not be turned on, which would normally cause the `os.open()` to hang indefinitely. The solution is to set a 5-second alarm before opening the file; if the operation takes too long, the alarm signal will be sent, and the handler raises an exception.

    import signal, os, FCNTL

    def handler(signum, frame):
        print 'Signal handler called with signal', signum
        raise IOError, "Couldn't open device!"

    # Set the signal handler and a 5-second alarm
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(5)

    # This open() may hang indefinitely
    fd = os.open('/dev/ttyS0', FCNTL.O_RDWR)  

    signal.alarm(0)          # Disable the alarm
# `site` — Site-specific configuration hook

*A standard way to reference site-specific modules.*\
**This module is automatically imported during initialization.**

In earlier versions of Python (up to and including 1.5a3), scripts or modules that needed to use site-specific modules would place `import site` somewhere near the top of their code. This is no longer necessary.

This will append site-specific paths to the module search path. It starts by constructing up to four directories from a head and a tail part. For the head part, it uses `sys.prefix` and `sys.exec_prefix`; empty heads are skipped. For the tail part, it uses the empty string (on Macintosh or Windows) or it uses first `lib/python/site-packages` and then `lib/site-python` (on Unix). For each of the distinct head-tail combinations, it sees if it refers to an existing directory, and if so, adds to `sys.path`, and also inspected for path configuration files. A path configuration file is a file whose name has the form *`package`*`.pth`; its contents are additional items (one per line) to be added to `sys.path`. Non-existing items are never added to `sys.path`, but no check is made that the item refers to a directory (rather than a file). No item is added to `sys.path` more than once. Blank lines and lines beginning with `#` are skipped. For example, suppose `sys.prefix` and `sys.exec_prefix` are set to `/usr/local`. The Python  library is then installed in `/usr/local/lib/python` (where only the first three characters of `sys.version` are used to form the installation path name). Suppose this has a subdirectory `/usr/local/lib/python/site-packages` with three subsubdirectories, `foo`, `bar` and `spam`, and two path configuration files, `foo.pth` and `bar.pth`. Assume `foo.pth` contains the following:

    # foo package configuration

    foo
    bar
    bletch

and `bar.pth` contains:

    # bar package configuration

    bar

Then the following directories are added to `sys.path`, in this order:

    /usr/local/lib/python1.5/site-packages/bar
    /usr/local/lib/python1.5/site-packages/foo

Note that `bletch` is omitted because it doesn’t exist; the `bar` directory precedes the `foo` directory because `bar.pth` comes alphabetically before `foo.pth`; and `spam` is omitted because it is not mentioned in either path configuration file.

After these path manipulations, an attempt is made to import a module named `sitecustomize`, which can perform arbitrary site-specific customizations. If this import fails with an `ImportError` exception, it is silently ignored.

Note that for some non-Unix systems, `sys.prefix` and `sys.exec_prefix` are empty, and the path manipulations are skipped; however the import of `sitecustomize`is still attempted.
# `sndhdr` — Determine type of sound file.

*Determine type of a sound file.*\
The `sndhdr` provides utility functions which attempt to determine the type of sound data which is in a file. When these functions are able to determine what type of sound data is stored in a file, they return a tuple `(`*`type`*`, `*`sampling_rate`*`, `*`channels`*`, `*`frames`*`, `*`bits_per_sample`*`)`. The value for *type* indicates the data type and will be one of the strings `’aifc’`, `’aiff’`, `’au’`, `’hcom’`, `’sndr’`, `’sndt’`, `’voc’`, `’wav’`, `’8svx’`, `’sb’`, `’ub’`, or `’ul’`. The *sampling_rate* will be either the actual value or `0` if unknown or difficult to decode. Similarly, *channels* will be either the number of channels or `0` if it cannot be determined or if the value is difficult to decode. The value for *frames* will be either the number of frames or `-1`. The last item in the tuple, *bits_per_sample*, will either be the sample size in bits or `’A’` for A-LAWor `’U’` for u-LAW.

<div class="funcdesc">

whatfilename Determines the type of sound data stored in the file *filename* using `whathdr()`. If it succeeds, returns a tuple as described above, otherwise `None` is returned.

</div>

<div class="funcdesc">

whathdrfilename Determines the type of sound data stored in a file based on the file header. The name of the file is given by *filename*. This function returns a tuple as described above on success, or `None`.

</div>
# `SocketServer` — A framework for network servers.

*A framework for network servers.*\
The `SocketServer` module simplifies the task of writing network servers.

There are four basic server classes: `TCPServer` uses the Internet TCP protocol, which provides for continuous streams of data between the client and server. `UDPServer` uses datagrams, which are discrete packets of information that may arrive out of order or be lost while in transit. The more infrequently used `UnixStreamServer` and `UnixDatagramServer` classes are similar, but use Unix domain sockets; they’re not available on non-Unix platforms. For more details on network programming, consult a book such as W. Richard Steven’s UNIX Network Programming or Ralph Davis’s Win32 Network Programming.

These four classes process requests *synchronously*; each request must be completed before the next request can be started. This isn’t suitable if each request takes a long time to complete, because it requires a lot of computation, or because it returns a lot of data which the client is slow to process. The solution is to create a separate process or thread to handle each request; the `ForkingMixIn` and `ThreadingMixIn` mix-in classes can be used to support asynchronous behaviour.

Creating a server requires several steps. First, you must create a request handler class by subclassing the `BaseRequestHandler` class and overriding its `handle()` method; this method will process incoming requests. Second, you must instantiate one of the server classes, passing it the server’s address and the request handler class. Finally, call the `handle_request()` or `serve_forever()` method of the server object to process one or many requests.

Server classes have the same external methods and attributes, no matter what network protocol they use:

<div class="funcdesc">

fileno Return an integer file descriptor for the socket on which the server is listening. This function is most commonly passed to `select.select()`, to allow monitoring multiple servers in the same process.

</div>

<div class="funcdesc">

handle_request Process a single request. This function calls the following methods in order: `get_request()`, `verify_request()`, and `process_request()`. If the user-provided `handle()` method of the handler class raises an exception, the server’s `handle_error()` method will be called.

</div>

<div class="funcdesc">

serve_forever Handle an infinite number of requests. This simply calls `handle_request()` inside an infinite loop.

</div>

<div class="datadesc">

address_family The family of protocols to which the server’s socket belongs. and are two possible values.

</div>

<div class="datadesc">

RequestHandlerClass The user-provided request handler class; an instance of this class is created for each request.

</div>

<div class="datadesc">

server_address The address on which the server is listening. The format of addresses varies depending on the protocol family; see the documentation for the socket module for details. For Internet protocols, this is a tuple containing a string giving the address, and an integer port number: `(’127.0.0.1’, 80)`, for example.

</div>

<div class="datadesc">

socket The socket object on which the server will listen for incoming requests.

</div>

The server classes support the following class variables:

<div class="datadesc">

request_queue_size The size of the request queue. If it takes a long time to process a single request, any requests that arrive while the server is busy are placed into a queue, up to `request_queue_size` requests. Once the queue is full, further requests from clients will get a “Connection denied” error. The default value is usually 5, but this can be overridden by subclasses.

</div>

<div class="datadesc">

socket_type The type of socket used by the server; and are two possible values.

</div>

There are various server methods that can be overridden by subclasses of base server classes like `TCPServer`; these methods aren’t useful to external users of the server object.

<div class="funcdesc">

finish_request Actually processes the request by instantiating `RequestHandlerClass` and calling its `handle()` method.

</div>

<div class="funcdesc">

get_request Must accept a request from the socket, and return a 2-tuple containing the *new* socket object to be used to communicate with the client, and the client’s address.

</div>

<div class="funcdesc">

handle_errorrequest, client_address This function is called if the `RequestHandlerClass`’s `handle()` method raises an exception. The default action is to print the traceback to standard output and continue handling further requests.

</div>

<div class="funcdesc">

process_requestrequest, client_address Calls `finish_request()` to create an instance of the `RequestHandlerClass`. If desired, this function can create a new process or thread to handle the request; the `ForkingMixIn` and `ThreadingMixIn` classes do this.

</div>

<div class="funcdesc">

server_activate Called by the server’s constructor to activate the server. May be overridden.

</div>

<div class="funcdesc">

server_bind Called by the server’s constructor to bind the socket to the desired address. May be overridden.

</div>

<div class="funcdesc">

verify_requestrequest, client_address Must return a Boolean value; if the value is true, the request will be processed, and if it’s false, the request will be denied. This function can be overridden to implement access controls for a server. The default implementation always return true.

</div>

The request handler class must define a new `handle()` method, and can override any of the following methods. A new instance is created for each request.

<div class="funcdesc">

finish Called after the `handle()` method to perform any clean-up actions required. The default implementation does nothing. If `setup()` or `handle()` raise an exception, this function will not be called.

</div>

<div class="funcdesc">

handle This function must do all the work required to service a request. Several instance attributes are available to it; the request is available as `self.request`; the client address as `self.client_address`; and the server instance as `self.server`, in case it needs access to per-server information.

The type of `self.request` is different for datagram or stream services. For stream services, `self.request` is a socket object; for datagram services, `self.request` is a string. However, this can be hidden by using the mix-in request handler classes `StreamRequestHandler` or `DatagramRequestHandler`, which override the `setup()` and `finish()` methods, and provides `self.rfile` and `self.wfile` attributes. `self.rfile` and `self.wfile` can be read or written, respectively, to get the request data or return data to the client.

</div>

<div class="funcdesc">

setup Called before the `handle()` method to perform any initialization actions required. The default implementation does nothing.

</div>
# Optional Operating System Services

The modules described in this chapter provide interfaces to operating system features that are available on selected operating systems only. The interfaces are generally modeled after the Unix or C interfaces but they are available on some other systems as well (e.g. Windows or NT). Here’s an overview:
# `stat` — Interpreting `stat()` results

*Utilities for interpreting the results of `os.stat()`, `os.lstat()` and `os.fstat()`.*\
The `stat` module defines constants and functions for interpreting the results of `os.stat()`, `os.fstat()` and `os.lstat()` (if they exist). For complete details about the , and calls, consult the documentation for your system.

The `stat` module defines the following functions to test for specific file types:

<div class="funcdesc">

S_ISDIRmode Return non-zero if the mode is from a directory.

</div>

<div class="funcdesc">

S_ISCHRmode Return non-zero if the mode is from a character special device file.

</div>

<div class="funcdesc">

S_ISBLKmode Return non-zero if the mode is from a block special device file.

</div>

<div class="funcdesc">

S_ISREGmode Return non-zero if the mode is from a regular file.

</div>

<div class="funcdesc">

S_ISFIFOmode Return non-zero if the mode is from a FIFO (named pipe).

</div>

<div class="funcdesc">

S_ISLNKmode Return non-zero if the mode is from a symbolic link.

</div>

<div class="funcdesc">

S_ISSOCKmode Return non-zero if the mode is from a socket.

</div>

Two additional functions are defined for more general manipulation of the file’s mode:

<div class="funcdesc">

S_IMODEmode Return the portion of the file’s mode that can be set by `os.chmod()`—that is, the file’s permission bits, plus the sticky bit, set-group-id, and set-user-id bits (on systems that support them).

</div>

<div class="funcdesc">

S_IFMTmode Return the portion of the file’s mode that describes the file type (used by the `S_IS*()` functions above).

</div>

Normally, you would use the `os.path.is*()` functions for testing the type of a file; the functions here are useful when you are doing multiple tests of the same file and wish to avoid the overhead of the system call for each test. These are also useful when checking for information about a file that isn’t handled by `os.path`, like the tests for block and character devices.

All the variables below are simply symbolic indexes into the 10-tuple returned by `os.stat()`, `os.fstat()` or `os.lstat()`.

<div class="datadesc">

ST_MODE Inode protection mode.

</div>

<div class="datadesc">

ST_INO Inode number.

</div>

<div class="datadesc">

ST_DEV Device inode resides on.

</div>

<div class="datadesc">

ST_NLINK Number of links to the inode.

</div>

<div class="datadesc">

ST_UID User id of the owner.

</div>

<div class="datadesc">

ST_GID Group id of the owner.

</div>

<div class="datadesc">

ST_SIZE File size in bytes.

</div>

<div class="datadesc">

ST_ATIME Time of last access.

</div>

<div class="datadesc">

ST_MTIME Time of last modification.

</div>

<div class="datadesc">

ST_CTIME Time of last status change (see manual pages for details).

</div>

Example:

    import os, sys
    from stat import *

    def walktree(dir, callback):
        '''recursively descend the directory rooted at dir,
           calling the callback function for each regular file'''

        for f in os.listdir(dir):
            pathname = '%s/%s' % (dir, f)
            mode = os.stat(pathname)[ST_MODE]
            if S_ISDIR(mode):
                # It's a directory, recurse into it
                walktree(pathname, callback)
            elif S_ISREG(mode):
                # It's a file, call the callback function
                callback(pathname)
            else:
                # Unknown file type, print a message
                print 'Skipping %s' % pathname

    def visitfile(file):
        print 'visiting', file

    if __name__ == '__main__':
        walktree(sys.argv[1], visitfile)
# `statcache` — An optimization of `os.stat()`

*Stat files, and remember results.*\
The `statcache` module provides a simple optimization to `os.stat()`: remembering the values of previous invocations.

The `statcache` module defines the following functions:

<div class="funcdesc">

statpath This is the main module entry-point. Identical for `os.stat()`, except for remembering the result for future invocations of the function.

</div>

The rest of the functions are used to clear the cache, or parts of it.

<div class="funcdesc">

reset Clear the cache: forget all results of previous `stat()` calls.

</div>

<div class="funcdesc">

forgetpath Forget the result of `stat(`*`path`*`)`, if any.

</div>

<div class="funcdesc">

forget_prefixprefix Forget all results of `stat(`*`path`*`)` for *path* starting with *prefix*.

</div>

<div class="funcdesc">

forget_dirprefix Forget all results of `stat(`*`path`*`)` for *path* a file in the directory *prefix*, including `stat(`*`prefix`*`)`.

</div>

<div class="funcdesc">

forget_except_prefixprefix Similar to `forget_prefix()`, but for all *path* values *not* starting with *prefix*.

</div>

Example:

    >>> import os, statcache
    >>> statcache.stat('.')
    (16893, 2049, 772, 18, 1000, 1000, 2048, 929609777, 929609777, 929609777)
    >>> os.stat('.')
    (16893, 2049, 772, 18, 1000, 1000, 2048, 929609777, 929609777, 929609777)
# `statvfs` — Constants used with `os.statvfs()`

*Constants for interpreting the result of `os.statvfs()`.*\
The `statvfs` module defines constants so interpreting the result if `os.statvfs()`, which returns a tuple, can be made without remembering “magic numbers.” Each of the constants defined in this module is the *index* of the entry in the tuple returned by `os.statvfs()` that contains the specified information.

<div class="datadesc">

F_BSIZE Preferred file system block size.

</div>

<div class="datadesc">

F_FRSIZE Fundamental file system block size.

</div>

<div class="datadesc">

F_BLOCKS Total number of blocks in the filesystem.

</div>

<div class="datadesc">

F_BFREE Total number of free blocks.

</div>

<div class="datadesc">

F_BAVAIL Free blocks available to non-super user.

</div>

<div class="datadesc">

F_FILES Total number of file nodes.

</div>

<div class="datadesc">

F_FFREE Total number of free file nodes.

</div>

<div class="datadesc">

F_FAVAIL Free nodes available to non-super user.

</div>

<div class="datadesc">

F_FLAG Flags. System dependent: see man page.

</div>

<div class="datadesc">

F_NAMEMAX Maximum file name length.

</div>
# Built-in Types <span id="types" label="types"></span>

The following sections describe the standard types that are built into the interpreter. These are the numeric types, sequence types, and several others, including types themselves. There is no explicit Boolean type; use integers instead. Some operations are supported by several object types; in particular, all objects can be compared, tested for truth value, and converted to a string (with the `‘`<span class="roman">`…`</span>`‘` notation). The latter conversion is implicitly used when an object is written by the statement.

## Truth Value Testing <span id="truth" label="truth"></span>

Any object can be tested for truth value, for use in an or condition or as operand of the Boolean operations below. The following values are considered false:

- `None`

- zero of any numeric type, for example, `0`, `0L`, `0.0`, `0j`.

- any empty sequence, for example, `’’`, `()`, `[]`.

- any empty mapping, for example, `{}`.

- instances of user-defined classes, if the class defines a `__nonzero__()` or `__len__()` method, when that method returns zero.[^1]

All other values are considered true — so objects of many types are always true. Operations and built-in functions that have a Boolean result always return `0` for false and `1` for true, unless otherwise stated. (Important exception: the Boolean operations `or` and `and` always return one of their operands.)

## Boolean Operations <span id="boolean" label="boolean"></span>

These are the Boolean operations, ordered by ascending priority:

|                      |     |     |
|:---------------------|:----|:----|
| OperationResultNotes |     |     |
| or *y*               |     |     |
| and *y*              |     |     |
|                      |     |     |

Notes:

\(1\)  
These only evaluate their second argument if needed for their outcome.

\(2\)  
`not` has a lower priority than non-Boolean operators, so `not `*`a`*` == `*`b`* is interpreted as `not (`*`a`*` == `*`b`*`)`, and *`a`*` == not `*`b`* is a syntax error.

## Comparisons <span id="comparisons" label="comparisons"></span>

Comparison operations are supported by all objects. They all have the same priority (which is higher than that of the Boolean operations). Comparisons can be chained arbitrarily; for example, *`x`*` < `*`y`*` <= `*`z`* is equivalent to *`x`*` < `*`y`*` and `*`y`*` <= `*`z`*, except that *y* is evaluated only once (but in both cases *z* is not evaluated at all when *`x`*` < `*`y`* is found to be false). This table summarizes the comparison operations:

|                          |                         |       |
|:-------------------------|:------------------------|:------|
| OperationMeaningNotes \< | strictly less than      |       |
| \<=                      | less than or equal      |       |
| \>                       | strictly greater than   |       |
| \>=                      | greater than or equal   |       |
| ==                       | equal                   |       |
| !=                       | not equal               | \(1\) |
| \<\>                     | not equal               | \(1\) |
| is                       | object identity         |       |
| is not                   | negated object identity |       |
|                          |                         |       |

Notes:

\(1\)  
`<>` and `!=` are alternate spellings for the same operator. (I couldn’t choose between ABC and C! :-) `!=` is the preferred spelling; `<>` is obsolescent.

Objects of different types, except different numeric types, never compare equal; such objects are ordered consistently but arbitrarily (so that sorting a heterogeneous array yields a consistent result). Furthermore, some types (for example, file objects) support only a degenerate notion of comparison where any two objects of that type are unequal. Again, such objects are ordered arbitrarily but consistently. Instances of a class normally compare as non-equal unless the class defines the `__cmp__()` method. Refer to the Python Reference Manual for information on the use of this method to effect object comparisons.

**Implementation note:** Objects of different types except numbers are ordered by their type names; objects of the same types that don’t support proper comparison are ordered by their address.

Two more operations with the same syntactic priority, `in` and `not in`, are supported only by sequence types (below).

## Numeric Types <span id="typesnumeric" label="typesnumeric"></span>

There are four numeric types: *plain integers*, *long integers*, *floating point numbers*, and *complex numbers*. Plain integers (also just called *integers*) are implemented using `long` in C, which gives them at least 32 bits of precision. Long integers have unlimited precision. Floating point numbers are implemented using `double` in C. All bets on their precision are off unless you happen to know the machine you are working with. Complex numbers have a real and imaginary part, which are both implemented using `double` in C. To extract these parts from a complex number *z*, use *`z`*`.real` and *`z`*`.imag`.

Numbers are created by numeric literals or as the result of built-in functions and operators. Unadorned integer literals (including hex and octal numbers) yield plain integers. Integer literals with an or suffix yield long integers ( is preferred because `1l` looks too much like eleven!). Numeric literals containing a decimal point or an exponent sign yield floating point numbers. Appending or to a numeric literal yields a complex number. Python fully supports mixed arithmetic: when a binary arithmetic operator has operands of different numeric types, the operand with the “smaller” type is converted to that of the other, where plain integer is smaller than long integer is smaller than floating point is smaller than complex. Comparisons between numbers of mixed type use the same rule.[^2] The functions `int()`, `long()`, `float()`, and `complex()` can be used to coerce numbers to a specific type. All numeric types support the following operations, sorted by ascending priority (operations in the same box have the same priority; all numeric operations have a higher priority than comparison operations):

|                      |     |     |
|:---------------------|:----|:----|
| OperationResultNotes |     |     |
| \+ *y*               |     |     |
| \- *y*               |     |     |
| \* *y*               |     |     |
| / *y*                |     |     |
| % *y*                |     |     |
|                      |     |     |
|                      |     |     |
| )                    |     |     |
| )                    |     |     |
| )                    |     |     |
| )                    |     |     |
| ,*im*)               |     |     |
| .conjugate()         |     |     |
| , *y*)               |     |     |
| , *y*)               |     |     |
| \*\* *y*             |     |     |

Notes:

\(1\)  
For (plain or long) integer division, the result is an integer. The result is always rounded towards minus infinity: 1/2 is 0, (-1)/2 is -1, 1/(-2) is -1, and (-1)/(-2) is 0. Note that the result is a long integer if either operand is a long integer, regardless of the numeric value.

\(2\)  
Conversion from floating point to (long or plain) integer may round or truncate as in C; see functions `floor()` and `ceil()` in the `math`module for well-defined conversions.

\(3\)  
See section <a href="#built-in-funcs" data-reference-type="ref" data-reference="built-in-funcs">[built-in-funcs]</a>, “Built-in Functions,” for a full description.

### Bit-string Operations on Integer Types <span id="bitstring-ops" label="bitstring-ops"></span>

Plain and long integer types support additional operations that make sense only for bit-strings. Negative numbers are treated as their 2’s complement value (for long integers, this assumes a sufficiently large number of bits that no overflow occurs during the operation).

The priorities of the binary bit-wise operations are all lower than the numeric operations and higher than the comparisons; the unary operation `~` has the same priority as the other unary numeric operations (`+` and `-`).

This table lists the bit-string operations sorted in ascending priority (operations in the same box have the same priority):

|                      |     |     |
|:---------------------|:----|:----|
| OperationResultNotes |     |     |
| \| *y*               |     |     |
| ^ *y*                |     |     |
| & *y*                |     |     |
| \<\< *n*             |     |     |
| \>\> *n*             |     |     |
|                      |     |     |

Notes:

\(1\)  
Negative shift counts are illegal and cause a `ValueError` to be raised.

\(2\)  
A left shift by *n* bits is equivalent to multiplication by `pow(2, `*`n`*`)` without overflow check.

\(3\)  
A right shift by *n* bits is equivalent to division by `pow(2, `*`n`*`)` without overflow check.

## Sequence Types <span id="typesseq" label="typesseq"></span>

There are six sequence types: strings, Unicode strings, lists, tuples, buffers, and xrange objects.

Strings literals are written in single or double quotes: `’xyzzy’`, `"frobozz"`. See chapter 2 of the Python Reference Manual for more about string literals. Unicode strings are much like strings, but are specified in the syntax using a preceeding character: `u’abc’`, `u"def"`. Lists are constructed with square brackets, separating items with commas: `[a, b, c]`. Tuples are constructed by the comma operator (not within square brackets), with or without enclosing parentheses, but an empty tuple must have the enclosing parentheses, e.g., `a, b, c` or `()`. A single item tuple must have a trailing comma, e.g., `(d,)`. Buffers are not directly supported by Python syntax, but can be created by calling the builtin function `buffer()`.XRanges objects are similar to buffers in that there is no specific syntax to create them, but they are created using the `xrange()` function.Sequence types support the following operations. The `in` and `not in` operations have the same priorities as the comparison operations. The `+` and `*` operations have the same priority as the corresponding numeric operations.[^3]

This table lists the sequence operations sorted in ascending priority (operations in the same box have the same priority). In the table, *s* and *t* are sequences of the same type; *n*, *i* and *j* are integers:

|                                               |     |     |
|:----------------------------------------------|:----|:----|
| OperationResultNotes                          |     |     |
| in *s*                                        |     |     |
| not in *s*                                    |     |     |
| \+ *t*                                        |     |     |
| \* *n*<span class="roman">,</span> *n* \* *s* |     |     |
|                                               |     |     |
|                                               |     |     |
| )                                             |     |     |
| )                                             |     |     |
| )                                             |     |     |

Notes:

\(1\)  
Values of *n* less than `0` are treated as `0` (which yields an empty sequence of the same type as *s*).

\(2\)  
If *i* or *j* is negative, the index is relative to the end of the string, i.e., `len(`*`s`*`) + `*`i`* or `len(`*`s`*`) + `*`j`* is substituted. But note that `-0` is still `0`.

\(3\)  
The slice of *s* from *i* to *j* is defined as the sequence of items with index *k* such that *`i`*` <= `*`k`*` < `*`j`*. If *i* or *j* is greater than `len(`*`s`*`)`, use `len(`*`s`*`)`. If *i* is omitted, use `0`. If *j* is omitted, use `len(`*`s`*`)`. If *i* is greater than or equal to *j*, the slice is empty.

### String Methods <span id="string-methods" label="string-methods"></span>

These are the string methods which both 8-bit strings and Unicode objects support:

<div class="methoddesc">

capitalize Return a copy of the string with only its first character capitalized.

</div>

<div class="methoddesc">

centerwidth Return centered in a string of length *width*. Padding is done using spaces.

</div>

<div class="methoddesc">

countsub Return the number of occurrences of substring *sub* in string S`[`*`start`*`:`*`end`*`]`. Optional arguments *start* and *end* are interpreted as in slice notation.

</div>

<div class="methoddesc">

encode Return an encoded version of the string. Default encoding is the current default string encoding. *errors* may be given to set a different error handling scheme. The default for *errors* is `’strict’`, meaning that encoding errors raise a `ValueError`. Other possible values are `’ignore’` and `’replace’`.

</div>

<div class="methoddesc">

endswithsuffix Return true if the string ends with the specified *suffix*, otherwise return false. With optional *start*, test beginning at that position. With optional *end*, stop comparing at that position.

</div>

<div class="methoddesc">

expandtabs Return a copy of the string where all tab characters are expanded using spaces. If *tabsize* is not given, a tab size of `8` characters is assumed.

</div>

<div class="methoddesc">

findsub Return the lowest index in the string where substring *sub* is found, such that *sub* is contained in the range \[*start*, *end*). Optional arguments *start* and *end* are interpreted as in slice notation. Return `-1` if *sub* is not found.

</div>

<div class="methoddesc">

indexsub Like `find()`, but raise `ValueError` when the substring is not found.

</div>

<div class="methoddesc">

isalnum Return true if all characters in the string are alphanumeric and there is at least one character, false otherwise.

</div>

<div class="methoddesc">

isalpha Return true if all characters in the string are alphabetic and there is at least one character, false otherwise.

</div>

<div class="methoddesc">

isdigit Return true if there are only digit characters, false otherwise.

</div>

<div class="methoddesc">

islower Return true if all cased characters in the string are lowercase and there is at least one cased character, false otherwise.

</div>

<div class="methoddesc">

isspace Return true if there are only whitespace characters in the string and the string is not empty, false otherwise.

</div>

<div class="methoddesc">

istitle Return true if the string is a titlecased string, i.e. uppercase characters may only follow uncased characters and lowercase characters only cased ones. Return false otherwise.

</div>

<div class="methoddesc">

isupper Return true if all cased characters in the string are uppercase and there is at least one cased character, false otherwise.

</div>

<div class="methoddesc">

joinseq Return a string which is the concatenation of the strings in the sequence *seq*. The separator between elements is the string providing this method.

</div>

<div class="methoddesc">

ljustwidth Return the string left justified in a string of length *width*. Padding is done using spaces. The original string is returned if *width* is less than `len(`*`s`*`)`.

</div>

<div class="methoddesc">

lower Return a copy of the string converted to lowercase.

</div>

<div class="methoddesc">

lstrip Return a copy of the string with leading whitespace removed.

</div>

<div class="methoddesc">

replaceold, new Return a copy of the string with all occurrences of substring *old* replaced by *new*. If the optional argument *maxsplit* is given, only the first *maxsplit* occurrences are replaced.

</div>

<div class="methoddesc">

rfindsub Return the highest index in the string where substring *sub* is found, such that *sub* is contained within s\[start,end\]. Optional arguments *start* and *end* are interpreted as in slice notation. Return `-1` on failure.

</div>

<div class="methoddesc">

rindexsub Like `rfind()` but raises `ValueError` when the substring *sub* is not found.

</div>

<div class="methoddesc">

rjustwidth Return the string right justified in a string of length *width*. Padding is done using spaces. The original string is returned if *width* is less than `len(`*`s`*`)`.

</div>

<div class="methoddesc">

rstrip Return a copy of the string with trailing whitespace removed.

</div>

<div class="methoddesc">

split Return a list of the words in the string, using *sep* as the delimiter string. If *maxsplit* is given, at most *maxsplit* splits are done. If *sep* is not specified or `None`, any whitespace string is a separator.

</div>

<div class="methoddesc">

splitlines Return a list of the lines in the string, breaking at line boundaries. Line breaks are not included in the resulting list unless *keepends* is given and true.

</div>

<div class="methoddesc">

startswithprefix Return true if string starts with the *prefix*, otherwise return false. With optional *start*, test string beginning at that position. With optional *end*, stop comparing string at that position.

</div>

<div class="methoddesc">

strip Return a copy of the string with leading and trailing whitespace removed.

</div>

<div class="methoddesc">

swapcase Return a copy of the string with uppercase characters converted to lowercase and vice versa.

</div>

<div class="methoddesc">

title Return a titlecased version of, i.e. words start with uppercase characters, all remaining cased characters are lowercase.

</div>

<div class="methoddesc">

translatetable Return a copy of the string where all characters occurring in the optional argument *deletechars* are removed, and the remaining characters have been mapped through the given translation table, which must be a string of length 256.

</div>

<div class="methoddesc">

upper Return a copy of the string converted to uppercase.

</div>

### String Formatting Operations <span id="typesseq-strings" label="typesseq-strings"></span>

String objects have one unique built-in operation: the `%` operator (modulo) with a string left argument interprets this string as a C format string to be applied to the right argument, and returns the string resulting from this formatting operation.

The right argument should be a tuple with one item for each argument required by the format string; if the string requires a single argument, the right argument may also be a single non-tuple object.[^4] The following format characters are understood: `%`, `c`, `s`, `i`, `d`, `u`, `o`, `x`, `X`, `e`, `E`, `f`, `g`, `G`. Width and precision may be a `*` to specify that an integer argument specifies the actual width or precision. The flag characters `-`, `+`, blank, `#` and `0` are understood. The size specifiers `h`, `l` or `L` may be present but are ignored. The `%s` conversion takes any Python object and converts it to a string using `str()` before formatting it. The ANSI features `%p` and `%n` are not supported. Since Python strings have an explicit length, `%s` conversions don’t assume that `’’` is the end of the string.

For safety reasons, floating point precisions are clipped to 50; `%f` conversions for numbers whose absolute value is over 1e25 are replaced by `%g` conversions.[^5] All other errors raise exceptions.

If the right argument is a dictionary (or any kind of mapping), then the formats in the string must have a parenthesized key into that dictionary inserted immediately after the character, and each format formats the corresponding entry from the mapping. For example:

    >>> count = 2
    >>> language = 'Python'
    >>> print '%(language)s has %(count)03d quote types.' % vars()
    Python has 002 quote types.

In this case no `*` specifiers may occur in a format (since they require a sequential parameter list).

Additional string operations are defined in standard module `string` and in built-in module `re`.

### XRange Type <span id="typesseq-xrange" label="typesseq-xrange"></span>

The xrangetype is an immutable sequence which is commonly used for looping. The advantage of the xrange type is that an xrange object will always take the same amount of memory, no matter the size of the range it represents. There are no consistent performance advantages.

XRange objects behave like tuples, and offer a single method:

<div class="methoddesc">

tolist Return a list object which represents the same values as the xrange object.

</div>

### Mutable Sequence Types <span id="typesseq-mutable" label="typesseq-mutable"></span>

List objects support additional operations that allow in-place modification of the object. These operations would be supported by other mutable sequence types (when added to the language) as well. Strings and tuples are immutable sequence types and such objects cannot be modified once created. The following operations are defined on mutable sequence types (where *x* is an arbitrary object):

|                      |     |     |
|:---------------------|:----|:----|
| OperationResultNotes |     |     |
| = *x*                |     |     |
| = *t*                |     |     |
|                      |     |     |
| .append(*x*)         |     |     |
| .extend(*x*)         |     |     |
| .count(*x*)          |     |     |
| .index(*x*)          |     |     |
| .insert(*i*, *x*)    |     |     |
| .pop()               |     |     |
| .remove(*x*)         |     |     |
| .reverse()           |     |     |
| .sort()              |     |     |

Notes:

\(1\)  
The C implementation of Python has historically accepted multiple parameters and implicitly joined them into a tuple; this no longer works in Python 2.0. Use of this misfeature has been deprecated since Python 1.4.

\(2\)  
Raises an exception when *x* is not a list object. The `extend()` method is experimental and not supported by mutable sequence types other than lists.

\(3\)  
Raises `ValueError` when *x* is not found in *s*.

\(4\)  
The `pop()` method is only supported by the list and array types. The optional argument *i* defaults to `-1`, so that by default the last item is removed and returned.

\(5\)  
The `sort()` and `reverse()` methods modify the list in place for economy of space when sorting or reversing a large list. They don’t return the sorted or reversed list to remind you of this side effect.

\(6\)  
The `sort()` method takes an optional argument specifying a comparison function of two arguments (list items) which should return `-1`, `0` or `1` depending on whether the first argument is considered smaller than, equal to, or larger than the second argument. Note that this slows the sorting process down considerably; e.g. to sort a list in reverse order it is much faster to use calls to the methods `sort()` and `reverse()` than to use the built-in function `sort()` with a comparison function that reverses the ordering of the elements.

## Mapping Types <span id="typesmapping" label="typesmapping"></span>

A *mapping* object maps values of one type (the key type) to arbitrary objects. Mappings are mutable objects. There is currently only one standard mapping type, the *dictionary*. A dictionary’s keys are almost arbitrary values. The only types of values not acceptable as keys are values containing lists or dictionaries or other mutable types that are compared by value rather than by object identity. Numeric types used for keys obey the normal rules for numeric comparison: if two numbers compare equal (e.g. `1` and `1.0`) then they can be used interchangeably to index the same dictionary entry.

Dictionaries are created by placing a comma-separated list of *`key`*`: `*`value`* pairs within braces, for example: `{’jack’: 4098, ’sjoerd’: 4127}` or `{4098: ’jack’, 4127: ’sjoerd’}`.

The following operations are defined on mappings (where *a* and *b* are mappings, *k* is a key, and *v* and *x* are arbitrary objects):

|                           |     |     |
|:--------------------------|:----|:----|
| OperationResultNotes len( |     |     |
| )                         |     |     |
|                           |     |     |
| = *v*                     |     |     |
|                           |     |     |
| .clear()                  |     |     |
| .copy()                   |     |     |
| .has_key(*k*)             |     |     |
| .items()                  |     |     |
| .keys()                   |     |     |
| .update(*b*)              |     |     |
| .values()                 |     |     |
| .get(*k*)                 |     |     |
| .setdefault(*k*)          |     |     |

Notes:

\(1\)  
Raises a `KeyError` exception if *k* is not in the map.

\(2\)  
Keys and values are listed in random order. If `keys()` and `values()` are called with no intervening modifications to the dictionary, the two lists will directly correspond. This allows the creation of `(`*`value`*`, `*`key`*`)` pairs using `map()`: `pairs = map(None, `*`a`*`.values(), `*`a`*`.keys())`.

\(3\)  
*b* must be of the same type as *a*.

\(4\)  
Never raises an exception if *k* is not in the map, instead it returns *x*. *x* is optional; when *x* is not provided and *k* is not in the map, `None` is returned.

\(5\)  
`setdefault()` is like `get()`, except that if *k* is missing, *x* is both returned and inserted into the dictionary as the value of *k*.

## Other Built-in Types <span id="typesother" label="typesother"></span>

The interpreter supports several other kinds of objects. Most of these support only one or two operations.

### Modules <span id="typesmodules" label="typesmodules"></span>

The only special operation on a module is attribute access: *`m`*`.`*`name`*, where *m* is a module and *name* accesses a name defined in *m*’s symbol table. Module attributes can be assigned to. (Note that the statement is not, strictly speaking, an operation on a module object; `import `*`foo`* does not require a module object named *foo* to exist, rather it requires an (external) *definition* for a module named *foo* somewhere.)

A special member of every module is `__dict__`. This is the dictionary containing the module’s symbol table. Modifying this dictionary will actually change the module’s symbol table, but direct assignment to the `__dict__` attribute is not possible (i.e., you can write *`m`*`.__dict__[’a’] = 1`, which defines *`m`*`.a` to be `1`, but you can’t write *`m`*`.__dict__ = {}`.

Modules built into the interpreter are written like this: `<module ’sys’ (built-in)>`. If loaded from a file, they are written as `<module ’os’ from ’/usr/local/lib/python/os.pyc’>`.

### Classes and Class Instances <span id="typesobjects" label="typesobjects"></span>

See chapters 3 and 7 of the Python Reference Manual for these.

### Functions <span id="typesfunctions" label="typesfunctions"></span>

Function objects are created by function definitions. The only operation on a function object is to call it: *`func`*`(`*`argument-list`*`)`.

There are really two flavors of function objects: built-in functions and user-defined functions. Both support the same operation (to call the function), but the implementation is different, hence the different object types.

The implementation adds two special read-only attributes: *`f`*`.func_code` is a function’s *code object*(see below) and *`f`*`.func_globals` is the dictionary used as the function’s global namespace (this is the same as *`m`*`.__dict__` where *m* is the module in which the function *f* was defined).

### Methods <span id="typesmethods" label="typesmethods"></span>

Methods are functions that are called using the attribute notation. There are two flavors: built-in methods (such as `append()` on lists) and class instance methods. Built-in methods are described with the types that support them.

The implementation adds two special read-only attributes to class instance methods: *`m`*`.im_self` is the object on which the method operates, and *`m`*`.im_func` is the function implementing the method. Calling *`m`*`(`*`arg-1`*`, `*`arg-2`*`, `<span class="roman">`…`</span>`, `*`arg-n`*`)` is completely equivalent to calling *`m`*`.im_func(`*`m`*`.im_self, `*`arg-1`*`, `*`arg-2`*`, `<span class="roman">`…`</span>`, `*`arg-n`*`)`.

See the Python Reference Manual for more information.

### Code Objects <span id="bltin-code-objects" label="bltin-code-objects"></span>

Code objects are used by the implementation to represent “pseudo-compiled” executable Python code such as a function body. They differ from function objects because they don’t contain a reference to their global execution environment. Code objects are returned by the built-in `compile()` function and can be extracted from function objects through their `func_code` attribute. A code object can be executed or evaluated by passing it (instead of a source string) to the statement or the built-in `eval()` function. See the Python Reference Manual for more information.

### Type Objects <span id="bltin-type-objects" label="bltin-type-objects"></span>

Type objects represent the various object types. An object’s type is accessed by the built-in function `type()`. There are no special operations on types. The standard module `types` defines names for all standard built-in types. Types are written like this: `<type ’int’>`.

### The Null Object <span id="bltin-null-object" label="bltin-null-object"></span>

This object is returned by functions that don’t explicitly return a value. It supports no special operations. There is exactly one null object, named `None` (a built-in name).

It is written as `None`.

### The Ellipsis Object <span id="bltin-ellipsis-object" label="bltin-ellipsis-object"></span>

This object is used by extended slice notation (see the Python Reference Manual). It supports no special operations. There is exactly one ellipsis object, named (a built-in name).

It is written as `Ellipsis`.

### File Objects<span id="bltin-file-objects" label="bltin-file-objects"></span>

File objects are implemented using C’s `stdio` package and can be created with the built-in function `open()`described in section <a href="#built-in-funcs" data-reference-type="ref" data-reference="built-in-funcs">[built-in-funcs]</a>, “Built-in Functions.” They are also returned by some other built-in functions and methods, e.g., `os.popen()` and `os.fdopen()` and the `makefile()` method of socket objects. When a file operation fails for an I/O-related reason, the exception `IOError` is raised. This includes situations where the operation is not defined for some reason, like `seek()` on a tty device or writing a file opened for reading.

Files have the following methods:

<div class="methoddesc">

close Close the file. A closed file cannot be read or written anymore. Any operation which requires that the file be open will raise an `IOError` after the file has been closed. Calling `close()` more than once is allowed.

</div>

<div class="methoddesc">

flush Flush the internal buffer, like `stdio`’s . This may be a no-op on some file-like objects.

</div>

<div class="methoddesc">

isatty Return true if the file is connected to a tty(-like) device, else false. **Note:** If a file-like object is not associated with a real file, this method should *not* be implemented.

</div>

<div class="methoddesc">

fileno Return the integer “file descriptor” that is used by the underlying implementation to request I/O operations from the operating system. This can be useful for other, lower level interfaces that use file descriptors, e.g. module `fcntl`or `os.read()` and friends. **Note:** File-like objects which do not have a real file descriptor should *not* provide this method!

</div>

<div class="methoddesc">

read Read at most *size* bytes from the file (less if the read hits EOF before obtaining *size* bytes). If the *size* argument is negative or omitted, read all data until EOF is reached. The bytes are returned as a string object. An empty string is returned when EOF is encountered immediately. (For certain files, like ttys, it makes sense to continue reading after an EOF is hit.) Note that this method may call the underlying C function more than once in an effort to acquire as close to *size* bytes as possible.

</div>

<div class="methoddesc">

readline Read one entire line from the file. A trailing newline character is kept in the string[^6] (but may be absent when a file ends with an incomplete line). If the *size* argument is present and non-negative, it is a maximum byte count (including the trailing newline) and an incomplete line may be returned. An empty string is returned when EOF is hit immediately. Note: Unlike `stdio`’s , the returned string contains null characters (`’’`) if they occurred in the input.

</div>

<div class="methoddesc">

readlines Read until EOF using `readline()` and return a list containing the lines thus read. If the optional *sizehint* argument is present, instead of reading up to EOF, whole lines totalling approximately *sizehint* bytes (possibly after rounding up to an internal buffer size) are read. Objects implementing a file-like interface may choose to ignore *sizehint* if it cannot be implemented, or cannot be implemented efficiently.

</div>

<div class="methoddesc">

seekoffset Set the file’s current position, like `stdio`’s . The *whence* argument is optional and defaults to `0` (absolute file positioning); other values are `1` (seek relative to the current position) and `2` (seek relative to the file’s end). There is no return value.

</div>

<div class="methoddesc">

tell Return the file’s current position, like `stdio`’s .

</div>

<div class="methoddesc">

truncate Truncate the file’s size. If the optional *size* argument present, the file is truncated to (at most) that size. The size defaults to the current position. Availability of this function depends on the operating system version (for example, not all Unix versions support this operation).

</div>

<div class="methoddesc">

writestr Write a string to the file. There is no return value. Note: Due to buffering, the string may not actually show up in the file until the `flush()` or `close()` method is called.

</div>

<div class="methoddesc">

writelineslist Write a list of strings to the file. There is no return value. (The name is intended to match `readlines()`; `writelines()` does not add line separators.)

</div>

File objects also offer a number of other interesting attributes. These are not required for file-like objects, but should be implemented if they make sense for the particular object.

<div class="memberdesc">

closed Boolean indicating the current state of the file object. This is a read-only attribute; the `close()` method changes the value. It may not be available on all file-like objects.

</div>

<div class="memberdesc">

mode The I/O mode for the file. If the file was created using the `open()` built-in function, this will be the value of the *mode* parameter. This is a read-only attribute and may not be present on all file-like objects.

</div>

<div class="memberdesc">

name If the file object was created using `open()`, the name of the file. Otherwise, some string that indicates the source of the file object, of the form `<…>`. This is a read-only attribute and may not be present on all file-like objects.

</div>

<div class="memberdesc">

softspace Boolean that indicates whether a space character needs to be printed before another value when using the statement. Classes that are trying to simulate a file object should also have a writable `softspace` attribute, which should be initialized to zero. This will be automatic for most classes implemented in Python (care may be needed for objects that override attribute access); types implemented in C will have to provide a writable `softspace` attribute. **Note:** This attribute is not used to control the statement, but to allow the implementation of to keep track of its internal state.

</div>

### Internal Objects <span id="typesinternal" label="typesinternal"></span>

See the Python Reference Manual for this information. It describes stack frame objects, traceback objects, and slice objects.

## Special Attributes <span id="specialattrs" label="specialattrs"></span>

The implementation adds a few special read-only attributes to several object types, where they are relevant:

<div class="memberdescni">

\_\_dict\_\_ A dictionary of some sort used to store an object’s (writable) attributes.

</div>

<div class="memberdescni">

\_\_methods\_\_ List of the methods of many built-in object types, e.g., `[].__methods__` yields `[’append’, ’count’, ’index’, ’insert’, ’pop’, ’remove’, ’reverse’, ’sort’]`.

</div>

<div class="memberdescni">

\_\_members\_\_ Similar to `__methods__`, but lists data attributes.

</div>

<div class="memberdescni">

\_\_class\_\_ The class to which a class instance belongs.

</div>

<div class="memberdescni">

\_\_bases\_\_ The tuple of base classes of a class object.

</div>

[^1]: Additional information on these special methods may be found in the Python Reference Manual.

[^2]: As a consequence, the list `[1, 2]` is considered equal to `[1.0, 2.0]`, and similar for tuples.

[^3]: They must have since the parser can’t tell the type of the operands.

[^4]: A tuple object in this case should be a singleton.

[^5]: These numbers are fairly arbitrary. They are intended to avoid printing endless strings of meaningless digits without hampering correct use and without having to know the exact precision of floating point values on a particular machine.

[^6]: The advantage of leaving the newline on is that an empty string can be returned to mean EOF without being ambiguous. Another advantage is that (in cases where it might matter, e.g. if you want to make an exact copy of a file while scanning its lines) you can tell whether the last line of a file ended in a newline or not (yes this happens!).
# Standard Windowing Interface

The modules in this chapter are available only on those systems where the STDWIN library is available. STDWIN runs on Unix under X11 and on the Macintosh. See CWI report CS-R8817.

**Warning:** Using STDWIN is not recommended for new applications. It has never been ported to Microsoft Windows or Windows NT, and for X11 or the Macintosh it lacks important functionality — in particular, it has no tools for the construction of dialogs. For most platforms, alternative, native solutions exist (though none are currently documented in this manual): Tkinter for Unix under X11, native Xt with Motif or Athena widgets for Unix under X11, Win32 for Windows and Windows NT, and a collection of native toolkit interfaces for the Macintosh.

## `stdwin` — Platform-independent GUI System

*Older GUI system for X11 and Macintosh.*\
This module defines several new object types and functions that provide access to the functionality of STDWIN.

On Unix running X11, it can only be used if the environment variable is set or an explicit `-display` *displayname* argument is passed to the Python interpreter.

Functions have names that usually resemble their C STDWIN counterparts with the initial ‘w’ dropped. Points are represented by pairs of integers; rectangles by pairs of points. For a complete description of STDWIN please refer to the documentation of STDWIN for C programmers (aforementioned CWI report).

### Functions Defined in Module `stdwin`

The following functions are defined in the `stdwin` module:

<div class="funcdesc">

opentitle Open a new window whose initial title is given by the string argument. Return a window object; window object methods are described below.[^1]

</div>

<div class="funcdesc">

getevent Wait for and return the next event. An event is returned as a triple: the first element is the event type, a small integer; the second element is the window object to which the event applies, or `None` if it applies to no window in particular; the third element is type-dependent. Names for event types and command codes are defined in the standard module `stdwinevents`.

</div>

<div class="funcdesc">

pollevent Return the next event, if one is immediately available. If no event is available, return `()`.

</div>

<div class="funcdesc">

getactive Return the window that is currently active, or `None` if no window is currently active. (This can be emulated by monitoring WE_ACTIVATE and WE_DEACTIVATE events.)

</div>

<div class="funcdesc">

listfontnamespattern Return the list of font names in the system that match the pattern (a string). The pattern should normally be `’*’`; returns all available fonts. If the underlying window system is X11, other patterns follow the standard X11 font selection syntax (as used e.g. in resource definitions), i.e. the wildcard character `’*’` matches any sequence of characters (including none) and `’?’` matches any single character. On the Macintosh this function currently returns an empty list.

</div>

<div class="funcdesc">

setdefscrollbarshflag, vflag Set the flags controlling whether subsequently opened windows will have horizontal and/or vertical scroll bars.

</div>

<div class="funcdesc">

setdefwinposh, v Set the default window position for windows opened subsequently.

</div>

<div class="funcdesc">

setdefwinsizewidth, height Set the default window size for windows opened subsequently.

</div>

<div class="funcdesc">

getdefscrollbars Return the flags controlling whether subsequently opened windows will have horizontal and/or vertical scroll bars.

</div>

<div class="funcdesc">

getdefwinpos Return the default window position for windows opened subsequently.

</div>

<div class="funcdesc">

getdefwinsize Return the default window size for windows opened subsequently.

</div>

<div class="funcdesc">

getscrsize Return the screen size in pixels.

</div>

<div class="funcdesc">

getscrmm Return the screen size in millimeters.

</div>

<div class="funcdesc">

fetchcolorcolorname Return the pixel value corresponding to the given color name. Return the default foreground color for unknown color names. Hint: the following code tests whether you are on a machine that supports more than two colors:

    if stdwin.fetchcolor('black') <> \
              stdwin.fetchcolor('red') <> \
              stdwin.fetchcolor('white'):
        print 'color machine'
    else:
        print 'monochrome machine'

</div>

<div class="funcdesc">

setfgcolorpixel Set the default foreground color. This will become the default foreground color of windows opened subsequently, including dialogs.

</div>

<div class="funcdesc">

setbgcolorpixel Set the default background color. This will become the default background color of windows opened subsequently, including dialogs.

</div>

<div class="funcdesc">

getfgcolor Return the pixel value of the current default foreground color.

</div>

<div class="funcdesc">

getbgcolor Return the pixel value of the current default background color.

</div>

<div class="funcdesc">

setfontfontname Set the current default font. This will become the default font for windows opened subsequently, and is also used by the text measuring functions `textwidth()`, `textbreak()`, `lineheight()` and `baseline()` below. This accepts two more optional parameters, size and style: Size is the font size (in ‘points’). Style is a single character specifying the style, as follows: `’b’` = bold, `’i’` = italic, `’o’` = bold + italic, `’u’` = underline; default style is roman. Size and style are ignored under X11 but used on the Macintosh. (Sorry for all this complexity — a more uniform interface is being designed.)

</div>

<div class="funcdesc">

menucreatetitle Create a menu object referring to a global menu (a menu that appears in all windows). Methods of menu objects are described below. Note: normally, menus are created locally; see the window method `menucreate()` below. **Warning:** the menu only appears in a window as long as the object returned by this call exists.

</div>

<div class="funcdesc">

newbitmapwidth, height Create a new bitmap object of the given dimensions. Methods of bitmap objects are described below. Not available on the Macintosh.

</div>

<div class="funcdesc">

fleep Cause a beep or bell (or perhaps a ‘visual bell’ or flash, hence the name).

</div>

<div class="funcdesc">

messagestring Display a dialog box containing the string. The user must click OK before the function returns.

</div>

<div class="funcdesc">

askyncprompt, default Display a dialog that prompts the user to answer a question with yes or no. Return 0 for no, 1 for yes. If the user hits the Return key, the default (which must be 0 or 1) is returned. If the user cancels the dialog, `KeyboardInterrupt` is raised.

</div>

<div class="funcdesc">

askstrprompt, default Display a dialog that prompts the user for a string. If the user hits the Return key, the default string is returned. If the user cancels the dialog, `KeyboardInterrupt` is raised.

</div>

<div class="funcdesc">

askfileprompt, default, new Ask the user to specify a filename. If *new* is zero it must be an existing file; otherwise, it must be a new file. If the user cancels the dialog, `KeyboardInterrupt` is raised.

</div>

<div class="funcdesc">

setcutbufferi, string Store the string in the system’s cut buffer number *i*, where it can be found (for pasting) by other applications. On X11, there are 8 cut buffers (numbered 0..7). Cut buffer number 0 is the ‘clipboard’ on the Macintosh.

</div>

<div class="funcdesc">

getcutbufferi Return the contents of the system’s cut buffer number *i*.

</div>

<div class="funcdesc">

rotatecutbuffersn On X11, rotate the 8 cut buffers by *n*. Ignored on the Macintosh.

</div>

<div class="funcdesc">

getselectioni Return X11 selection number *i.* Selections are not cut buffers. Selection numbers are defined in module `stdwinevents`. Selection is the *primary* selection (used by , for instance); selection is the *secondary* selection; selection is the *clipboard* selection (used by ). On the Macintosh, this always returns an empty string.

</div>

<div class="funcdesc">

resetselectioni Reset selection number *i*, if this process owns it. (See window method `setselection()`).

</div>

<div class="funcdesc">

baseline Return the baseline of the current font (defined by STDWIN as the vertical distance between the baseline and the top of the characters).

</div>

<div class="funcdesc">

lineheight Return the total line height of the current font.

</div>

<div class="funcdesc">

textbreakstr, width Return the number of characters of the string that fit into a space of *width* bits wide when drawn in the current font.

</div>

<div class="funcdesc">

textwidthstr Return the width in bits of the string when drawn in the current font.

</div>

<div class="funcdesc">

connectionnumber (X11 under Unix only) Return the “connection number” used by the underlying X11 implementation. (This is normally the file number of the socket.) Both functions return the same value; `connectionnumber()` is named after the corresponding function in X11 and STDWIN, while `fileno()` makes it possible to use the `stdwin` module as a “file” object parameter to `select.select()`. Note that if implies that input is possible on `stdwin`, this does not guarantee that an event is ready — it may be some internal communication going on between the X server and the client library. Thus, you should call `stdwin.pollevent()` until it returns `None` to check for events if you don’t want your program to block. Because of internal buffering in X11, it is also possible that `stdwin.pollevent()` returns an event while `select()` does not find `stdwin` to be ready, so you should read any pending events with `stdwin.pollevent()` until it returns `None` before entering a blocking `select()` call.

</div>

### Window Objects

Window objects are created by `stdwin.open()`. They are closed by their `close()` method or when they are garbage-collected. Window objects have the following methods:

<div class="methoddesc">

begindrawing Return a drawing object, whose methods (described below) allow drawing in the window.

</div>

<div class="methoddesc">

changerect Invalidate the given rectangle; this may cause a draw event.

</div>

<div class="methoddesc">

gettitle Returns the window’s title string.

</div>

<div class="methoddesc">

getdocsize

Return a pair of integers giving the size of the document as set by `setdocsize()`.

</div>

<div class="methoddesc">

getorigin Return a pair of integers giving the origin of the window with respect to the document.

</div>

<div class="methoddesc">

gettitle Return the window’s title string.

</div>

<div class="methoddesc">

getwinsize Return a pair of integers giving the size of the window.

</div>

<div class="methoddesc">

getwinpos Return a pair of integers giving the position of the window’s upper left corner (relative to the upper left corner of the screen).

</div>

<div class="methoddesc">

menucreatetitle Create a menu object referring to a local menu (a menu that appears only in this window). Methods of menu objects are described below. **Warning:** the menu only appears as long as the object returned by this call exists.

</div>

<div class="methoddesc">

scrollrect, point Scroll the given rectangle by the vector given by the point.

</div>

<div class="methoddesc">

setdocsizepoint Set the size of the drawing document.

</div>

<div class="methoddesc">

setoriginpoint Move the origin of the window (its upper left corner) to the given point in the document.

</div>

<div class="methoddesc">

setselectioni, str Attempt to set X11 selection number *i* to the string *str*. (See `stdwin` function `getselection()` for the meaning of *i*.) Return true if it succeeds. If succeeds, the window “owns” the selection until (a) another application takes ownership of the selection; or (b) the window is deleted; or (c) the application clears ownership by calling `stdwin.resetselection(`*`i`*`)`. When another application takes ownership of the selection, a event is received for no particular window and with the selection number as detail. Ignored on the Macintosh.

</div>

<div class="methoddesc">

settimerdsecs Schedule a timer event for the window in *`dsecs`*`/10` seconds.

</div>

<div class="methoddesc">

settitletitle Set the window’s title string.

</div>

<div class="methoddesc">

setwincursorname

Set the window cursor to a cursor of the given name. It raises `RuntimeError` if no cursor of the given name exists. Suitable names include `’ibeam’`, `’arrow’`, `’cross’`, `’watch’` and `’plus’`. On X11, there are many more (see `<X11/cursorfont.h>`).

</div>

<div class="methoddesc">

setwinposh, v Set the the position of the window’s upper left corner (relative to the upper left corner of the screen).

</div>

<div class="methoddesc">

setwinsizewidth, height Set the window’s size.

</div>

<div class="methoddesc">

showrect Try to ensure that the given rectangle of the document is visible in the window.

</div>

<div class="methoddesc">

textcreaterect Create a text-edit object in the document at the given rectangle. Methods of text-edit objects are described below.

</div>

<div class="methoddesc">

setactive Attempt to make this window the active window. If successful, this will generate a WE_ACTIVATE event (and a WE_DEACTIVATE event in case another window in this application became inactive).

</div>

<div class="methoddesc">

close Discard the window object. It should not be used again.

</div>

### Drawing Objects

Drawing objects are created exclusively by the window method `begindrawing()`. Only one drawing object can exist at any given time; the drawing object must be deleted to finish drawing. No drawing object may exist when `stdwin.getevent()` is called. Drawing objects have the following methods:

<div class="methoddesc">

boxrect Draw a box just inside a rectangle.

</div>

<div class="methoddesc">

circlecenter, radius Draw a circle with given center point and radius.

</div>

<div class="methoddesc">

elarccenter, (rh, rv), (a1, a2) Draw an elliptical arc with given center point. `(`*`rh`*`, `*`rv`*`)` gives the half sizes of the horizontal and vertical radii. `(`*`a1`*`, `*`a2`*`)` gives the angles (in degrees) of the begin and end points. 0 degrees is at 3 o’clock, 90 degrees is at 12 o’clock.

</div>

<div class="methoddesc">

eraserect Erase a rectangle.

</div>

<div class="methoddesc">

fillcirclecenter, radius Draw a filled circle with given center point and radius.

</div>

<div class="methoddesc">

fillelarccenter, (rh, rv), (a1, a2) Draw a filled elliptical arc; arguments as for `elarc()`.

</div>

<div class="methoddesc">

fillpolypoints Draw a filled polygon given by a list (or tuple) of points.

</div>

<div class="methoddesc">

invertrect Invert a rectangle.

</div>

<div class="methoddesc">

linep1, p2 Draw a line from point *p1* to *p2*.

</div>

<div class="methoddesc">

paintrect Fill a rectangle.

</div>

<div class="methoddesc">

polypoints Draw the lines connecting the given list (or tuple) of points.

</div>

<div class="methoddesc">

shaderect, percent Fill a rectangle with a shading pattern that is about *percent* percent filled.

</div>

<div class="methoddesc">

textp, str Draw a string starting at point p (the point specifies the top left coordinate of the string).

</div>

<div class="methoddesc">

xorcirclecenter, radius Draw a circle, an elliptical arc, a line or a polygon, respectively, in XOR mode.

</div>

<div class="methoddesc">

setfgcolor These functions are similar to the corresponding functions described above for the `stdwin` module, but affect or return the colors currently used for drawing instead of the global default colors. When a drawing object is created, its colors are set to the window’s default colors, which are in turn initialized from the global default colors when the window is created.

</div>

<div class="methoddesc">

setfont These functions are similar to the corresponding functions described above for the `stdwin` module, but affect or use the current drawing font instead of the global default font. When a drawing object is created, its font is set to the window’s default font, which is in turn initialized from the global default font when the window is created.

</div>

<div class="methoddesc">

bitmappoint, bitmap, mask Draw the *bitmap* with its top left corner at *point*. If the optional *mask* argument is present, it should be either the same object as *bitmap*, to draw only those bits that are set in the bitmap, in the foreground color, or `None`, to draw all bits (ones are drawn in the foreground color, zeros in the background color). Not available on the Macintosh.

</div>

<div class="methoddesc">

cliprectrect Set the “clipping region” to a rectangle. The clipping region limits the effect of all drawing operations, until it is changed again or until the drawing object is closed. When a drawing object is created the clipping region is set to the entire window. When an object to be drawn falls partly outside the clipping region, the set of pixels drawn is the intersection of the clipping region and the set of pixels that would be drawn by the same operation in the absence of a clipping region.

</div>

<div class="methoddesc">

noclip Reset the clipping region to the entire window.

</div>

<div class="methoddesc">

close Discard the drawing object. It should not be used again.

</div>

### Menu Objects

A menu object represents a menu. The menu is destroyed when the menu object is deleted. The following methods are defined:

<div class="methoddesc">

additemtext, shortcut Add a menu item with given text. The shortcut must be a string of length 1, or omitted (to specify no shortcut).

</div>

<div class="methoddesc">

setitemi, text Set the text of item number *i*.

</div>

<div class="methoddesc">

enablei, flag Enable or disables item *i*.

</div>

<div class="methoddesc">

checki, flag Set or clear the *check mark* for item *i*.

</div>

<div class="methoddesc">

close Discard the menu object. It should not be used again.

</div>

### Bitmap Objects

A bitmap represents a rectangular array of bits. The top left bit has coordinate (0, 0). A bitmap can be drawn with the `bitmap()` method of a drawing object. Bitmaps are currently not available on the Macintosh.

The following methods are defined:

<div class="methoddesc">

getsize Return a tuple representing the width and height of the bitmap. (This returns the values that have been passed to the `newbitmap()` function.)

</div>

<div class="methoddesc">

setbitpoint, bit Set the value of the bit indicated by *point* to *bit*.

</div>

<div class="methoddesc">

getbitpoint Return the value of the bit indicated by *point*.

</div>

<div class="methoddesc">

close Discard the bitmap object. It should not be used again.

</div>

### Text-edit Objects

A text-edit object represents a text-edit block. For semantics, see the STDWIN documentation for C programmers. The following methods exist:

<div class="methoddesc">

arrowcode Pass an arrow event to the text-edit block. The *code* must be one of , , or (see module `stdwinevents`).

</div>

<div class="methoddesc">

drawrect Pass a draw event to the text-edit block. The rectangle specifies the redraw area.

</div>

<div class="methoddesc">

eventtype, window, detail Pass an event gotten from `stdwin.getevent()` to the text-edit block. Return true if the event was handled.

</div>

<div class="methoddesc">

getfocus Return 2 integers representing the start and end positions of the focus, usable as slice indices on the string returned by `gettext()`.

</div>

<div class="methoddesc">

getfocustext Return the text in the focus.

</div>

<div class="methoddesc">

getrect Return a rectangle giving the actual position of the text-edit block. (The bottom coordinate may differ from the initial position because the block automatically shrinks or grows to fit.)

</div>

<div class="methoddesc">

gettext Return the entire text buffer.

</div>

<div class="methoddesc">

moverect Specify a new position for the text-edit block in the document.

</div>

<div class="methoddesc">

replacestr Replace the text in the focus by the given string. The new focus is an insert point at the end of the string.

</div>

<div class="methoddesc">

setfocusi, j Specify the new focus. Out-of-bounds values are silently clipped.

</div>

<div class="methoddesc">

settextstr Replace the entire text buffer by the given string and set the focus to `(0, 0)`.

</div>

<div class="methoddesc">

setviewrect Set the view rectangle to *rect*. If *rect* is `None`, viewing mode is reset. In viewing mode, all output from the text-edit object is clipped to the viewing rectangle. This may be useful to implement your own scrolling text subwindow.

</div>

<div class="methoddesc">

close Discard the text-edit object. It should not be used again.

</div>

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

## `stdwinevents` — Constants for use with `stdwin`

*Constant definitions for use with `stdwin`*\
This module defines constants used by STDWIN for event types ( etc.), command codes ( etc.) and selection types ( etc.). Read the file for details. Suggested usage is

    >>> from stdwinevents import *
    >>> 

## `rect` — Functions for use with `stdwin`

*Geometry-related utility function for use with `stdwin`.*\
This module contains useful operations on rectangles. A rectangle is defined as in module `stdwin`: a pair of points, where a point is a pair of integers. For example, the rectangle

    (10, 20), (90, 80)

is a rectangle whose left, top, right and bottom edges are 10, 20, 90 and 80, respectively. Note that the positive vertical axis points down (as in `stdwin`).

The module defines the following objects:

<div class="excdesc">

error The exception raised by functions in this module when they detect an error. The exception argument is a string describing the problem in more detail.

</div>

<div class="datadesc">

empty The rectangle returned when some operations return an empty result. This makes it possible to quickly check whether a result is empty:

    >>> import rect
    >>> r1 = (10, 20), (90, 80)
    >>> r2 = (0, 0), (10, 20)
    >>> r3 = rect.intersect([r1, r2])
    >>> if r3 is rect.empty: print 'Empty intersection'
    Empty intersection
    >>> 

</div>

<div class="funcdesc">

is_emptyr Returns true if the given rectangle is empty. A rectangle `(`*`left`*`, `*`top`*`), (`*`right`*`, `*`bottom`*`)` is empty if $`\emph{left} \geq \emph{right}`$ or $`\emph{top} \geq \emph{bottom}`$.

</div>

<div class="funcdesc">

intersectlist Returns the intersection of all rectangles in the list argument. It may also be called with a tuple argument. Raises `rect.error` if the list is empty. Returns if the intersection of the rectangles is empty.

</div>

<div class="funcdesc">

unionlist Returns the smallest rectangle that contains all non-empty rectangles in the list argument. It may also be called with a tuple argument or with two or more rectangles as arguments. Returns if the list is empty or all its rectangles are empty.

</div>

<div class="funcdesc">

pointinrectpoint, rect Returns true if the point is inside the rectangle. By definition, a point `(`*`h`*`, `*`v`*`)` is inside a rectangle `(`*`left`*`, `*`top`*`), (`*`right`*`, `*`bottom`*`)` if $`\emph{left} \leq \emph{h} < \emph{right}`$ and $`\emph{top} \leq \emph{v} < \emph{bottom}`$.

</div>

<div class="funcdesc">

insetrect, (dh, dv) Returns a rectangle that lies inside the *rect* argument by *dh* pixels horizontally and *dv* pixels vertically. If *dh* or *dv* is negative, the result lies outside *rect*.

</div>

<div class="funcdesc">

rect2geomrect Converts a rectangle to geometry representation: `(`*`left`*`, `*`top`*`), (`*`width`*`, `*`height`*`)`.

</div>

<div class="funcdesc">

geom2rectgeom Converts a rectangle given in geometry representation back to the standard rectangle representation `(`*`left`*`, `*`top`*`), (`*`right`*`, `*`bottom`*`)`.

</div>

[^1]: The Python version of STDWIN does not support draw procedures; all drawing requests are reported as draw events.
# `string` — Common string operations

*Common string operations.*\
This module defines some constants useful for checking character classes and some useful string functions. See the module `re`for string functions based on regular expressions.

The constants defined in this module are are:

<div class="datadesc">

digits The string `’0123456789’`.

</div>

<div class="datadesc">

hexdigits The string `’0123456789abcdefABCDEF’`.

</div>

<div class="datadesc">

letters The concatenation of the strings and described below.

</div>

<div class="datadesc">

lowercase A string containing all the characters that are considered lowercase letters. On most systems this is the string `’abcdefghijklmnopqrstuvwxyz’`. Do not change its definition — the effect on the routines `upper()` and `swapcase()` is undefined.

</div>

<div class="datadesc">

octdigits The string `’01234567’`.

</div>

<div class="datadesc">

punctuation String of characters which are considered punctuation characters in the `C` locale.

</div>

<div class="datadesc">

printable String of characters which are considered printable. This is a combination of , , , and .

</div>

<div class="datadesc">

uppercase A string containing all the characters that are considered uppercase letters. On most systems this is the string `’ABCDEFGHIJKLMNOPQRSTUVWXYZ’`. Do not change its definition — the effect on the routines `lower()` and `swapcase()` is undefined.

</div>

<div class="datadesc">

whitespace A string containing all characters that are considered whitespace. On most systems this includes the characters space, tab, linefeed, return, formfeed, and vertical tab. Do not change its definition — the effect on the routines `strip()` and `split()` is undefined.

</div>

Many of the functions provided by this module are also defined as methods of string and Unicode objects; see “String Methods” (section <a href="#string-methods" data-reference-type="ref" data-reference="string-methods">[string-methods]</a>) for more information on those. The functions defined in this module are:

<div class="funcdesc">

atofs Convert a string to a floating point number. The string must have the standard syntax for a floating point literal in Python, optionally preceded by a sign (`+` or `-`). Note that this behaves identical to the built-in function `float()`when passed a string.

**Note:** When passing in a string, values for NaNand Infinitymay be returned, depending on the underlying C library. The specific set of strings accepted which cause these values to be returned depends entirely on the C library and is known to vary.

</div>

<div class="funcdesc">

atois Convert string *s* to an integer in the given *base*. The string must consist of one or more digits, optionally preceded by a sign (`+` or `-`). The *base* defaults to 10. If it is 0, a default base is chosen depending on the leading characters of the string (after stripping the sign): `0x` or `0X` means 16, `0` means 8, anything else means 10. If *base* is 16, a leading `0x` or `0X` is always accepted, though not required. This behaves identically to the built-in function `int()` when passed a string. (Also note: for a more flexible interpretation of numeric literals, use the built-in function `eval()`.)

</div>

<div class="funcdesc">

atols Convert string *s* to a long integer in the given *base*. The string must consist of one or more digits, optionally preceded by a sign (`+` or `-`). The *base* argument has the same meaning as for `atoi()`. A trailing `l` or `L` is not allowed, except if the base is 0. Note that when invoked without *base* or with *base* set to 10, this behaves identical to the built-in function `long()`when passed a string.

</div>

<div class="funcdesc">

capitalizeword Capitalize the first character of the argument.

</div>

<div class="funcdesc">

capwordss Split the argument into words using `split()`, capitalize each word using `capitalize()`, and join the capitalized words using `join()`. Note that this replaces runs of whitespace characters by a single space, and removes leading and trailing whitespace.

</div>

<div class="funcdesc">

expandtabss, Expand tabs in a string, i.e. replace them by one or more spaces, depending on the current column and the given tab size. The column number is reset to zero after each newline occurring in the string. This doesn’t understand other non-printing characters or escape sequences. The tab size defaults to 8.

</div>

<div class="funcdesc">

finds, sub Return the lowest index in *s* where the substring *sub* is found such that *sub* is wholly contained in *`s`*`[`*`start`*`:`*`end`*`]`. Return `-1` on failure. Defaults for *start* and *end* and interpretation of negative values is the same as for slices.

</div>

<div class="funcdesc">

rfinds, sub Like `find()` but find the highest index.

</div>

<div class="funcdesc">

indexs, sub Like `find()` but raise `ValueError` when the substring is not found.

</div>

<div class="funcdesc">

rindexs, sub Like `rfind()` but raise `ValueError` when the substring is not found.

</div>

<div class="funcdesc">

counts, sub Return the number of (non-overlapping) occurrences of substring *sub* in string *`s`*`[`*`start`*`:`*`end`*`]`. Defaults for *start* and *end* and interpretation of negative values are the same as for slices.

</div>

<div class="funcdesc">

lowers Return a copy of *s*, but with upper case letters converted to lower case.

</div>

<div class="funcdesc">

maketransfrom, to Return a translation table suitable for passing to `translate()` or `regex.compile()`, that will map each character in *from* into the character at the same position in *to*; *from* and *to* must have the same length.

**Warning:** don’t use strings derived from and as arguments; in some locales, these don’t have the same length. For case conversions, always use `lower()` and `upper()`.

</div>

<div class="funcdesc">

splits Return a list of the words of the string *s*. If the optional second argument *sep* is absent or `None`, the words are separated by arbitrary strings of whitespace characters (space, tab, newline, return, formfeed). If the second argument *sep* is present and not `None`, it specifies a string to be used as the word separator. The returned list will then have one more item than the number of non-overlapping occurrences of the separator in the string. The optional third argument *maxsplit* defaults to 0. If it is nonzero, at most *maxsplit* number of splits occur, and the remainder of the string is returned as the final element of the list (thus, the list will have at most *`maxsplit`*`+1` elements).

</div>

<div class="funcdesc">

splitfieldss This function behaves identically to `split()`. (In the past, `split()` was only used with one argument, while `splitfields()` was only used with two arguments.)

</div>

<div class="funcdesc">

joinwords Concatenate a list or tuple of words with intervening occurrences of *sep*. The default value for *sep* is a single space character. It is always true that `string.join(string.split(`*`s`*`, `*`sep`*`), `*`sep`*`)` equals *s*.

</div>

<div class="funcdesc">

joinfieldswords This function behaves identical to `join()`. (In the past, `join()` was only used with one argument, while `joinfields()` was only used with two arguments.)

</div>

<div class="funcdesc">

lstrips Return a copy of *s* but without leading whitespace characters.

</div>

<div class="funcdesc">

rstrips Return a copy of *s* but without trailing whitespace characters.

</div>

<div class="funcdesc">

strips Return a copy of *s* without leading or trailing whitespace.

</div>

<div class="funcdesc">

swapcases Return a copy of *s*, but with lower case letters converted to upper case and vice versa.

</div>

<div class="funcdesc">

translates, table Delete all characters from *s* that are in *deletechars* (if present), and then translate the characters using *table*, which must be a 256-character string giving the translation for each character value, indexed by its ordinal.

</div>

<div class="funcdesc">

uppers Return a copy of *s*, but with lower case letters converted to upper case.

</div>

<div class="funcdesc">

ljusts, width These functions respectively left-justify, right-justify and center a string in a field of given width. They return a string that is at least *width* characters wide, created by padding the string *s* with spaces until the given width on the right, left or both sides. The string is never truncated.

</div>

<div class="funcdesc">

zfills, width Pad a numeric string on the left with zero digits until the given width is reached. Strings starting with a sign are handled correctly.

</div>

<div class="funcdesc">

replacestr, old, new Return a copy of string *str* with all occurrences of substring *old* replaced by *new*. If the optional argument *maxsplit* is given, the first *maxsplit* occurrences are replaced.

</div>

This module is implemented in Python. Much of its functionality has been reimplemented in the built-in module `strop`. However, you should *never* import the latter module directly. When `string` discovers that `strop` exists, it transparently replaces parts of itself with the implementation from `strop`. After initialization, there is *no* overhead in using `string` instead of `strop`.
# `StringIO` — Read and write strings as files

*Read and write strings as if they were files.*\
This module implements a file-like class, `StringIO`, that reads and writes a string buffer (also known as *memory files*). See the description on file objects for operations (section <a href="#bltin-file-objects" data-reference-type="ref" data-reference="bltin-file-objects">[bltin-file-objects]</a>).

<div class="classdesc">

StringIO When a `StringIO` object is created, it can be initialized to an existing string by passing the string to the constructor. If no string is given, the `StringIO` will start empty.

</div>

The following methods of `StringIO` objects require special mention:

<div class="methoddesc">

getvalue Retrieve the entire contents of the “file” at any time before the `StringIO` object’s `close()` method is called.

</div>

<div class="methoddesc">

close Free the memory buffer.

</div>

# `cStringIO` — Faster version of `StringIO`

*Faster version of `StringIO`, but not subclassable.*\
The module `cStringIO` provides an interface similar to that of the `StringIO` module. Heavy use of `StringIO.StringIO` objects can be made more efficient by using the function `StringIO()` from this module instead.

Since this module provides a factory function which returns objects of built-in types, there’s no way to build your own version using subclassing. Use the original `StringIO` module in that case.

The following data objects are provided as well:

<div class="datadesc">

InputType The type object of the objects created by calling `StringIO` with a string parameter.

</div>

<div class="datadesc">

OutputType The type object of the objects returned by calling `StringIO` with no parameters.

</div>

There is a C API to the module as well; refer to the module source for more information.
# String Services

The modules described in this chapter provide a wide range of string manipulation operations. Here’s an overview:
# SunOS Specific Services

The modules described in this chapter provide interfaces to features that are unique to the SunOS operating system (versions 4 and 5; the latter is also known as Solaris version 2).
# `sunau` — Read and write Sun AU files

*Provide an interface to the Sun AU sound format.*\
The `sunau` module provides a convenient interface to the Sun AU sound format. Note that this module is interface-compatible with the modules `aifc` and `wave`.

The `sunau` module defines the following functions:

<div class="funcdesc">

openfile, mode If *file* is a string, open the file by that name, otherwise treat it as a seekable file-like object. *mode* can be any of

`’r’`  
Read only mode.

`’w’`  
Write only mode.

Note that it does not allow read/write files.

A *mode* of `’r’` returns a `AU_read` object, while a *mode* of `’w’` or `’wb’` returns a `AU_write` object.

</div>

<div class="funcdesc">

openfpfile, mode A synonym for `open`, maintained for backwards compatibility.

</div>

The `sunau` module defines the following exception:

<div class="excdesc">

Error An error raised when something is impossible because of Sun AU specs or implementation deficiency.

</div>

The `sunau` module defines the following data item:

<div class="datadesc">

AUDIO_FILE_MAGIC An integer every valid Sun AU file begins with a big-endian encoding of.

</div>

## AU_read Objects <span id="au-read-objects" label="au-read-objects"></span>

AU_read objects, as returned by `open()` above, have the following methods:

<div class="methoddesc">

close Close the stream, and make the instance unusable. (This is called automatically on deletion.)

</div>

<div class="methoddesc">

getnchannels Returns number of audio channels (1 for mone, 2 for stereo).

</div>

<div class="methoddesc">

getsampwidth Returns sample width in bytes.

</div>

<div class="methoddesc">

getframerate Returns sampling frequency.

</div>

<div class="methoddesc">

getnframes Returns number of audio frames.

</div>

<div class="methoddesc">

getcomptype Returns compression type. Supported compression types are `’ULAW’`, `’ALAW’` and `’NONE’`.

</div>

<div class="methoddesc">

getcompname Human-readable version of `getcomptype()`. The supported types have the respective names `’CCITT G.711 u-law’`, `’CCITT G.711 A-law’` and `’not compressed’`.

</div>

<div class="methoddesc">

getparams Returns a tuple `(`*`nchannels`*`, `*`sampwidth`*`, `*`framerate`*`, `*`nframes`*`, `*`comptype`*`, `*`compname`*`)`, equivalent to output of the `get*()` methods.

</div>

<div class="methoddesc">

readframesn Reads and returns at most *n* frames of audio, as a string of bytes.

</div>

<div class="methoddesc">

rewind Rewind the file pointer to the beginning of the audio stream.

</div>

The following two methods define a term “position” which is compatible between them, and is otherwise implementation dependent.

<div class="methoddesc">

setpospos Set the file pointer to the specified position.

</div>

<div class="methoddesc">

tell Return current file pointer position.

</div>

The following two functions are defined for compatibility with the `aifc`, and don’t do anything interesting.

<div class="methoddesc">

getmarkers Returns `None`.

</div>

<div class="methoddesc">

getmarkid Raise an error.

</div>

## AU_write Objects <span id="au-write-objects" label="au-write-objects"></span>

AU_write objects, as returned by `open()` above, have the following methods:

<div class="methoddesc">

setnchannelsn Set the number of channels.

</div>

<div class="methoddesc">

setsampwidthn Set the sample width (in bytes.)

</div>

<div class="methoddesc">

setframeraten Set the frame rate.

</div>

<div class="methoddesc">

setnframesn Set the number of frames. This can be later changed, when and if more frames are written.

</div>

<div class="methoddesc">

setcomptypetype, name Set the compression type and description. Only `’NONE’` and `’ULAW’` are supported on output.

</div>

<div class="methoddesc">

setparamstuple The *tuple* should be `(`*`nchannels`*`, `*`sampwidth`*`, `*`framerate`*`, `*`nframes`*`, `*`comptype`*`, `*`compname`*`)`, with values valid for the `set*()` methods. Set all parameters.

</div>

<div class="methoddesc">

tell Return current position in the file, with the same disclaimer for the `AU_read.tell()` and `AU_read.setpos()` methods.

</div>

<div class="methoddesc">

writeframesrawdata Write audio frames, without correcting *nframes*.

</div>

<div class="methoddesc">

writeframesdata Write audio frames and make sure *nframes* is correct.

</div>

<div class="methoddesc">

close Make sure *nframes* is correct, and close the file.

This method is called upon deletion.

</div>

Note that it is invalid to set any parameters after calling `writeframes()` or `writeframesraw()`.
# `sunaudiodev` — Access to Sun audio hardware

*Access to Sun audio hardware.*\
This module allows you to access the Sun audio interface. The Sun audio hardware is capable of recording and playing back audio data in u-LAWformat with a sample rate of 8K per second. A full description can be found in the manual page.

The module `SUNAUDIODEV`defines constants which may be used with this module.

This module defines the following variables and functions:

<div class="excdesc">

error This exception is raised on all errors. The argument is a string describing what went wrong.

</div>

<div class="funcdesc">

openmode This function opens the audio device and returns a Sun audio device object. This object can then be used to do I/O on. The *mode* parameter is one of `’r’` for record-only access, `’w’` for play-only access, `’rw’` for both and `’control’` for access to the control device. Since only one process is allowed to have the recorder or player open at the same time it is a good idea to open the device only for the activity needed. See for details.

As per the manpage, this module first looks in the environment variable `AUDIODEV` for the base audio device filename. If not found, it falls back to `/dev/audio`. The control device is calculated by appending “ctl” to the base audio device.

</div>

## Audio Device Objects <span id="audio-device-objects" label="audio-device-objects"></span>

The audio device objects are returned by `open()` define the following methods (except `control` objects which only provide `getinfo()`, `setinfo()`, `fileno()`, and `drain()`):

<div class="methoddesc">

close This method explicitly closes the device. It is useful in situations where deleting the object does not immediately close it since there are other references to it. A closed device should not be used again.

</div>

<div class="methoddesc">

fileno Returns the file descriptor associated with the device. This can be used to set up `SIGPOLL` notification, as described below.

</div>

<div class="methoddesc">

drain This method waits until all pending output is processed and then returns. Calling this method is often not necessary: destroying the object will automatically close the audio device and this will do an implicit drain.

</div>

<div class="methoddesc">

flush This method discards all pending output. It can be used avoid the slow response to a user’s stop request (due to buffering of up to one second of sound).

</div>

<div class="methoddesc">

getinfo This method retrieves status information like input and output volume, etc. and returns it in the form of an audio status object. This object has no methods but it contains a number of attributes describing the current device status. The names and meanings of the attributes are described in `<sun/audioio.h>` and in the manual page. Member names are slightly different from their C counterparts: a status object is only a single structure. Members of the substructure have `o_` prepended to their name and members of the structure have `i_`. So, the C member is accessed as `o_sample_rate`, as `i_gain` and plainly as `monitor_gain`.

</div>

<div class="methoddesc">

ibufcount This method returns the number of samples that are buffered on the recording side, i.e. the program will not block on a `read()` call of so many samples.

</div>

<div class="methoddesc">

obufcount This method returns the number of samples buffered on the playback side. Unfortunately, this number cannot be used to determine a number of samples that can be written without blocking since the kernel output queue length seems to be variable.

</div>

<div class="methoddesc">

readsize This method reads *size* samples from the audio input and returns them as a Python string. The function blocks until enough data is available.

</div>

<div class="methoddesc">

setinfostatus This method sets the audio device status parameters. The *status* parameter is an device status object as returned by `getinfo()` and possibly modified by the program.

</div>

<div class="methoddesc">

writesamples Write is passed a Python string containing audio samples to be played. If there is enough buffer space free it will immediately return, otherwise it will block.

</div>

The audio device supports asynchronous notification of various events, through the SIGPOLL signal. Here’s an example of how you might enable this in Python:

    def handle_sigpoll(signum, frame):
        print 'I got a SIGPOLL update'

    import fcntl, signal, STROPTS

    signal.signal(signal.SIGPOLL, handle_sigpoll)
    fcntl.ioctl(audio_obj.fileno(), STROPTS.I_SETSIG, STROPTS.S_MSG)

# `SUNAUDIODEV` — Constants used with `sunaudiodev`

*Constants for use with `sunaudiodev`.*\
This is a companion module to `sunaudiodev`which defines useful symbolic constants like , , , etc. The names of the constants are the same names as used in the C include file `<sun/audioio.h>`, with the leading string `AUDIO_` stripped.
# `sys` — System-specific parameters and functions

*Access system-specific parameters and functions.*\
This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.

<div class="datadesc">

argv The list of command line arguments passed to a Python script. `argv[0]` is the script name (it is operating system dependent whether this is a full pathname or not). If the command was executed using the `-c` command line option to the interpreter, `argv[0]` is set to the string `’-c’`. If no script name was passed to the Python interpreter, `argv` has zero length.

</div>

<div class="datadesc">

byteorder An indicator of the native byte order. This will have the value `’big’` on big-endian (most-signigicant byte first) platforms, and `’little’` on little-endian (least-significant byte first) platforms. *New in version 2.0.*

</div>

<div class="datadesc">

builtin_module_names A tuple of strings giving the names of all modules that are compiled into this Python interpreter. (This information is not available in any other way — `modules.keys()` only lists the imported modules.)

</div>

<div class="datadesc">

copyright A string containing the copyright pertaining to the Python interpreter.

</div>

<div class="datadesc">

dllhandle Integer specifying the handle of the Python DLL. Availability: Windows.

</div>

<div class="funcdesc">

exc_info This function returns a tuple of three values that give information about the exception that is currently being handled. The information returned is specific both to the current thread and to the current stack frame. If the current stack frame is not handling an exception, the information is taken from the calling stack frame, or its caller, and so on until a stack frame is found that is handling an exception. Here, “handling an exception” is defined as “executing or having executed an except clause.” For any stack frame, only information about the most recently handled exception is accessible.

If no exception is being handled anywhere on the stack, a tuple containing three `None` values is returned. Otherwise, the values returned are `(`*`type`*`, `*`value`*`, `*`traceback`*`)`. Their meaning is: *type* gets the exception type of the exception being handled (a string or class object); *value* gets the exception parameter (its *associated value* or the second argument to , which is always a class instance if the exception type is a class object); *traceback* gets a traceback object (see the Reference Manual) which encapsulates the call stack at the point where the exception originally occurred. **Warning:** assigning the *traceback* return value to a local variable in a function that is handling an exception will cause a circular reference. This will prevent anything referenced by a local variable in the same function or by the traceback from being garbage collected. Since most functions don’t need access to the traceback, the best solution is to use something like `type, value = sys.exc_info()[:2]` to extract only the exception type and value. If you do need the traceback, make sure to delete it after use (best done with a ... statement) or to call `exc_info()` in a function that does not itself handle an exception.

</div>

<div class="datadesc">

exc_type *Deprecated since version 1.5: Use `exc_info()` instead.* Since they are global variables, they are not specific to the current thread, so their use is not safe in a multi-threaded program. When no exception is being handled, `exc_type` is set to `None` and the other two are undefined.

</div>

<div class="datadesc">

exec_prefix A string giving the site-specific directory prefix where the platform-dependent Python files are installed; by default, this is also `’/usr/local’`. This can be set at build time with the `--exec-prefix` argument to the script. Specifically, all configuration files (e.g. the `config.h` header file) are installed in the directory `exec_prefix + ’/lib/python`*`version`*`/config’`, and shared library modules are installed in `exec_prefix + ’/lib/python`*`version`*`/lib-dynload’`, where *version* is equal to `version[:3]`.

</div>

<div class="datadesc">

executable A string giving the name of the executable binary for the Python interpreter, on systems where this makes sense.

</div>

<div class="funcdesc">

exit Exit from Python. This is implemented by raising the `SystemExit` exception, so cleanup actions specified by finally clauses of statements are honored, and it is possible to intercept the exit attempt at an outer level. The optional argument *arg* can be an integer giving the exit status (defaulting to zero), or another type of object. If it is an integer, zero is considered “successful termination” and any nonzero value is considered “abnormal termination” by shells and the like. Most systems require it to be in the range 0-127, and produce undefined results otherwise. Some systems have a convention for assigning specific meanings to specific exit codes, but these are generally underdeveloped; Unix programs generally use 2 for command line syntax errors and 1 for all other kind of errors. If another type of object is passed, `None` is equivalent to passing zero, and any other object is printed to `sys.stderr` and results in an exit code of 1. In particular, `sys.exit("some error message")` is a quick way to exit a program when an error occurs.

</div>

<div class="datadesc">

exitfunc This value is not actually defined by the module, but can be set by the user (or by a program) to specify a clean-up action at program exit. When set, it should be a parameterless function. This function will be called when the interpreter exits. Only one function may be installed in this way; to allow multiple functions which will be called at termination, use the `atexit` module. Note: the exit function is not called when the program is killed by a signal, when a Python fatal internal error is detected, or when `os._exit()` is called.

</div>

<div class="funcdesc">

getrefcountobject Return the reference count of the *object*. The count returned is generally one higher than you might expect, because it includes the (temporary) reference as an argument to `getrefcount()`.

</div>

<div class="funcdesc">

getrecursionlimit Return the current value of the recursion limit, the maximum depth of the Python interpreter stack. This limit prevents infinite recursion from causing an overflow of the C stack and crashing Python. It can be set by `setrecursionlimit()`.

</div>

<div class="datadesc">

hexversion The version number encoded as a single integer. This is guaranteed to increase with each version, including proper support for non-production releases. For example, to test that the Python interpreter is at least version 1.5.2, use:

    if sys.hexversion >= 0x010502F0:
        # use some advanced feature
        ...
    else:
        # use an alternative implementation or warn the user
        ...

This is called `hexversion` since it only really looks meaningful when viewed as the result of passing it to the built-in `hex()` function. The `version_info` value may be used for a more human-friendly encoding of the same information. *New in version 1.5.2.*

</div>

<div class="datadesc">

last_type These three variables are not always defined; they are set when an exception is not handled and the interpreter prints an error message and a stack traceback. Their intended use is to allow an interactive user to import a debugger module and engage in post-mortem debugging without having to re-execute the command that caused the error. (Typical use is `import pdb; pdb.pm()` to enter the post-mortem debugger; see the chapter “The Python Debugger” for more information.) The meaning of the variables is the same as that of the return values from `exc_info()` above. (Since there is only one interactive thread, thread-safety is not a concern for these variables, unlike for `exc_type` etc.)

</div>

<div class="datadesc">

maxint The largest positive integer supported by Python’s regular integer type. This is at least 2\*\*31-1. The largest negative integer is `-maxint-1` – the asymmetry results from the use of 2’s complement binary arithmetic.

</div>

<div class="datadesc">

modules This is a dictionary that maps module names to modules which have already been loaded. This can be manipulated to force reloading of modules and other tricks. Note that removing a module from this dictionary is *not* the same as calling `reload()`on the corresponding module object.

</div>

<div class="datadesc">

path A list of strings that specifies the search path for modules. Initialized from the environment variable , or an installation-dependent default.

The first item of this list, `path[0]`, is the directory containing the script that was used to invoke the Python interpreter. If the script directory is not available (e.g. if the interpreter is invoked interactively or if the script is read from standard input), `path[0]` is the empty string, which directs Python to search modules in the current directory first. Notice that the script directory is inserted *before* the entries inserted as a result of .

</div>

<div class="datadesc">

platform This string contains a platform identifier, e.g. `’sunos5’` or `’linux1’`. This can be used to append platform-specific components to `path`, for instance.

</div>

<div class="datadesc">

prefix A string giving the site-specific directory prefix where the platform independent Python files are installed; by default, this is the string `’/usr/local’`. This can be set at build time with the `--prefix` argument to the script. The main collection of Python library modules is installed in the directory `prefix + ’/lib/python`*`version`*`’` while the platform independent header files (all except `config.h`) are stored in `prefix + ’/include/python`*`version`*`’`, where *version* is equal to `version[:3]`.

</div>

<div class="datadesc">

ps1 Strings specifying the primary and secondary prompt of the interpreter. These are only defined if the interpreter is in interactive mode. Their initial values in this case are `’>>> ’` and `’... ’`. If a non-string object is assigned to either variable, its `str()` is re-evaluated each time the interpreter prepares to read a new interactive command; this can be used to implement a dynamic prompt.

</div>

<div class="funcdesc">

setcheckintervalinterval Set the interpreter’s “check interval”. This integer value determines how often the interpreter checks for periodic things such as thread switches and signal handlers. The default is `10`, meaning the check is performed every 10 Python virtual instructions. Setting it to a larger value may increase performance for programs using threads. Setting it to a value `<=` 0 checks every virtual instruction, maximizing responsiveness as well as overhead.

</div>

<div class="funcdesc">

setprofileprofilefunc Set the system’s profile function, which allows you to implement a Python source code profiler in Python. See the chapter on the Python Profiler. The system’s profile function is called similarly to the system’s trace function (see `settrace()`), but it isn’t called for each executed line of code (only on call and return and when an exception occurs). Also, its return value is not used, so it can just return `None`.

</div>

<div class="funcdesc">

setrecursionlimitlimit Set the maximum depth of the Python interpreter stack to *limit*. This limit prevents infinite recursion from causing an overflow of the C stack and crashing Python.

The highest possible limit is platform-dependent. A user may need to set the limit higher when she has a program that requires deep recursion and a platform that supports a higher limit. This should be done with care, because a too-high limit can lead to a crash.

</div>

<div class="funcdesc">

settracetracefunc Set the system’s trace function, which allows you to implement a Python source code debugger in Python. See section “How It Works” in the chapter on the Python Debugger.

</div>

<div class="datadesc">

stdin File objects corresponding to the interpreter’s standard input, output and error streams. `stdin` is used for all interpreter input except for scripts but including calls to `input()`and `raw_input()`. `stdout` is used for the output of and expression statements and for the prompts of `input()` and `raw_input()`. The interpreter’s own prompts and (almost all of) its error messages go to `stderr`. `stdout` and `stderr` needn’t be built-in file objects: any object is acceptable as long as it has a `write()` method that takes a string argument. (Changing these objects doesn’t affect the standard I/O streams of processes executed by `os.popen()`, `os.system()` or the `exec*()` family of functions in the `os` module.)

</div>

<div class="datadesc">

\_\_stdin\_\_ These objects contain the original values of `stdin`, `stderr` and `stdout` at the start of the program. They are used during finalization, and could be useful to restore the actual files to known working file objects in case they have been overwritten with a broken object.

</div>

<div class="datadesc">

tracebacklimit When this variable is set to an integer value, it determines the maximum number of levels of traceback information printed when an unhandled exception occurs. The default is `1000`. When set to 0 or less, all traceback information is suppressed and only the exception type and value are printed.

</div>

<div class="datadesc">

version A string containing the version number of the Python interpreter plus additional information on the build number and compiler used. It has a value of the form `’`*`version`*` (#`*`build_number`*`, `*`build_date`*`, `*`build_time`*`) [`*`compiler`*`]’`. The first three characters are used to identify the version in the installation directories (where appropriate on each platform). An example:

    >>> import sys
    >>> sys.version
    '1.5.2 (#0 Apr 13 1999, 10:51:12) [MSC 32 bit (Intel)]'

</div>

<div class="datadesc">

version_info A tuple containing the five components of the version number: *major*, *minor*, *micro*, *releaselevel*, and *serial*. All values except *releaselevel* are integers; the release level is `’alpha’`, `’beta’`, `’candidate’`, or `’final’`. The `version_info` value corresponding to the Python version 2.0 is `(2, 0, 0, ’final’, 0)`. *New in version 2.0.*

</div>

<div class="datadesc">

winver The version number used to form registry keys on Windows platforms. This is stored as string resource 1000 in the Python DLL. The value is normally the first three characters of . It is provided in the `sys` module for informational purposes; modifying this value has no effect on the registry keys used by Python. Availability: Windows.

</div>
# `syslog` — Unix syslog library routines

*An interface to the Unix syslog library routines.*\
This module provides an interface to the Unix `syslog` library routines. Refer to the Unix manual pages for a detailed description of the `syslog` facility.

The module defines the following functions:

<div class="funcdesc">

syslog message Send the string *message* to the system logger. A trailing newline is added if necessary. Each message is tagged with a priority composed of a *facility* and a *level*. The optional *priority* argument, which defaults to , determines the message priority. If the facility is not encoded in *priority* using logical-or (`LOG_INFO | LOG_USER`), the value given in the `openlog()` call is used.

</div>

<div class="funcdesc">

openlogident Logging options other than the defaults can be set by explicitly opening the log file with `openlog()` prior to calling `syslog()`. The defaults are (usually) *ident* = `’syslog’`, *logopt* = `0`, *facility* = . The *ident* argument is a string which is prepended to every message. The optional *logopt* argument is a bit field - see below for possible values to combine. The optional *facility* argument sets the default facility for messages which do not have a facility explicitly encoded.

</div>

<div class="funcdesc">

closelog Close the log file.

</div>

<div class="funcdesc">

setlogmaskmaskpri Set the priority mask to *maskpri* and return the previous mask value. Calls to `syslog()` with a priority level not set in *maskpri* are ignored. The default is to log all priorities. The function `LOG_MASK(`*`pri`*`)` calculates the mask for the individual priority *pri*. The function `LOG_UPTO(`*`pri`*`)` calculates the mask for all priorities up to and including *pri*.

</div>

The module defines the following constants:

Priority levels (high to low):  
, , , , , , , .

Facilities:  
, , , , , , , , and to .

Log options:  
, , , and if defined in `<syslog.h>`.
# `tempfile` — Generate temporary file names

*Generate temporary file names.*\
This module generates temporary file names. It is not Unix specific, but it may require some help on non-Unix systems.

The module defines the following user-callable functions:

<div class="funcdesc">

mktemp Return a unique temporary filename. This is an absolute pathname of a file that does not exist at the time the call is made. No two calls will return the same filename. *suffix*, if provided, is used as the last part of the generated file name. This can be used to provide a filename extension or other identifying information that may be useful on some platforms.

</div>

<div class="funcdesc">

TemporaryFile Return a file (or file-like) object that can be used as a temporary storage area. The file is created in the most secure manner available in the appropriate temporary directory for the host platform. Under Unix, the directory entry to the file is removed so that it is secure against attacks which involve creating symbolic links to the file or replacing the file with a symbolic link to some other file. For other platforms, which don’t allow removing the directory entry while the file is in use, the file is automatically deleted as soon as it is closed (including an implicit close when it is garbage-collected).

The *mode* parameter defaults to `’w+b’` so that the file created can be read and written without being closed. Binary mode is used so that it behaves consistently on all platforms without regard for the data that is stored. *bufsize* defaults to `-1`, meaning that the operating system default is used. *suffix* is passed to `mktemp()`.

</div>

The module uses two global variables that tell it how to construct a temporary name. The caller may assign values to them; by default they are initialized at the first call to `mktemp()`.

<div class="datadesc">

tempdir When set to a value other than `None`, this variable defines the directory in which filenames returned by `mktemp()` reside. The default is taken from the environment variable ; if this is not set, either `/usr/tmp` is used (on Unix), or the current working directory (all other systems). No check is made to see whether its value is valid.

</div>

<div class="funcdesc">

gettempprefix Return the filename prefix used to create temporary files. This does not contain the directory component. Using this function is preferred over using the `template` variable directly. *New in version 1.5.2.*

</div>

<div class="datadesc">

template *Deprecated since version 2.0: Use `gettempprefix()` instead.* When set to a value other than `None`, this variable defines the prefix of the final component of the filenames returned by `mktemp()`. A string of decimal digits is added to generate unique filenames. The default is either `@`*`pid`*`.` where *pid* is the current process ID (on Unix), `~`*`pid`*`-` on Windows NT, `Python-Tmp-` on MacOS, or `tmp` (all other systems).

Older versions of this module used to require that `template` be set to `None` after a call to `os.fork()`; this has not been necessary since version 1.5.2.

</div>
# `thread` — Multiple threads of control

*Create multiple threads of control within one interpreter.*\
This module provides low-level primitives for working with multiple threads (a.k.a. *light-weight processes* or *tasks*) — multiple threads of control sharing their global data space. For synchronization, simple locks (a.k.a. *mutexes* or *binary semaphores*) are provided. The module is optional. It is supported on Windows NT and ’95, SGI IRIX, Solaris 2.x, as well as on systems that have a thread (a.k.a. “pthread”) implementation. It defines the following constant and functions:

<div class="excdesc">

error Raised on thread-specific errors.

</div>

<div class="datadesc">

LockType This is the type of lock objects.

</div>

<div class="funcdesc">

start_new_threadfunction, args Start a new thread. The thread executes the function *function* with the argument list *args* (which must be a tuple). The optional *kwargs* argument specifies a dictionary of keyword arguments. When the function returns, the thread silently exits. When the function terminates with an unhandled exception, a stack trace is printed and then the thread exits (but other threads continue to run).

</div>

<div class="funcdesc">

exit Raise the `SystemExit` exception. When not caught, this will cause the thread to exit silently.

</div>

<div class="funcdesc">

exit_thread *Deprecated since version 1.5.2: Use `exit()`.* This is an obsolete synonym for `exit()`.

</div>

<div class="funcdesc">

allocate_lock Return a new lock object. Methods of locks are described below. The lock is initially unlocked.

</div>

<div class="funcdesc">

get_ident Return the ‘thread identifier’ of the current thread. This is a nonzero integer. Its value has no direct meaning; it is intended as a magic cookie to be used e.g. to index a dictionary of thread-specific data. Thread identifiers may be recycled when a thread exits and another thread is created.

</div>

Lock objects have the following methods:

<div class="methoddesc">

acquire Without the optional argument, this method acquires the lock unconditionally, if necessary waiting until it is released by another thread (only one thread at a time can acquire a lock — that’s their reason for existence), and returns `None`. If the integer *waitflag* argument is present, the action depends on its value: if it is zero, the lock is only acquired if it can be acquired immediately without waiting, while if it is nonzero, the lock is acquired unconditionally as before. If an argument is present, the return value is `1` if the lock is acquired successfully, `0` if not.

</div>

<div class="methoddesc">

release Releases the lock. The lock must have been acquired earlier, but not necessarily by the same thread.

</div>

<div class="methoddesc">

locked Return the status of the lock: `1` if it has been acquired by some thread, `0` if not.

</div>

**Caveats:**

- Threads interact strangely with interrupts: the `KeyboardInterrupt` exception will be received by an arbitrary thread. (When the `signal`module is available, interrupts always go to the main thread.)

- Calling `sys.exit()` or raising the `SystemExit` exception is equivalent to calling `exit()`.

- Not all built-in functions that may block waiting for I/O allow other threads to run. (The most popular ones (`time.sleep()`, *`file`*`.read()`, `select.select()`) work as expected.)

- It is not possible to interrupt the `acquire()` method on a lock — the `KeyboardInterrupt` exception will happen after the lock has been acquired.

- When the main thread exits, it is system defined whether the other threads survive. On SGI IRIX using the native thread implementation, they survive. On most other systems, they are killed without executing ... clauses or executing object destructors.

- When the main thread exits, it does not do any of its usual cleanup (except that ... clauses are honored), and the standard I/O files are not flushed.
# `threading` — Higher-level threading interface

*Higher-level threading interface.*\
This module constructs higher-level threading interfaces on top of the lower level `thread` module.

This module is safe for use with `from threading import *`. It defines the following functions and objects:

<div class="funcdesc">

activeCount Return the number of currently active `Thread` objects. The returned count is equal to the length of the list returned by `enumerate()`. A function that returns the number of currently active threads.

</div>

<div class="funcdesc">

Condition A factory function that returns a new condition variable object. A condition variable allows one or more threads to wait until they are notified by another thread.

</div>

<div class="funcdesc">

currentThread Return the current `Thread` object, corresponding to the caller’s thread of control. If the caller’s thread of control was not created through the `threading` module, a dummy thread object with limited functionality is returned.

</div>

<div class="funcdesc">

enumerate Return a list of all currently active `Thread` objects. The list includes daemonic threads, dummy thread objects created by `currentThread()`, and the main thread. It excludes terminated threads and threads that have not yet been started.

</div>

<div class="funcdesc">

Event A factory function that returns a new event object. An event manages a flag that can be set to true with the `set()` method and reset to false with the `clear()` method. The `wait()` method blocks until the flag is true.

</div>

<div class="funcdesc">

Lock A factory function that returns a new primitive lock object. Once a thread has acquired it, subsequent attempts to acquire it block, until it is released; any thread may release it.

</div>

<div class="funcdesc">

RLock A factory function that returns a new reentrant lock object. A reentrant lock must be released by the thread that acquired it. Once a thread has acquired a reentrant lock, the same thread may acquire it again without blocking; the thread must release it once for each time it has acquired it.

</div>

<div class="funcdesc">

Semaphore A factory function that returns a new semaphore object. A semaphore manages a counter representing the number of `release()` calls minus the number of `acquire()` calls, plus an initial value. The `acquire()` method blocks if necessary until it can return without making the counter negative.

</div>

<div class="classdesc">

Thread A class that represents a thread of control. This class can be safely subclassed in a limited fashion.

</div>

Detailed interfaces for the objects are documented below.

The design of this module is loosely based on Java’s threading model. However, where Java makes locks and condition variables basic behavior of every object, they are separate objects in Python. Python’s `Thread` class supports a subset of the behavior of Java’s Thread class; currently, there are no priorities, no thread groups, and threads cannot be destroyed, stopped, suspended, resumed, or interrupted. The static methods of Java’s Thread class, when implemented, are mapped to module-level functions.

All of the methods described below are executed atomically.

## Lock Objects <span id="lock-objects" label="lock-objects"></span>

A primitive lock is a synchronization primitive that is not owned by a particular thread when locked. In Python, it is currently the lowest level synchronization primitive available, implemented directly by the `thread` extension module.

A primitive lock is in one of two states, “locked” or “unlocked”. It is created in the unlocked state. It has two basic methods, `acquire()` and `release()`. When the state is unlocked, `acquire()` changes the state to locked and returns immediately. When the state is locked, `acquire()` blocks until a call to `release()` in another thread changes it to unlocked, then the `acquire()` call resets it to locked and returns. The `release()` method should only be called in the locked state; it changes the state to unlocked and returns immediately. When more than one thread is blocked in `acquire()` waiting for the state to turn to unlocked, only one thread proceeds when a `release()` call resets the state to unlocked; which one of the waiting threads proceeds is not defined, and may vary across implementations.

All methods are executed atomically.

<div class="methoddesc">

acquire Acquire a lock, blocking or non-blocking.

When invoked without arguments, block until the lock is unlocked, then set it to locked, and return. There is no return value in this case.

When invoked with the *blocking* argument set to true, do the same thing as when called without arguments, and return true.

When invoked with the *blocking* argument set to false, do not block. If a call without an argument would block, return false immediately; otherwise, do the same thing as when called without arguments, and return true.

</div>

<div class="methoddesc">

release Release a lock.

When the lock is locked, reset it to unlocked, and return. If any other threads are blocked waiting for the lock to become unlocked, allow exactly one of them to proceed.

Do not call this method when the lock is unlocked.

There is no return value.

</div>

## RLock Objects <span id="rlock-objects" label="rlock-objects"></span>

A reentrant lock is a synchronization primitive that may be acquired multiple times by the same thread. Internally, it uses the concepts of “owning thread” and “recursion level” in addition to the locked/unlocked state used by primitive locks. In the locked state, some thread owns the lock; in the unlocked state, no thread owns it.

To lock the lock, a thread calls its `acquire()` method; this returns once the thread owns the lock. To unlock the lock, a thread calls its `release()` method. `acquire()`/`release()` call pairs may be nested; only the final `release()` (i.e. the `release()` of the outermost pair) resets the lock to unlocked and allows another thread blocked in `acquire()` to proceed.

<div class="methoddesc">

acquire Acquire a lock, blocking or non-blocking.

When invoked without arguments: if this thread already owns the lock, increment the recursion level by one, and return immediately. Otherwise, if another thread owns the lock, block until the lock is unlocked. Once the lock is unlocked (not owned by any thread), then grab ownership, set the recursion level to one, and return. If more than one thread is blocked waiting until the lock is unlocked, only one at a time will be able to grab ownership of the lock. There is no return value in this case.

When invoked with the *blocking* argument set to true, do the same thing as when called without arguments, and return true.

When invoked with the *blocking* argument set to false, do not block. If a call without an argument would block, return false immediately; otherwise, do the same thing as when called without arguments, and return true.

</div>

<div class="methoddesc">

release Release a lock, decrementing the recursion level. If after the decrement it is zero, reset the lock to unlocked (not owned by any thread), and if any other threads are blocked waiting for the lock to become unlocked, allow exactly one of them to proceed. If after the decrement the recursion level is still nonzero, the lock remains locked and owned by the calling thread.

Only call this method when the calling thread owns the lock. Do not call this method when the lock is unlocked.

There is no return value.

</div>

## Condition Objects <span id="condition-objects" label="condition-objects"></span>

A condition variable is always associated with some kind of lock; this can be passed in or one will be created by default. (Passing one in is useful when several condition variables must share the same lock.)

A condition variable has `acquire()` and `release()` methods that call the corresponding methods of the associated lock. It also has a `wait()` method, and `notify()` and `notifyAll()` methods. These three must only be called when the calling thread has acquired the lock.

The `wait()` method releases the lock, and then blocks until it is awakened by a `notify()` or `notifyAll()` call for the same condition variable in another thread. Once awakened, it re-acquires the lock and returns. It is also possible to specify a timeout.

The `notify()` method wakes up one of the threads waiting for the condition variable, if any are waiting. The `notifyAll()` method wakes up all threads waiting for the condition variable.

Note: the `notify()` and `notifyAll()` methods don’t release the lock; this means that the thread or threads awakened will not return from their `wait()` call immediately, but only when the thread that called `notify()` or `notifyAll()` finally relinquishes ownership of the lock.

Tip: the typical programming style using condition variables uses the lock to synchronize access to some shared state; threads that are interested in a particular change of state call `wait()` repeatedly until they see the desired state, while threads that modify the state call `notify()` or `notifyAll()` when they change the state in such a way that it could possibly be a desired state for one of the waiters. For example, the following code is a generic producer-consumer situation with unlimited buffer capacity:

    # Consume one item
    cv.acquire()
    while not an_item_is_available():
        cv.wait()
    get_an_available_item()
    cv.release()

    # Produce one item
    cv.acquire()
    make_an_item_available()
    cv.notify()
    cv.release()

To choose between `notify()` and `notifyAll()`, consider whether one state change can be interesting for only one or several waiting threads. E.g. in a typical producer-consumer situation, adding one item to the buffer only needs to wake up one consumer thread.

<div class="classdesc">

Condition If the *lock* argument is given and not `None`, it must be a `Lock` or `RLock` object, and it is used as the underlying lock. Otherwise, a new `RLock` object is created and used as the underlying lock.

</div>

<div class="methoddesc">

acquire\*args Acquire the underlying lock. This method calls the corresponding method on the underlying lock; the return value is whatever that method returns.

</div>

<div class="methoddesc">

release Release the underlying lock. This method calls the corresponding method on the underlying lock; there is no return value.

</div>

<div class="methoddesc">

wait Wait until notified or until a timeout occurs. This must only be called when the calling thread has acquired the lock.

This method releases the underlying lock, and then blocks until it is awakened by a `notify()` or `notifyAll()` call for the same condition variable in another thread, or until the optional timeout occurs. Once awakened or timed out, it re-acquires the lock and returns.

When the *timeout* argument is present and not `None`, it should be a floating point number specifying a timeout for the operation in seconds (or fractions thereof).

When the underlying lock is an `RLock`, it is not released using its `release()` method, since this may not actually unlock the lock when it was acquired multiple times recursively. Instead, an internal interface of the `RLock` class is used, which really unlocks it even when it has been recursively acquired several times. Another internal interface is then used to restore the recursion level when the lock is reacquired.

</div>

<div class="methoddesc">

notify Wake up a thread waiting on this condition, if any. This must only be called when the calling thread has acquired the lock.

This method wakes up one of the threads waiting for the condition variable, if any are waiting; it is a no-op if no threads are waiting.

The current implementation wakes up exactly one thread, if any are waiting. However, it’s not safe to rely on this behavior. A future, optimized implementation may occasionally wake up more than one thread.

Note: the awakened thread does not actually return from its `wait()` call until it can reacquire the lock. Since `notify()` does not release the lock, its caller should.

</div>

<div class="methoddesc">

notifyAll Wake up all threads waiting on this condition. This method acts like `notify()`, but wakes up all waiting threads instead of one.

</div>

## Semaphore Objects <span id="semaphore-objects" label="semaphore-objects"></span>

This is one of the oldest synchronization primitives in the history of computer science, invented by the early Dutch computer scientist Edsger W. Dijkstra (he used `P()` and `V()` instead of `acquire()` and `release()`).

A semaphore manages an internal counter which is decremented by each `acquire()` call and incremented by each `release()` call. The counter can never go below zero; when `acquire()` finds that it is zero, it blocks, waiting until some other thread calls `release()`.

<div class="classdesc">

Semaphore The optional argument gives the initial value for the internal counter; it defaults to `1`.

</div>

<div class="methoddesc">

acquire Acquire a semaphore.

When invoked without arguments: if the internal counter is larger than zero on entry, decrement it by one and return immediately. If it is zero on entry, block, waiting until some other thread has called `release()` to make it larger than zero. This is done with proper interlocking so that if multiple `acquire()` calls are blocked, `release()` will wake exactly one of them up. The implementation may pick one at random, so the order in which blocked threads are awakened should not be relied on. There is no return value in this case.

When invoked with *blocking* set to true, do the same thing as when called without arguments, and return true.

When invoked with *blocking* set to false, do not block. If a call without an argument would block, return false immediately; otherwise, do the same thing as when called without arguments, and return true.

</div>

<div class="methoddesc">

release Release a semaphore, incrementing the internal counter by one. When it was zero on entry and another thread is waiting for it to become larger than zero again, wake up that thread.

</div>

## Event Objects <span id="event-objects" label="event-objects"></span>

This is one of the simplest mechanisms for communication between threads: one thread signals an event and one or more other threads are waiting for it.

An event object manages an internal flag that can be set to true with the `set()` method and reset to false with the `clear()` method. The `wait()` method blocks until the flag is true.

<div class="classdesc">

Event The internal flag is initially false.

</div>

<div class="methoddesc">

isSet Return true if and only if the internal flag is true.

</div>

<div class="methoddesc">

set Set the internal flag to true. All threads waiting for it to become true are awakened. Threads that call `wait()` once the flag is true will not block at all.

</div>

<div class="methoddesc">

clear Reset the internal flag to false. Subsequently, threads calling `wait()` will block until `set()` is called to set the internal flag to true again.

</div>

<div class="methoddesc">

wait Block until the internal flag is true. If the internal flag is true on entry, return immediately. Otherwise, block until another thread calls `set()` to set the flag to true, or until the optional timeout occurs.

When the timeout argument is present and not `None`, it should be a floating point number specifying a timeout for the operation in seconds (or fractions thereof).

</div>

## Thread Objects <span id="thread-objects" label="thread-objects"></span>

This class represents an activity that is run in a separate thread of control. There are two ways to specify the activity: by passing a callable object to the constructor, or by overriding the `run()` method in a subclass. No other methods (except for the constructor) should be overridden in a subclass. In other words, *only* override the `__init__()` and `run()` methods of this class.

Once a thread object is created, its activity must be started by calling the thread’s `start()` method. This invokes the `run()` method in a separate thread of control.

Once the thread’s activity is started, the thread is considered ’alive’ and ’active’ (these concepts are almost, but not quite exactly, the same; their definition is intentionally somewhat vague). It stops being alive and active when its `run()` method terminates – either normally, or by raising an unhandled exception. The `isAlive()` method tests whether the thread is alive.

Other threads can call a thread’s `join()` method. This blocks the calling thread until the thread whose `join()` method is called is terminated.

A thread has a name. The name can be passed to the constructor, set with the `setName()` method, and retrieved with the `getName()` method.

A thread can be flagged as a “daemon thread”. The significance of this flag is that the entire Python program exits when only daemon threads are left. The initial value is inherited from the creating thread. The flag can be set with the `setDaemon()` method and retrieved with the `getDaemon()` method.

There is a “main thread” object; this corresponds to the initial thread of control in the Python program. It is not a daemon thread.

There is the possibility that “dummy thread objects” are created. These are thread objects corresponding to “alien threads”. These are threads of control started outside the threading module, e.g. directly from C code. Dummy thread objects have limited functionality; they are always considered alive, active, and daemonic, and cannot be `join()`ed. They are never deleted, since it is impossible to detect the termination of alien threads.

<div class="classdesc">

Threadgroup=None, target=None, name=None, args=(), kwargs={} This constructor should always be called with keyword arguments. Arguments are:

*group* Should be `None`; reserved for future extension when a `ThreadGroup` class is implemented.

*target* Callable object to be invoked by the `run()` method. Defaults to `None`, meaning nothing is called.

*name* The thread name. By default, a unique name is constructed of the form “Thread-*N*” where *N* is a small decimal number.

*args* Argument tuple for the target invocation. Defaults to `()`.

*kwargs* Keyword argument dictionary for the target invocation. Defaults to `{}`.

If the subclass overrides the constructor, it must make sure to invoke the base class constructor (`Thread.__init__()`) before doing anything else to the thread.

</div>

<div class="methoddesc">

start Start the thread’s activity.

This must be called at most once per thread object. It arranges for the object’s `run()` method to be invoked in a separate thread of control.

</div>

<div class="methoddesc">

run Method representing the thread’s activity.

You may override this method in a subclass. The standard `run()` method invokes the callable object passed to the object’s constructor as the *target* argument, if any, with sequential and keyword arguments taken from the *args* and *kwargs* arguments, respectively.

</div>

<div class="methoddesc">

join Wait until the thread terminates. This blocks the calling thread until the thread whose `join()` method is called terminates – either normally or through an unhandled exception – or until the optional timeout occurs.

When the *timeout* argument is present and not `None`, it should be a floating point number specifying a timeout for the operation in seconds (or fractions thereof).

A thread can be `join()`ed many times.

A thread cannot join itself because this would cause a deadlock.

It is an error to attempt to `join()` a thread before it has been started.

</div>

<div class="methoddesc">

getName Return the thread’s name.

</div>

<div class="methoddesc">

setNamename Set the thread’s name.

The name is a string used for identification purposes only. It has no semantics. Multiple threads may be given the same name. The initial name is set by the constructor.

</div>

<div class="methoddesc">

isAlive Return whether the thread is alive.

Roughly, a thread is alive from the moment the `start()` method returns until its `run()` method terminates.

</div>

<div class="methoddesc">

isDaemon Return the thread’s daemon flag.

</div>

<div class="methoddesc">

setDaemondaemonic Set the thread’s daemon flag to the Boolean value *daemonic*. This must be called before `start()` is called.

The initial value is inherited from the creating thread.

The entire Python program exits when no active non-daemon threads are left.

</div>
# `tokenize` — Tokenizer for Python source

*Lexical scanner for Python source code.*\
The `tokenize` module provides a lexical scanner for Python source code, implemented in Python. The scanner in this module returns comments as tokens as well, making it useful for implementing “pretty-printers,” including colorizers for on-screen displays.

The scanner is exposed by a single function:

<div class="funcdesc">

tokenizereadline The `tokenize()` function accepts two parameters: one representing the input stream, and one providing an output mechanism for `tokenize()`.

The first parameter, *readline*, must be a callable object which provides the same interface as the `readline()` method of built-in file objects (see section <a href="#bltin-file-objects" data-reference-type="ref" data-reference="bltin-file-objects">[bltin-file-objects]</a>). Each call to the function should return one line of input as a string.

The second parameter, *tokeneater*, must also be a callable object. It is called with five parameters: the token type, the token string, a tuple `(`*`srow`*`, `*`scol`*`)` specifying the row and column where the token begins in the source, a tuple `(`*`erow`*`, `*`ecol`*`)` giving the ending position of the token, and the line on which the token was found. The line passed is the *logical* line; continuation lines are included.

</div>

All constants from the `token` module are also exported from `tokenize`, as is one additional token type value that might be passed to the *tokeneater* function by `tokenize()`:

<div class="datadesc">

COMMENT Token value used to indicate a comment.

</div>
# `traceback` — Print or retrieve a stack traceback

*Print or retrieve a stack traceback.*\
This module provides a standard interface to extract, format and print stack traces of Python programs. It exactly mimics the behavior of the Python interpreter when it prints a stack trace. This is useful when you want to print stack traces under program control, e.g. in a “wrapper” around the interpreter.

The module uses traceback objects — this is the object type that is stored in the variables `sys.exc_traceback` and `sys.last_traceback` and returned as the third item from `sys.exc_info()`. The module defines the following functions:

<div class="funcdesc">

print_tbtraceback Print up to *limit* stack trace entries from *traceback*. If *limit* is omitted or `None`, all entries are printed. If *file* is omitted or `None`, the output goes to `sys.stderr`; otherwise it should be an open file or file-like object to receive the output.

</div>

<div class="funcdesc">

print_exceptiontype, value, traceback Print exception information and up to *limit* stack trace entries from *traceback* to *file*. This differs from `print_tb()` in the following ways: (1) if *traceback* is not `None`, it prints a header `Traceback (innermost last):`; (2) it prints the exception *type* and *value* after the stack trace; (3) if *type* is `SyntaxError` and *value* has the appropriate format, it prints the line where the syntax error occurred with a caret indicating the approximate position of the error.

</div>

<div class="funcdesc">

print_exc This is a shorthand for ‘`print_exception(sys.exc_type,` `sys.exc_value,` `sys.exc_traceback,` *limit*`,` *file*`)`’. (In fact, it uses `sys.exc_info()` to retrieve the same information in a thread-safe way.)

</div>

<div class="funcdesc">

print_last This is a shorthand for ‘`print_exception(sys.last_type,` `sys.last_value,` `sys.last_traceback,` *limit*`,` *file*`)`’.

</div>

<div class="funcdesc">

print_stack This function prints a stack trace from its invocation point. The optional *f* argument can be used to specify an alternate stack frame to start. The optional *limit* and *file* arguments have the same meaning as for `print_exception()`.

</div>

<div class="funcdesc">

extract_tbtraceback Return a list of up to *limit* “pre-processed” stack trace entries extracted from the traceback object *traceback*. It is useful for alternate formatting of stack traces. If *limit* is omitted or `None`, all entries are extracted. A “pre-processed” stack trace entry is a quadruple (*filename*, *line number*, *function name*, *text*) representing the information that is usually printed for a stack trace. The *text* is a string with leading and trailing whitespace stripped; if the source is not available it is `None`.

</div>

<div class="funcdesc">

extract_stack Extract the raw traceback from the current stack frame. The return value has the same format as for `extract_tb()`. The optional *f* and *limit* arguments have the same meaning as for `print_stack()`.

</div>

<div class="funcdesc">

format_listlist Given a list of tuples as returned by `extract_tb()` or `extract_stack()`, return a list of strings ready for printing. Each string in the resulting list corresponds to the item with the same index in the argument list. Each string ends in a newline; the strings may contain internal newlines as well, for those items whose source text line is not `None`.

</div>

<div class="funcdesc">

format_exception_onlytype, value Format the exception part of a traceback. The arguments are the exception type and value such as given by `sys.last_type` and `sys.last_value`. The return value is a list of strings, each ending in a newline. Normally, the list contains a single string; however, for `SyntaxError` exceptions, it contains several lines that (when printed) display detailed information about where the syntax error occurred. The message indicating which exception occurred is the always last string in the list.

</div>

<div class="funcdesc">

format_exceptiontype, value, tb Format a stack trace and the exception information. The arguments have the same meaning as the corresponding arguments to `print_exception()`. The return value is a list of strings, each ending in a newline and some containing internal newlines. When these lines are concatenated and printed, exactly the same text is printed as does `print_exception()`.

</div>

<div class="funcdesc">

format_tbtb A shorthand for `format_list(extract_tb(`*`tb`*`, `*`limit`*`))`.

</div>

<div class="funcdesc">

format_stack A shorthand for `format_list(extract_stack(`*`f`*`, `*`limit`*`))`.

</div>

<div class="funcdesc">

tb_linenotb This function returns the current line number set in the traceback object. This is normally the same as the *`tb`*`.tb_lineno` field of the object, but when optimization is used (the -O flag) this field is not updated correctly; this function calculates the correct value.

</div>

## Traceback Example <span id="traceback-example" label="traceback-example"></span>

This simple example implements a basic read-eval-print loop, similar to (but less useful than) the standard Python interactive interpreter loop. For a more complete implementation of the interpreter loop, refer to the `code` module.

    import sys, traceback

    def run_user_code(envdir):
        source = raw_input(">>> ")
        try:
            exec source in envdir
        except:
            print "Exception in user code:"
            print '-'*60
            traceback.print_exc(file=sys.stdout)
            print '-'*60

    envdir = {}
    while 1:
        run_user_code(envdir)
# `turtle` — Turtle graphics for Tk

*An environment for turtle graphics.*\
The `turtle` module provides turtle graphics primitives, in both an object-oriented and procedure-oriented ways. Because it uses `Tkinter` for the underlying graphics, it needs a version of python installed with Tk support.

The procedural interface uses a pen and a canvas which are automagically created when any of the functions are called.

The `turtle` module defines the following functions:

<div class="funcdesc">

degrees Set angle measurement units to degrees.

</div>

<div class="funcdesc">

radians Set angle measurement units to radians.

</div>

<div class="funcdesc">

reset Clear the screen, re-center the pen, and set variables to the default values.

</div>

<div class="funcdesc">

clear Clear the screen.

</div>

<div class="funcdesc">

tracerflag Set tracing on/off (according to whether flag is true or not). Tracing means line are drawn more slowly, with an animation of an arrow along the line.

</div>

<div class="funcdesc">

forwarddistance Go forward *distance* steps.

</div>

<div class="funcdesc">

backwarddistance Go backward *distance* steps.

</div>

<div class="funcdesc">

leftangle Turn left *angle* units. Units are by default degrees, but can be set via the `degrees()` and `radians()` functions.

</div>

<div class="funcdesc">

rightangle Turn right *angle* units. Units are by default degrees, but can be set via the `degrees()` and `radians()` functions.

</div>

<div class="funcdesc">

up Move the pen up — stop drawing.

</div>

<div class="funcdesc">

down Move the pen up — draw when moving.

</div>

<div class="funcdesc">

widthwidth Set the line width to *width*.

</div>

<div class="funcdesc">

colors Set the color by giving a Tk color string.

</div>

<div class="funcdesc">

color(r, g, b) Set the color by giving a RGB tuple, each between 0 and 1.

</div>

<div class="funcdesc">

colorr, g, b Set the color by giving the RGB components, each between 0 and 1.

</div>

<div class="funcdesc">

writetext Write *text* at the current pen position. If *move* is true, the pen is moved to the bottom-right corner of the text. By default, *move* is false.

</div>

<div class="funcdesc">

fillflag The complete specifications are rather complex, but the recommended usage is: call `fill(1)` before drawing a path you want to fill, and call `fill(0)` when you finish to draw the path.

</div>

<div class="funcdesc">

circleradius Draw a circle with radius *radius* whose center-point is where the pen would be if a `forward(`*`radius`*`)` were called. *extent* determines which part of a circle is drawn: if not given it defaults to a full circle.

If *extent* is not a full circle, one endpoint of the arc is the current pen position. The arc is drawn in a counter clockwise direction if *radius* is positive, otherwise in a clockwise direction.

</div>

<div class="funcdesc">

gotox, y Go to co-ordinates (*x*, *y*).

</div>

<div class="funcdesc">

goto(x, y) Go to co-ordinates (*x*, *y*) (specified as a tuple instead of individually).

</div>

This module also does `from math import *`, so see the documentation for the `math` module for additional constants and functions useful for turtle graphics.

<div class="funcdesc">

demo Exercise the module a bit.

</div>

<div class="excdesc">

Error Exception raised on any error caught by this module.

</div>

For examples, see the code of the `demo()` function.

This module defines the following classes:

<div class="classdesc">

Pen Define a pen. All above functions can be called as a methods on the given pen. The constructor automatically creates a canvas do be drawn on.

</div>

<div class="classdesc">

RawPencanvas Define a pen which draws on a canvas *canvas*. This is useful if you want to use the module to create graphics in a “real” program.

</div>

## Pen and RawPen Objects <span id="pen-rawpen-objects" label="pen-rawpen-objects"></span>

`Pen` and `RawPen` objects have all the global functions described above, except for `demo()` as methods, which manipulate the given pen.

The only method which is more powerful as a method is `degrees()`.

<div class="methoddesc">

degrees *fullcircle* is by default 360. This can cause the pen to have any angular units whatever: give *fullcircle* 2\*$`\pi`$ for radians, or 400 for gradians.

</div>
# `types` — Names for all built-in types

*Names for all built-in types.*\
This module defines names for all object types that are used by the standard Python interpreter, but not for the types defined by various extension modules. It is safe to use `from types import *` — the module does not export any names besides the ones listed here. New names exported by future versions of this module will all end in `Type`.

Typical use is for functions that do different things depending on their argument types, like the following:

    from types import *
    def delete(list, item):
        if type(item) is IntType:
           del list[item]
        else:
           list.remove(item)

The module defines the following names:

<div class="datadesc">

NoneType The type of `None`.

</div>

<div class="datadesc">

TypeType The type of type objects (such as returned by `type()`).

</div>

<div class="datadesc">

IntType The type of integers (e.g. `1`).

</div>

<div class="datadesc">

LongType The type of long integers (e.g. `1L`).

</div>

<div class="datadesc">

FloatType The type of floating point numbers (e.g. `1.0`).

</div>

<div class="datadesc">

ComplexType The type of complex numbers (e.g. `1.0j`).

</div>

<div class="datadesc">

StringType The type of character strings (e.g. `’Spam’`).

</div>

<div class="datadesc">

UnicodeType The type of Unicode character strings (e.g. `u’Spam’`).

</div>

<div class="datadesc">

TupleType The type of tuples (e.g. `(1, 2, 3, ’Spam’)`).

</div>

<div class="datadesc">

ListType The type of lists (e.g. `[0, 1, 2, 3]`).

</div>

<div class="datadesc">

DictType The type of dictionaries (e.g. `{’Bacon’: 1, ’Ham’: 0}`).

</div>

<div class="datadesc">

DictionaryType An alternate name for `DictType`.

</div>

<div class="datadesc">

FunctionType The type of user-defined functions and lambdas.

</div>

<div class="datadesc">

LambdaType An alternate name for `FunctionType`.

</div>

<div class="datadesc">

CodeType The type for code objects such as returned by `compile()`.

</div>

<div class="datadesc">

ClassType The type of user-defined classes.

</div>

<div class="datadesc">

InstanceType The type of instances of user-defined classes.

</div>

<div class="datadesc">

MethodType The type of methods of user-defined class instances.

</div>

<div class="datadesc">

UnboundMethodType An alternate name for `MethodType`.

</div>

<div class="datadesc">

BuiltinFunctionType The type of built-in functions like `len()` or `sys.exit()`.

</div>

<div class="datadesc">

BuiltinMethodType An alternate name for `BuiltinFunction`.

</div>

<div class="datadesc">

ModuleType The type of modules.

</div>

<div class="datadesc">

FileType The type of open file objects such as `sys.stdout`.

</div>

<div class="datadesc">

XRangeType The type of range objects returned by `xrange()`.

</div>

<div class="datadesc">

SliceType The type of objects returned by `slice()`.

</div>

<div class="datadesc">

EllipsisType The type of `Ellipsis`.

</div>

<div class="datadesc">

TracebackType The type of traceback objects such as found in `sys.exc_traceback`.

</div>

<div class="datadesc">

FrameType The type of frame objects such as found in `tb.tb_frame` if `tb` is a traceback object.

</div>

<div class="datadesc">

BufferType The type of buffer objects created by the `buffer()`function.

</div>
# Undocumented Modules <span id="undoc" label="undoc"></span>

Here’s a quick listing of modules that are currently undocumented, but that should be documented. Feel free to contribute documentation for them! (Send via email to `python-docs@python.org`.)

The idea and original contents for this chapter were taken from a posting by Fredrik Lundh; the specific contents of this chapter have been substantially revised.

## Frameworks

Frameworks tend to be harder to document, but are well worth the effort spent.

`Tkinter`  
— Interface to Tcl/Tk for graphical user interfaces; Fredrik Lundh is working on this one! See An Introduction to Tkinter at `http://www.pythonware.com/library.htm` for on-line reference material.

`Tkdnd`  
— Drag-and-drop support for `Tkinter`.

`turtle`  
— Turtle graphics in a Tk window.

`test`  
— Regression testing framework. This is used for the Python regression test, but is useful for other Python libraries as well. This is a package rather than a single module.

## Miscellaneous useful utilities

Some of these are very old and/or not very robust; marked with “hmm.”

`bdb`  
— A generic Python debugger base class (used by pdb).

`ihooks`  
— Import hook support (for `rexec`; may become obsolete).

`tzparse`  
— Parse a timezone specification (unfinished; may disappear in the future).

## Platform specific modules

These modules are used to implement the `os.path` module, and are not documented beyond this mention. There’s little need to document these.

`dospath`  
— Implementation of `os.path` on MS-DOS.

`ntpath`  
— Implementation on `os.path` on Win32, Win64, WinCE, and OS/2 platforms.

`posixpath`  
— Implementation on `os.path` on .

## Multimedia

`audiodev`  
— Platform-independent API for playing audio data.

`sunaudio`  
— Interpret Sun audio headers (may become obsolete or a tool/demo).

`toaiff`  
— Convert "arbitrary" sound files to AIFF files; should probably become a tool or demo. Requires the external program .

## Obsolete <span id="obsolete-modules" label="obsolete-modules"></span>

These modules are not normally available for import; additional work must be done to make them available.

Those which are written in Python will be installed into the directory `lib-old/` installed as part of the standard library. To use these, the directory must be added to `sys.path`, possibly using .

Obsolete extension modules written in C are not built by default. Under Unix, these must be enabled by uncommenting the appropriate lines in `Modules/Setup` in the build tree and either rebuilding Python if the modules are statically linked, or building and installing the shared object if using dynamically-loaded extensions.

`addpack`  
— Alternate approach to packages. Use the built-in package support instead.

`cmp`  
— File comparison function. Use the newer `filecmp` instead.

`cmpcache`  
— Caching version of the obsolete `cmp` module. Use the newer `filecmp` instead.

`codehack`  
— Extract function name or line number from a function code object (these are now accessible as attributes: `co.co_name`, `func.func_name`, `co.co_firstlineno`).

`dircmp`  
— Class to build directory diff tools on (may become a demo or tool). *Deprecated since version 2.0: The `filecmp` module replaces `dircmp`.*

`dump`  
— Print python code that reconstructs a variable.

`fmt`  
— Text formatting abstractions (too slow).

`lockfile`  
— Wrapper around FCNTL file locking (use `fcntl.lockf()`/`flock()` instead; see `fcntl`).

`newdir`  
— New `dir()` function (the standard `dir()` is now just as good).

`Para`  
— Helper for `fmt`.

`poly`  
— Polynomials.

`tb`  
— Print tracebacks, with a dump of local variables (use `pdb.pm()` or `traceback` instead).

`timing`  
— Measure time intervals to high resolution (use `time.clock()` instead). (This is an extension module.)

`util`  
— Useful functions that don’t fit elsewhere.

`whatsound`  
— Recognize sound files; use `sndhdr` instead.

`zmod`  
— Compute properties of mathematical “fields.”

The following modules are obsolete, but are likely to re-surface as tools or scripts:

`find`  
— Find files matching pattern in directory tree.

`grep`  
— implementation in Python.

`packmail`  
— Create a self-unpacking Unix shell archive.

The following modules were documented in previous versions of this manual, but are now considered obsolete. The source for the documentation is still available as part of the documentation source archive.

`ni`  
— Import modules in “packages.” Basic package support is now built in. The built-in support is very similar to what is provided in this module.

`rand`  
— Old interface to the random number generator.

`soundex`  
— Algorithm for collapsing names which sound similar to a shared key. The specific algorithm doesn’t seem to match any published algorithm. (This is an extension module.)

## SGI-specific Extension modules

The following are SGI specific, and may be out of touch with the current version of reality.

`cl`  
— Interface to the SGI compression library.

`sv`  
— Interface to the “simple video” board on SGI Indigo (obsolete hardware).
# `unicodedata` — Unicode Database

*Access the Unicode Database.*\
This module provides access to the Unicode Character Database which defines character properties for all Unicode characters. The data in this database is based on the `UnicodeData.txt` file version 3.0.0 which is publically available from `ftp://ftp.unicode.org/`.

The module uses the same names and symbols as defined by the UnicodeData File Format 3.0.0 (see `http://www.unicode.org/Public/UNIDATA/UnicodeData.html`). It defines the following functions:

<div class="funcdesc">

decimalunichr Returns the decimal value assigned to the Unicode character *unichr* as integer. If no such value is defined, *default* is returned, or, if not given, `ValueError` is raised.

</div>

<div class="funcdesc">

digitunichr Returns the digit value assigned to the Unicode character *unichr* as integer. If no such value is defined, *default* is returned, or, if not given, `ValueError` is raised.

</div>

<div class="funcdesc">

numericunichr Returns the numeric value assigned to the Unicode character *unichr* as float. If no such value is defined, *default* is returned, or, if not given, `ValueError` is raised.

</div>

<div class="funcdesc">

categoryunichr Returns the general category assigned to the Unicode character *unichr* as string.

</div>

<div class="funcdesc">

bidirectionalunichr Returns the bidirectional category assigned to the Unicode character *unichr* as string. If no such value is defined, an empty string is returned.

</div>

<div class="funcdesc">

combiningunichr Returns the canonical combining class assigned to the Unicode character *unichr* as integer. Returns `0` if no combining class is defined.

</div>

<div class="funcdesc">

mirroredunichr Returns the mirrored property of assigned to the Unicode character *unichr* as integer. Returns `1` if the character has been identified as a “mirrored” character in bidirectional text, `0` otherwise.

</div>

<div class="funcdesc">

decompositionunichr Returns the character decomposition mapping assigned to the Unicode character *unichr* as string. An empty string is returned in case no such mapping is defined.

</div>
# Unix Specific Services

The modules described in this chapter provide interfaces to features that are unique to the Unix operating system, or in some cases to some or many variants of it. Here’s an overview:
# `urllib` — Open arbitrary resources by URL

*Open an arbitrary network resource by URL (requires sockets).*\
This module provides a high-level interface for fetching data across the World-Wide Web. In particular, the `urlopen()` function is similar to the built-in function `open()`, but accepts Universal Resource Locators (URLs) instead of filenames. Some restrictions apply — it can only open URLs for reading, and no seek operations are available.

It defines the following public functions:

<div class="funcdesc">

urlopenurl Open a network object denoted by a URL for reading. If the URL does not have a scheme identifier, or if it has `file:` as its scheme identifier, this opens a local file; otherwise it opens a socket to a server somewhere on the network. If the connection cannot be made, or if the server returns an error code, the `IOError` exception is raised. If all went well, a file-like object is returned. This supports the following methods: `read()`, `readline()`, `readlines()`, `fileno()`, `close()`, `info()` and `geturl()`.

Except for the `info()` and `geturl()` methods, these methods have the same interface as for file objects — see section <a href="#bltin-file-objects" data-reference-type="ref" data-reference="bltin-file-objects">[bltin-file-objects]</a> in this manual. (It is not a built-in file object, however, so it can’t be used at those few places where a true built-in file object is required.)

The `info()` method returns an instance of the class `mimetools.Message` containing meta-information associated with the URL. When the method is HTTP, these headers are those returned by the server at the head of the retrieved HTML page (including Content-Length and Content-Type). When the method is FTP, a Content-Length header will be present if (as is now usual) the server passed back a file length in response to the FTP retrieval request. When the method is local-file, returned headers will include a Date representing the file’s last-modified time, a Content-Length giving file size, and a Content-Type containing a guess at the file’s type. See also the description of the `mimetools`module.

The `geturl()` method returns the real URL of the page. In some cases, the HTTP server redirects a client to another URL. The `urlopen()` function handles this transparently, but in some cases the caller needs to know which URL the client was redirected to. The `geturl()` method can be used to get at this redirected URL.

If the *url* uses the `http:` scheme identifier, the optional *data* argument may be given to specify a `POST` request (normally the request type is `GET`). The *data* argument must in standard `application/x-www-form-urlencoded` format; see the `urlencode()` function below.

The `urlopen()` function works transparently with proxies which do not require authentication. In a Unix or Windows environment, set the , or environment variables to a URL that identifies the proxy server before starting the Python interpreter. For example (the is the command prompt):

    % http_proxy="http://www.someproxy.com:3128"
    % export http_proxy
    % python
    ...

In a Macintosh environment, `urlopen()` will retrieve proxy information from InternetConfig.

Proxies which require authentication for use are not currently supported; this is considered an implementation limitation.

The `urlopen()` function works transparently with proxies. In a Unix or Windows environment, set the , or environment variables to a URL that identifies the proxy server before starting the Python interpreter, e.g.:

    % http_proxy="http://www.someproxy.com:3128"
    % export http_proxy
    % python
    ...

In a Macintosh environment, `urlopen()` will retrieve proxy information from Internet Config.

</div>

<div class="funcdesc">

urlretrieveurl Copy a network object denoted by a URL to a local file, if necessary. If the URL points to a local file, or a valid cached copy of the object exists, the object is not copied. Return a tuple `(`*`filename`*`, `*`headers`*`)` where *filename* is the local file name under which the object can be found, and *headers* is either `None` (for a local object) or whatever the `info()` method of the object returned by `urlopen()` returned (for a remote object, possibly cached). Exceptions are the same as for `urlopen()`.

The second argument, if present, specifies the file location to copy to (if absent, the location will be a tempfile with a generated name). The third argument, if present, is a hook function that will be called once on establishment of the network connection and once after each block read thereafter. The hook will be passed three arguments; a count of blocks transferred so far, a block size in bytes, and the total size of the file. The third argument may be `-1` on older FTP servers which do not return a file size in response to a retrieval request.

If the *url* uses the `http:` scheme identifier, the optional *data* argument may be given to specify a `POST` request (normally the request type is `GET`). The *data* argument must in standard `application/x-www-form-urlencoded` format; see the `urlencode()` function below.

</div>

<div class="funcdesc">

urlcleanup Clear the cache that may have been built up by previous calls to `urlretrieve()`.

</div>

<div class="funcdesc">

quotestring Replace special characters in *string* using the `%xx` escape. Letters, digits, and the characters are never quoted. The optional *safe* parameter specifies additional characters that should not be quoted — its default value is `’/’`.

Example: `quote(’/~connolly/’)` yields `’/%7econnolly/’`.

</div>

<div class="funcdesc">

quote_plusstring Like `quote()`, but also replaces spaces by plus signs, as required for quoting HTML form values. Plus signs in the original string are escaped unless they are included in *safe*.

</div>

<div class="funcdesc">

unquotestring Replace `%xx` escapes by their single-character equivalent.

Example: `unquote(’/%7Econnolly/’)` yields `’/~connolly/’`.

</div>

<div class="funcdesc">

unquote_plusstring Like `unquote()`, but also replaces plus signs by spaces, as required for unquoting HTML form values.

</div>

<div class="funcdesc">

urlencodedict Convert a dictionary to a “url-encoded” string, suitable to pass to `urlopen()` above as the optional *data* argument. This is useful to pass a dictionary of form fields to a `POST` request. The resulting string is a series of *`key`*`=`*`value`* pairs separated by characters, where both *key* and *value* are quoted using `quote_plus()` above.

</div>

The public functions `urlopen()` and `urlretrieve()` create an instance of the `FancyURLopener` class and use it to perform their requested actions. To override this functionality, programmers can create a subclass of `URLopener` or `FancyURLopener`, then assign that an instance of that class to the `urllib._urlopener` variable before calling the desired function. For example, applications may want to specify a different `user-agent` header than `URLopener` defines. This can be accomplished with the following code:

    class AppURLopener(urllib.FancyURLopener):
        def __init__(self, *args):
            self.version = "App/1.7"
            apply(urllib.FancyURLopener.__init__, (self,) + args)

    urllib._urlopener = AppURLopener()

<div class="classdesc">

URLopener Base class for opening and reading URLs. Unless you need to support opening objects using schemes other than `http:`, `ftp:`, `gopher:` or `file:`, you probably want to use `FancyURLopener`.

By default, the `URLopener` class sends a `user-agent` header of `urllib/`*`VVV`*, where *VVV* is the `urllib` version number. Applications can define their own `user-agent` header by subclassing `URLopener` or `FancyURLopener` and setting the instance attribute `version` to an appropriate string value before the `open()` method is called.

Additional keyword parameters, collected in *x509*, are used for authentication with the `https:` scheme. The keywords *key_file* and *cert_file* are supported; both are needed to actually retrieve a resource at an `https:` URL.

</div>

<div class="classdesc">

FancyURLopener... `FancyURLopener` subclasses `URLopener` providing default handling for the following HTTP response codes: 301, 302 or 401. For 301 and 302 response codes, the `location` header is used to fetch the actual URL. For 401 response codes (authentication required), basic HTTP authentication is performed.

The parameters to the constructor are the same as those for `URLopener`.

</div>

Restrictions:

- Currently, only the following protocols are supported: HTTP, (versions 0.9 and 1.0), Gopher (but not Gopher-+), FTP, and local files.

- The caching feature of `urlretrieve()` has been disabled until I find the time to hack proper processing of Expiration time headers.

- There should be a function to query whether a particular URL is in the cache.

- For backward compatibility, if a URL appears to point to a local file but the file can’t be opened, the URL is re-interpreted using the FTP protocol. This can sometimes cause confusing error messages.

- The `urlopen()` and `urlretrieve()` functions can cause arbitrarily long delays while waiting for a network connection to be set up. This means that it is difficult to build an interactive web client using these functions without using threads.

- The data returned by `urlopen()` or `urlretrieve()` is the raw data returned by the server. This may be binary data (e.g. an image), plain text or (for example) HTML. The HTTPprotocol provides type information in the reply header, which can be inspected by looking at the `content-type` header. For the Gopherprotocol, type information is encoded in the URL; there is currently no easy way to extract it. If the returned data is HTML, you can use the module `htmllib`to parse it.

- This module does not support the use of proxies which require authentication. This may be implemented in the future.

- Although the `urllib` module contains (undocumented) routines to parse and unparse URL strings, the recommended interface for URL manipulation is in module `urlparse`.

## URLopener Objects <span id="urlopener-objs" label="urlopener-objs"></span>

`URLopener` and `FancyURLopener` objects have the following attributes.

<div class="methoddesc">

openfullurl Open *fullurl* using the appropriate protocol. This method sets up cache and proxy information, then calls the appropriate open method with its input arguments. If the scheme is not recognized, `open_unknown()` is called. The *data* argument has the same meaning as the *data* argument of `urlopen()`.

</div>

<div class="methoddesc">

open_unknownfullurl Overridable interface to open unknown URL types.

</div>

<div class="methoddesc">

retrieveurl Retrieves the contents of *url* and places it in *filename*. The return value is a tuple consisting of a local filename and either a `mimetools.Message` object containing the response headers (for remote URLs) or None (for local URLs). The caller must then open and read the contents of *filename*. If *filename* is not given and the URL refers to a local file, the input filename is returned. If the URL is non-local and *filename* is not given, the filename is the output of `tempfile.mktemp()` with a suffix that matches the suffix of the last path component of the input URL. If *reporthook* is given, it must be a function accepting three numeric parameters. It will be called after each chunk of data is read from the network. *reporthook* is ignored for local URLs.

If the *url* uses the `http:` scheme identifier, the optional *data* argument may be given to specify a `POST` request (normally the request type is `GET`). The *data* argument must in standard `application/x-www-form-urlencoded` format; see the `urlencode()` function below.

</div>

<div class="memberdesc">

version Variable that specifies the user agent of the opener object. To get `urllib` to tell servers that it is a particular user agent, set this in a subclass as a class variable or in the constructor before calling the base constructor.

</div>

## Examples

Here is an example session that uses the `GET` method to retrieve a URL containing parameters:

    >>> import urllib
    >>> params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
    >>> f = urllib.urlopen("http://www.musi-cal.com/cgi-bin/query?%s" % params)
    >>> print f.read()

The following example uses the `POST` method instead:

    >>> import urllib
    >>> params = urllib.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
    >>> f = urllib.urlopen("http://www.musi-cal.com/cgi-bin/query", params)
    >>> print f.read()
# `UserDict` — Class wrapper for dictionary objects

*Class wrapper for dictionary objects.*\
This module defines a class that acts as a wrapper around dictionary objects. It is a useful base class for your own dictionary-like classes, which can inherit from them and override existing methods or add new ones. In this way one can add new behaviors to dictionaries.

The `UserDict` module defines the `UserDict` class:

<div class="classdesc">

UserDict Return a class instance that simulates a dictionary. The instance’s contents are kept in a regular dictionary, which is accessible via the `data` attribute of `UserDict` instances. If *initialdata* is provided, `data` is initialized with its contents; note that a reference to *initialdata* will not be kept, allowing it be used used for other purposes.

</div>

In addition to supporting the methods and operations of mappings (see section <a href="#typesmapping" data-reference-type="ref" data-reference="typesmapping">[typesmapping]</a>), `UserDict` instances provide the following attribute:

<div class="memberdesc">

data A real dictionary used to store the contents of the `UserDict` class.

</div>

# `UserList` — Class wrapper for list objects

*Class wrapper for list objects.*\
This module defines a class that acts as a wrapper around list objects. It is a useful base class for your own list-like classes, which can inherit from them and override existing methods or add new ones. In this way one can add new behaviors to lists.

The `UserList` module defines the `UserList` class:

<div class="classdesc">

UserList Return a class instance that simulates a list. The instance’s contents are kept in a regular list, which is accessible via the `data` attribute of `UserList` instances. The instance’s contents are initially set to a copy of *list*, defaulting to the empty list `[]`. *list* can be either a regular Python list, or an instance of `UserList` (or a subclass).

</div>

In addition to supporting the methods and operations of mutable sequences (see section <a href="#typesseq" data-reference-type="ref" data-reference="typesseq">[typesseq]</a>), `UserList` instances provide the following attribute:

<div class="memberdesc">

data A real Python list object used to store the contents of the `UserList` class.

</div>

# `UserString` — Class wrapper for string objects

*Class wrapper for string objects.*\
This module defines a class that acts as a wrapper around string objects. It is a useful base class for your own string-like classes, which can inherit from them and override existing methods or add new ones. In this way one can add new behaviors to strings.

The `UserString` module defines the `UserString` class:

<div class="classdesc">

UserString Return a class instance that simulates a string or a Unicode string object. The instance’s content is kept in a regular string or Unicode string object, which is accessible via the `data` attribute of `UserString` instances. The instance’s contents are initially set to a copy of *sequence*. *sequence* can be either a regular Python string or Unicode string, an instance of `UserString` (or a subclass) or an arbitrary sequence which can be converted into a string.

</div>

<div class="classdesc">

MutableString This class is derived from the `UserString` above and redefines strings to be *mutable*. Mutable strings can’t be used as dictionary keys, because dictionaries require *immutable* objects as keys. The main intention of this class is to serve as an educational example for inheritance and necessity to remove (override) the `__hash__` method in order to trap attempts to use a mutable object as dictionary key, which would be otherwise very error prone and hard to track down.

</div>

In addition to supporting the methods and operations of string or Unicode objects (see section <a href="#typesseq" data-reference-type="ref" data-reference="typesseq">[typesseq]</a>), `UserString` instances provide the following attribute:

<div class="memberdesc">

data A real Python string or Unicode object used to store the content of the `UserString` class.

</div>
# `wave` — Read and write WAV files

*Provide an interface to the WAV sound format.*\
The `wave` module provides a convenient interface to the WAV sound format. It does not support compression/decompression, but it does support mono/stereo.

The `wave` module defines the following function and exception:

<div class="funcdesc">

openfile If *file* is a string, open the file by that name, other treat it as a seekable file-like object. *mode* can be any of

`’r’`, `’rb’`  
Read only mode.

`’w’`, `’wb’`  
Write only mode.

Note that it does not allow read/write WAV files.

A *mode* of `’r’` or `’rb’` returns a `Wave_read` object, while a *mode* of `’w’` or `’wb’` returns a `Wave_write` object. If *mode* is omitted and a file-like object is passed as *file*, *`file`*`.mode` is used as the default value for *mode* (the flag is still added if necessary).

</div>

<div class="funcdesc">

openfpfile, mode A synonym for `open()`, maintained for backwards compatibility.

</div>

<div class="excdesc">

Error An error raised when something is impossible because it violates the WAV specification or hits an implementation deficiency.

</div>

## Wave_read Objects <span id="Wave-read-objects" label="Wave-read-objects"></span>

Wave_read objects, as returned by `open()`, have the following methods:

<div class="methoddesc">

close Close the stream, and make the instance unusable. This is called automatically on object collection.

</div>

<div class="methoddesc">

getnchannels Returns number of audio channels (`1` for mono, `2` for stereo).

</div>

<div class="methoddesc">

getsampwidth Returns sample width in bytes.

</div>

<div class="methoddesc">

getframerate Returns sampling frequency.

</div>

<div class="methoddesc">

getnframes Returns number of audio frames.

</div>

<div class="methoddesc">

getcomptype Returns compression type (`’NONE’` is the only supported type).

</div>

<div class="methoddesc">

getcompname Human-readable version of `getcomptype()`. Usually `’not compressed’` parallels `’NONE’`.

</div>

<div class="methoddesc">

getparams Returns a tuple `(`*`nchannels`*`, `*`sampwidth`*`, `*`framerate`*`, `*`nframes`*`, `*`comptype`*`, `*`compname`*`)`, equivalent to output of the `get*()` methods.

</div>

<div class="methoddesc">

readframesn Reads and returns at most *n* frames of audio, as a string of bytes.

</div>

<div class="methoddesc">

rewind Rewind the file pointer to the beginning of the audio stream.

</div>

The following two methods are defined for compatibility with the `aifc` module, and don’t do anything interesting.

<div class="methoddesc">

getmarkers Returns `None`.

</div>

<div class="methoddesc">

getmarkid Raise an error.

</div>

The following two methods define a term “position” which is compatible between them, and is otherwise implementation dependent.

<div class="methoddesc">

setpospos Set the file pointer to the specified position.

</div>

<div class="methoddesc">

tell Return current file pointer position.

</div>

## Wave_write Objects <span id="Wave-write-objects" label="Wave-write-objects"></span>

Wave_write objects, as returned by `open()`, have the following methods:

<div class="methoddesc">

close Make sure *nframes* is correct, and close the file. This method is called upon deletion.

</div>

<div class="methoddesc">

setnchannelsn Set the number of channels.

</div>

<div class="methoddesc">

setsampwidthn Set the sample width to *n* bytes.

</div>

<div class="methoddesc">

setframeraten Set the frame rate to *n*.

</div>

<div class="methoddesc">

setnframesn Set the number of frames to *n*. This will be changed later if more frames are written.

</div>

<div class="methoddesc">

setcomptypetype, name Set the compression type and description.

</div>

<div class="methoddesc">

setparamstuple The *tuple* should be `(`*`nchannels`*`, `*`sampwidth`*`, `*`framerate`*`, `*`nframes`*`, `*`comptype`*`, `*`compname`*`)`, with values valid for the `set*()` methods. Sets all parameters.

</div>

<div class="methoddesc">

tell Return current position in the file, with the same disclaimer for the `Wave_read.tell()` and `Wave_read.setpos()` methods.

</div>

<div class="methoddesc">

writeframesrawdata Write audio frames, without correcting *nframes*.

</div>

<div class="methoddesc">

writeframesdata Write audio frames and make sure *nframes* is correct.

</div>

Note that it is invalid to set any parameters after calling `writeframes()` or `writeframesraw()`, and any attempt to do so will raise `wave.Error`.
# `webbrowser` — Convenient Web-browser controller

*Easy-to-use controller for Web browsers.*\
The `webbrowser` module provides a very high-level interface to allow displaying Web-based documents to users. The controller objects are easy to use and are platform independent.

Under Unix, graphical browsers are preferred under X11, but text-mode browser will be used if graphical browsers are not available or an X11 display isn’t available. If text-mode browsers are used, the calling process will block until the user exits the browser.

For non-Unix platforms, or when X11 browsers are available on Unix, the controlling process will not wait for the user to finish with the browser, but allow the browser to maintain its own window on the display.

The following exception is defined:

<div class="excdesc">

Error Exception raised when a browser control error occurs.

</div>

The following functions are defined:

<div class="funcdesc">

openurl Display *url* using the default browser. If *new* is true, a new browser window is opened if possible.

</div>

<div class="funcdesc">

open_newurl Open *url* in a new window of the default browser, if possible, otherwise, open *url* in the only browser window.

</div>

<div class="funcdesc">

get Return a controller object for the browser type *name*.

</div>

<div class="funcdesc">

registername, constructor Register the browser type *name*. Once a browser type is registered, the `get()` function can return a controller for that browser type. If *instance* is not provided, or is `None`, *constructor* will be called without parameters to create an instance when needed. If *instance* is provided, *constructor* will never be called, and may be `None`.

</div>

Several browser types are defined. This table gives the type names that may be passed to the `get()` function and the names of the implementation classes, all defined in this module.

|                                     |     |     |
|:------------------------------------|:----|:----|
| Type NameClass NameNotes ’netscape’ |     |     |
|                                     |     |     |
|                                     |     |     |
|                                     |     |     |
|                                     |     |     |
|                                     |     |     |
|                                     |     |     |

Notes:

\(1\)  
“Konquerer” is the file manager for the KDE desktop environment, and only makes sense to use if KDE is running.

\(2\)  
Only on Windows platforms; requires the common extension modules `win32api` and `win32con`.

\(3\)  
Only on MacOS platforms; requires the standard MacPython `ic` module, described in the Macintosh Library Modules manual.

## Browser Controller Objects <span id="browser-controllers" label="browser-controllers"></span>

Browser controllers provide two methods which parallel two of the module-level convenience functions:

<div class="funcdesc">

openurl Display *url* using the browser handled by this controller. If *new* is true, a new browser window is opened if possible.

</div>

<div class="funcdesc">

open_newurl Open *url* in a new window of the browser handled by this controller, if possible, otherwise, open *url* in the only browser window.

</div>
# `whichdb` — Guess which DBM module created a database

*Guess which DBM-style module created a given database.*\
The single function in this module attempts to guess which of the several simple database modules available–`dbm`, `gdbm`, or `dbhash`–should be used to open a given file.

<div class="funcdesc">

whichdbfilename Returns one of the following values: `None` if the file can’t be opened because it’s unreadable or doesn’t exist; the empty string (`’’`) if the file’s format can’t be guessed; or a string containing the required module name, such as `’dbm’` or `’gdbm’`.

</div>
# `_winreg` – Windows registry access

*Routines and objects for manipulating the Windows registry.*\
*New in version 2.0.*

These functions expose the Windows registry API to Python. Instead of using an integer as the registry handle, a handle object is used to ensure that the handles are closed correctly, even if the programmer neglects to explicitly close them.

This module exposes a very low-level interface to the Windows registry; it is expected that in the future a new `winreg` module will be created offering a higher-level interface to the registry API.

This module offers the following functions:

<div class="funcdesc">

CloseKeyhkey Closes a previously opened registry key. The hkey argument specifies a previously opened key.

Note that if *hkey* is not closed using this method, (or the `handle.Close()` closed when the *hkey* object is destroyed by Python.

</div>

<div class="funcdesc">

ConnectRegistrycomputer_name, key Establishes a connection to a predefined registry handle on another computer, and returns a *handle object*

*computer_name* is the name of the remote computer, of the form `computername`. If `None`, the local computer is used.

*key* is the predefined handle to connect to.

The return value is the handle of the opened key. If the function fails, an `EnvironmentError` exception is raised.

</div>

<div class="funcdesc">

CreateKeykey, sub_key Creates or opens the specified key, returning a *handle object*

*key* is an already open key, or one of the predefined constants.

*sub_key* is a string that names the key this method opens or creates.

If *key* is one of the predefined keys, *sub_key* may be `None`. In that case, the handle returned is the same key handle passed in to the function.

If the key already exists, this function opens the existing key

The return value is the handle of the opened key. If the function fails, an `EnvironmentError` exception is raised.

</div>

<div class="funcdesc">

DeleteKeykey, sub_key Deletes the specified key.

*key* is an already open key, or any one of the predefined constants.

*sub_key* is a string that must be a subkey of the key identified by the *key* parameter. This value must not be `None`, and the key may not have subkeys.

*This method can not delete keys with subkeys.*

If the method succeeds, the entire key, including all of its values, is removed. If the method fails, an `EnvironmentError` exception is raised.

</div>

<div class="funcdesc">

DeleteValuekey, value Removes a named value from a registry key.

*key* is an already open key, or one of the predefined constants.

*value* is a string that identifies the value to remove.

</div>

<div class="funcdesc">

EnumKeykey, index Enumerates subkeys of an open registry key, returning a string.

*key* is an already open key, or any one of the predefined constants.

*index* is an integer that identifies the index of the key to retrieve.

The function retrieves the name of one subkey each time it is called. It is typically called repeatedly until an `EnvironmentError` exception is raised, indicating, no more values are available.

</div>

<div class="funcdesc">

EnumValuekey, index Enumerates values of an open registry key, returning a tuple.

*key* is an already open key, or any one of the predefined constants.

*index* is an integer that identifies the index of the value to retrieve.

The function retrieves the name of one subkey each time it is called. It is typically called repeatedly, until an `EnvironmentError` exception is raised, indicating no more values.

The result is a tuple of 3 items:

A string that identifies the value name

An object that holds the value data, and whose type depends on the underlying registry type.

is an integer that identifies the type of the value data.

</div>

<div class="funcdesc">

FlushKeykey Writes all the attributes of a key to the registry.

*key* is an already open key, or one of the predefined constants.

It is not necessary to call RegFlushKey to change a key. Registry changes are flushed to disk by the registry using its lazy flusher. Registry changes are also flushed to disk at system shutdown. Unlike `CloseKey()`, the `FlushKey()` method returns only when all the data has been written to the registry. An application should only call `FlushKey()` if it requires absolute certainty that registry changes are on disk.

*If you don’t know whether a `FlushKey()` call is required, it probably isn’t.*

</div>

<div class="funcdesc">

RegLoadKeykey, sub_key, file_name Creates a subkey under the specified key and stores registration information from a specified file into that subkey.

*key* is an already open key, or any of the predefined constants.

*sub_key* is a string that identifies the sub_key to load

*file_name* is the name of the file to load registry data from. This file must have been created with the `SaveKey()` function. Under the file allocation table (FAT) file system, the filename may not have an extension.

A call to LoadKey() fails if the calling process does not have the privilege. Note that privileges are different than permissions - see the Win32 documentation for more details.

If *key* is a handle returned by `ConnectRegistry()`, then the path specified in *fileName* is relative to the remote computer.

The Win32 documentation implies *key* must be in the or tree. This may or may not be true.

</div>

<div class="funcdesc">

OpenKeykey, sub_key Opens the specified key, returning a *handle object*

*key* is an already open key, or any one of the predefined constants.

*sub_key* is a string that identifies the sub_key to open

*res* is a reserved integer, and must be zero. The default is zero.

*sam* is an integer that specifies an access mask that describes the desired security access for the key. Default is

The result is a new handle to the specified key

If the function fails, `EnvironmentError` is raised.

</div>

<div class="funcdesc">

OpenKeyEx The functionality of `OpenKeyEx()` is provided via `OpenKey()`, by the use of default arguments.

</div>

<div class="funcdesc">

QueryInfoKeykey Returns information about a key, as a tuple.

*key* is an already open key, or one of the predefined constants.

The result is a tuple of 3 items:

An integer that identifies the number of sub keys this key has.

An integer that identifies the number of values this key has.

A long integer that identifies when the key was last modified (if available) as 100’s of nanoseconds since Jan 1, 1600.

</div>

<div class="funcdesc">

QueryValuekey, sub_key Retrieves the unnamed value for a key, as a string

*key* is an already open key, or one of the predefined constants.

*sub_key* is a string that holds the name of the subkey with which the value is associated. If this parameter is `None` or empty, the function retrieves the value set by the `SetValue()` method for the key identified by *key*.

Values in the registry have name, type, and data components. This method retrieves the data for a key’s first value that has a NULL name. But the underlying API call doesn’t return the type, Lame Lame Lame, DO NOT USE THIS!!!

</div>

<div class="funcdesc">

QueryValueExkey, value_name Retrieves the type and data for a specified value name associated with an open registry key.

*key* is an already open key, or one of the predefined constants.

*value_name* is a string indicating the value to query.

The result is a tuple of 2 items:

The value of the registry item.

An integer that identifies the registry type for this value.

</div>

<div class="funcdesc">

SaveKeykey, file_name Saves the specified key, and all its subkeys to the specified file.

*key* is an already open key, or one of the predefined constants.

*file_name* is the name of the file to save registry data to. This file cannot already exist. If this filename includes an extension, it cannot be used on file allocation table (FAT) file systems by the `LoadKey()`, `ReplaceKey()` or `RestoreKey()` methods.

If *key* represents a key on a remote computer, the path described by *file_name* is relative to the remote computer. The caller of this method must possess the security privilege. Note that privileges are different than permissions - see the Win32 documentation for more details.

This function passes NULL for *security_attributes* to the API.

</div>

<div class="funcdesc">

SetValuekey, sub_key, type, value Associates a value with a specified key.

*key* is an already open key, or one of the predefined constants.

*sub_key* is a string that names the subkey with which the value is associated.

*type* is an integer that specifies the type of the data. Currently this must be , meaning only strings are supported. Use the `SetValueEx()` function for support for other data types.

*value* is a string that specifies the new value.

If the key specified by the *sub_key* parameter does not exist, the SetValue function creates it.

Value lengths are limited by available memory. Long values (more than 2048 bytes) should be stored as files with the filenames stored in the configuration registry. This helps the registry perform efficiently.

The key identified by the *key* parameter must have been opened with access.

</div>

<div class="funcdesc">

SetValueExkey, value_name, reserved, type, value Stores data in the value field of an open registry key.

*key* is an already open key, or one of the predefined constants.

*sub_key* is a string that names the subkey with which the value is associated.

*type* is an integer that specifies the type of the data. This should be one of:

Binary data in any form.

A 32-bit number.

A 32-bit number in little-endian format.

A 32-bit number in big-endian format.

A null-terminated string that contains unexpanded references to environment variables (for example, `%PATH%`)

A Unicode symbolic link.

A sequence (eg, list, sequence) of null-terminated strings, terminated by two null characters. (Note that Python handles this termination automatically)

No defined value type.

A device-driver resource list.

A null-terminated string.

*reserved* can be anything - zero is always passed to the API.

*value* is a string that specifies the new value.

This method can also set additional value and type information for the specified key. The key identified by the key parameter must have been opened with access.

To open the key, use the `CreateKeyEx()` or `OpenKey()` methods.

Value lengths are limited by available memory. Long values (more than 2048 bytes) should be stored as files with the filenames stored in the configuration registry. This helps the registry perform efficiently.

</div>

## Registry handle objects <span id="handle-object" label="handle-object"></span>

This object wraps a Windows HKEY object, automatically closing it when the object is destroyed. To guarantee cleanup, you can call either the `Close()` method on the object, or the `CloseKey()` function.

All registry functions in this module return one of these objects.

All registry functions in this module which accept a handle object also accept an integer, however, use of the handle object is encouraged.

Handle objects provide semantics for `__nonzero__()` - thus

        if handle:
            print "Yes"

will print `Yes` if the handle is currently valid (i.e., has not been closed or detached).

The object also support comparison semantics, so handle objects will compare true if they both reference the same underlying Windows handle value.

Handle objects can be converted to an integer (eg, using the builtin `int()` function, in which case the underlying Windows handle value is returned. You can also use the `Detach()` method to return the integer handle, and also disconnect the Windows handle from the handle object.

<div class="methoddesc">

Close Closes the underlying Windows handle.

If the handle is already closed, no error is raised.

</div>

<div class="methoddesc">

Detach Detaches the Windows handle from the handle object.

The result is an integer (or long on 64 bit Windows) that holds the value of the handle before it is detached. If the handle is already detached or closed, this will return zero.

After calling this function, the handle is effectively invalidated, but the handle is not closed. You would call this function when you need the underlying Win32 handle to exist beyond the lifetime of the handle object.

</div>
# `winsound` — Sound-playing interface for Windows

*Access to the sound-playing machinery for Windows.*\
*New in version 1.5.2.*

The `winsound` module provides access to the basic sound-playing machinery provided by Windows platforms. It includes two functions and several constants.

<div class="funcdesc">

Beepfrequency, duration Beep the PC’s speaker. The *frequency* parameter specifies frequency, in hertz, of the sound, and must be in the range 37 through 32,767 (`0x25` through `0x7fff`). The *duration* parameter specifies the number of milliseconds the sound should last. If the system is not able to beep the speaker, `RuntimeError` is raised. *New in version 1.5.3.*

</div>

<div class="funcdesc">

PlaySoundsound, flags Call the underlying function from the Platform API. The *sound* parameter may be a filename, audio data as a string, or `None`. Its interpretation depends on the value of *flags*, which can be a bit-wise ORed combination of the constants described below. If the system indicates an error, `RuntimeError` is raised.

</div>

<div class="datadesc">

SND_FILENAME The *sound* parameter is the name of a WAV file.

</div>

<div class="datadesc">

SND_ALIAS The *sound* parameter should be interpreted as a control panel sound association name.

</div>

<div class="datadesc">

SND_LOOP Play the sound repeatedly. The flag must also be used to avoid blocking.

</div>

<div class="datadesc">

SND_MEMORY The *sound* parameter to `PlaySound()` is a memory image of a WAV file.

**Note:** This module does not support playing from a memory image asynchronously, so a combination of this flag and will raise a `RuntimeError`.

</div>

<div class="datadesc">

SND_PURGE Stop playing all instances of the specified sound.

</div>

<div class="datadesc">

SND_ASYNC Return immediately, allowing sounds to play asynchronously.

</div>

<div class="datadesc">

SND_NODEFAULT If the specified sound cannot be found, do not play a default beep.

</div>

<div class="datadesc">

SND_NOSTOP Do not interrupt sounds currently playing.

</div>

<div class="datadesc">

SND_NOWAIT Return immediately if the sound driver is busy.

</div>
# `xdrlib` — Encode and decode XDR data.

*Encoders and decoders for the External Data Representation (XDR).*\
The `xdrlib` module supports the External Data Representation Standard as described in , written by Sun Microsystems, Inc. June 1987. It supports most of the data types described in the RFC.

The `xdrlib` module defines two classes, one for packing variables into XDR representation, and another for unpacking from XDR representation. There are also two exception classes.

<div class="classdesc">

Packer `Packer` is the class for packing data into XDR representation. The `Packer` class is instantiated with no arguments.

</div>

<div class="classdesc">

Unpackerdata `Unpacker` is the complementary class which unpacks XDR data values from a string buffer. The input buffer is given as *data*.

</div>

## Packer Objects <span id="xdr-packer-objects" label="xdr-packer-objects"></span>

`Packer` instances have the following methods:

<div class="methoddesc">

get_buffer Returns the current pack buffer as a string.

</div>

<div class="methoddesc">

reset Resets the pack buffer to the empty string.

</div>

In general, you can pack any of the most common XDR data types by calling the appropriate `pack_`*`type`*`()` method. Each method takes a single argument, the value to pack. The following simple data type packing methods are supported: `pack_uint()`, `pack_int()`, `pack_enum()`, `pack_bool()`, `pack_uhyper()`, and `pack_hyper()`.

<div class="methoddesc">

pack_floatvalue Packs the single-precision floating point number *value*.

</div>

<div class="methoddesc">

pack_doublevalue Packs the double-precision floating point number *value*.

</div>

The following methods support packing strings, bytes, and opaque data:

<div class="methoddesc">

pack_fstringn, s Packs a fixed length string, *s*. *n* is the length of the string but it is *not* packed into the data buffer. The string is padded with null bytes if necessary to guaranteed 4 byte alignment.

</div>

<div class="methoddesc">

pack_fopaquen, data Packs a fixed length opaque data stream, similarly to `pack_fstring()`.

</div>

<div class="methoddesc">

pack_strings Packs a variable length string, *s*. The length of the string is first packed as an unsigned integer, then the string data is packed with `pack_fstring()`.

</div>

<div class="methoddesc">

pack_opaquedata Packs a variable length opaque data string, similarly to `pack_string()`.

</div>

<div class="methoddesc">

pack_bytesbytes Packs a variable length byte stream, similarly to `pack_string()`.

</div>

The following methods support packing arrays and lists:

<div class="methoddesc">

pack_listlist, pack_item Packs a *list* of homogeneous items. This method is useful for lists with an indeterminate size; i.e. the size is not available until the entire list has been walked. For each item in the list, an unsigned integer `1` is packed first, followed by the data value from the list. *pack_item* is the function that is called to pack the individual item. At the end of the list, an unsigned integer `0` is packed.

For example, to pack a list of integers, the code might appear like this:

    import xdrlib
    p = xdrlib.Packer()
    p.pack_list([1, 2, 3], p.pack_int)

</div>

<div class="methoddesc">

pack_farrayn, array, pack_item Packs a fixed length list (*array*) of homogeneous items. *n* is the length of the list; it is *not* packed into the buffer, but a `ValueError` exception is raised if `len(`*`array`*`)` is not equal to *n*. As above, *pack_item* is the function used to pack each element.

</div>

<div class="methoddesc">

pack_arraylist, pack_item Packs a variable length *list* of homogeneous items. First, the length of the list is packed as an unsigned integer, then each element is packed as in `pack_farray()` above.

</div>

## Unpacker Objects <span id="xdr-unpacker-objects" label="xdr-unpacker-objects"></span>

The `Unpacker` class offers the following methods:

<div class="methoddesc">

resetdata Resets the string buffer with the given *data*.

</div>

<div class="methoddesc">

get_position Returns the current unpack position in the data buffer.

</div>

<div class="methoddesc">

set_positionposition Sets the data buffer unpack position to *position*. You should be careful about using `get_position()` and `set_position()`.

</div>

<div class="methoddesc">

get_buffer Returns the current unpack data buffer as a string.

</div>

<div class="methoddesc">

done Indicates unpack completion. Raises an `Error` exception if all of the data has not been unpacked.

</div>

In addition, every data type that can be packed with a `Packer`, can be unpacked with an `Unpacker`. Unpacking methods are of the form `unpack_`*`type`*`()`, and take no arguments. They return the unpacked object.

<div class="methoddesc">

unpack_float Unpacks a single-precision floating point number.

</div>

<div class="methoddesc">

unpack_double Unpacks a double-precision floating point number, similarly to `unpack_float()`.

</div>

In addition, the following methods unpack strings, bytes, and opaque data:

<div class="methoddesc">

unpack_fstringn Unpacks and returns a fixed length string. *n* is the number of characters expected. Padding with null bytes to guaranteed 4 byte alignment is assumed.

</div>

<div class="methoddesc">

unpack_fopaquen Unpacks and returns a fixed length opaque data stream, similarly to `unpack_fstring()`.

</div>

<div class="methoddesc">

unpack_string Unpacks and returns a variable length string. The length of the string is first unpacked as an unsigned integer, then the string data is unpacked with `unpack_fstring()`.

</div>

<div class="methoddesc">

unpack_opaque Unpacks and returns a variable length opaque data string, similarly to `unpack_string()`.

</div>

<div class="methoddesc">

unpack_bytes Unpacks and returns a variable length byte stream, similarly to `unpack_string()`.

</div>

The following methods support unpacking arrays and lists:

<div class="methoddesc">

unpack_listunpack_item Unpacks and returns a list of homogeneous items. The list is unpacked one element at a time by first unpacking an unsigned integer flag. If the flag is `1`, then the item is unpacked and appended to the list. A flag of `0` indicates the end of the list. *unpack_item* is the function that is called to unpack the items.

</div>

<div class="methoddesc">

unpack_farrayn, unpack_item Unpacks and returns (as a list) a fixed length array of homogeneous items. *n* is number of list elements to expect in the buffer. As above, *unpack_item* is the function used to unpack each element.

</div>

<div class="methoddesc">

unpack_arrayunpack_item Unpacks and returns a variable length *list* of homogeneous items. First, the length of the list is unpacked as an unsigned integer, then each element is unpacked as in `unpack_farray()` above.

</div>

## Exceptions <span id="xdr-exceptions" label="xdr-exceptions"></span>

Exceptions in this module are coded as class instances:

<div class="excdesc">

Error The base exception class. `Error` has a single public data member `msg` containing the description of the error.

</div>

<div class="excdesc">

ConversionError Class derived from `Error`. Contains no additional instance variables.

</div>

Here is an example of how you would catch one of these exceptions:

    import xdrlib
    p = xdrlib.Packer()
    try:
        p.pack_double(8.01)
    except xdrlib.ConversionError, instance:
        print 'packing the double failed:', instance.msg


{{< python-copyright version="2.0b2" >}}
