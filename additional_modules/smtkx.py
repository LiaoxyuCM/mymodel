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