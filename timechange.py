import time
fortime = time.gmtime()
time_str = "{0}:{1}:{2}".format(fortime[3], fortime[4], fortime[5])

with open("README.md", "w") as f:
  f.write(f"""# Testing workflows

The time is {time_str}.""")
