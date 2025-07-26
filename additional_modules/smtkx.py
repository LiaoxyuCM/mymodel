import os, sys

def colorful_that_under_win10():
    if sys.platform == "win32":
        if sys.getwindowsversion().major < 10:
            try:
                import colorama
                colorama.init()
            except Exception:
                if os.system("pip -V"):
                    print("Please install pip at first.")
                else:
                    os.system("pip install colorama")
                    import colorama
                    colorama.init()

usage: str = r'''If you do not know how does it work, here is the help msg.
Other chrs       : Add chrs into the pre-print list
.                : Print and clear the pre-print list, then create a new line
\.               : Add "." into the pre-print list
\comment.        : Comment, comment msg will ignore, then do nothing
\\               : Add "\" into the pre-print list
\comment\        : Comment, comment msg will ignore, then do nothing
<Ctrl+C>         : Quit this program
Try these now! They are useful when I was debugging.
    Hello.
    Hello
    Hello\..
    Hello\.\..
    Hello\. \..
    Hello\.\ ..
    Hello\\.
    Hello\\\\.
    Hello \\ \\.
    Hello\comment..
    Hello\first comment.\second comment..
    He\first.\second.llo.
    He\first. \second.llo.
    Hello\comment\.
    Hello\first comment\\second comment\.
    He\first\\second\llo.
    He\first\ \second\llo.
    Line 1.Line 2.
    Line 1. Line 2.
    Line 1.Line 2
And the last one:
    Message:.1\. AAA;.2\. BBB;.3\. CCC;\Some Message..
After this test, I can say this is not a Turing Complete.
'''