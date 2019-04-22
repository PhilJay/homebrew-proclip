# ProClip
A terminal / commandline extension for **storing and executing frequently used commands** conveniently instead of having to re-type them everytime.

Requires Python 3+

# Installation
Clone the repository and add the brew formula to the brew search path using:
```python
  brew tap philjay/proclip https://github.com/PhilJay/homebrew-proclip.git
```

Install "proclip":
```python
  brew install proclip
```


# Usage

After successful installation, ProClip can be used via the `pcl` command:
```python
  # shows the help explaining all available commands
  pcl -h

  # lists all currently stored entries / shortcuts
  pcl -l 
  
  # stores the command "ping www.google.com" under the alias pg (ping google)
  pcl -s pg "ping www.google.com"
  
  # executes "ping www.google.com"
  pcl -e pg
  
  # copies "ping www.google.com" to the clipboard
  pcl -c pg
  
  # removes the "pg" alias (meaning it is no longer usable and can be replaced by a new command)
  pcl -r pg
```

# More examples

```python
  # store multiple commands and execute them at once
  pcl -s test "mkdir test && cd test && touch test.txt"
  
  # execute the command and perform all operations (crate folder, move to it, create file)
  pcl -e test
```
