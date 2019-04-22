# ProClip
A terminal / commandline extension capable of storing and executing frequently used commands conveniently

# Installation
Clone the repository and add the brew formula to the brew search path:

```python
  brew tap philjay/proclip https://github.com/PhilJay/homebrew-proclip.git
```

Install the script "proclip":

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
```
