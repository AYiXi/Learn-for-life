## [Frida](https://frida.re/docs/home/)

## Welcome
- it’s a dynamic code instrumentation toolkit
- It lets you inject snippets of JavaScript or your own library into native apps on Windows, macOS, GNU/Linux, iOS, Android, and QNX
- 
- API tracing
- logging code
- set up a test lab
- black-box tests
- 
- written in C and injects QuickJS into the target processes
- [QuickJs](https://bellard.org/quickjs/)
  - Small and easily embeddable
  - Fast
  - Small built-in standard library with C library wrappers
  - Can compile Javascript sources to executables with no external dependency
  - ...

## QuickStart Guide
- `pip install frida-tools`
- `frida-trace -i "recv*" -i "read*" "wechat"`
  - let’s have a look at the generated `recvfrom.js`
  - replace `log()`

## [GadGet](https://frida.re/docs/gadget/)[Not Known]
- Modifying the source code of the program
- Patching it or one of its libraries
- Using a dynamic linker feature