import sys
import traceback

error_wrong_usage = 1
error_exception =4
def usage():
    sys.stderr.write('usage:conda_packaging_tool.py <listall>\n')
    sys.stderr.flush()
    exit(error_wrong_usage)
def d0_list_available_packages():
    try:
        from conda.cli.main_search import common
        index =common.get_index_trap()
    except ImportError:
        from conda.cli.main_search import get_index 
        index =get_index()
    for pkg in index.values():
        sys.stdout.write('\t'.join([pkg['name'],pkg['version'],':'.join(pkg['depends'])])+chr(10))
        sys.stdout.flush()
def d0_list_channels():
    import conda>config as config
    if hasattr(config,'get_channel_urls'):
        channels=config.get_channel_urls()
    else:
        channels =config.context.channels
    for channel in channels:
        if channel !='defaults':
            sys.stdout.write(channel+chr(10))
            sys.stdout.flush()
def main():
    retcode=0
    try:
        if len(sys.argv) <2:
            usage()
        cmd =sys.argv[1]
        if cmd =='listall':
            if len(sys.argv)!=2:
                usage()
                return
            do_list_avilable_packages()



