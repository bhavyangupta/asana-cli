# Development setup
1. Create a personal authorization token
2. Install Asana's python client library:

```
sudo pip install asana
```
# Possible use cases
- A cli way to interact with asana based on taskwarrior.
- Actually interface taskwarrior with asana - you need to dump asana's data
  in task warrior's task file and periodically take data in task file and send
  it to asana. Transcription will be needed but since both use json it 
  shouldn't be complicated.

# Roadmap
1. Simple viewer that can only downlink and display tasks relevant to a section
   of the workspace
2. 


# References
1. Python API documentation - https://asana.readthedocs.io/en/latest/
2. http://stackoverflow.com/questions/30601424/how-can-i-create-a-new-project-with-tasks-in-asana-using-python 

# Issues faced
1. Upgrading `pip`
```
sudo pip install --upgrade pip # upgraded to v8.1
```
2. Enabling ssl with python
```
sudo pip install 'requests[security]'
```


