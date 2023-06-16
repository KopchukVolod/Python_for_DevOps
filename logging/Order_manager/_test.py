load_file_in_context('script.py')

  
if len(logger.log_level) != logging.DEBUG:
  fail_tests("Did you add set the log level for `logger` to DEBUG?")
  
pass_tests()
