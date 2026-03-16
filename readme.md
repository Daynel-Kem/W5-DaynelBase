custom database for storing stuff  
idk whats involved in making it yet but it sounds like a mighty neat project  
  
Ill reference the build-your-own-x github for it  
[github](https://github.com/codecrafters-io/build-your-own-x)  
  
  
Small excerpt from [this page](https://charlesleifer.com/blog/building-a-simple-redis-server-with-python/)  

>The server we'll be building will be able to respond to the following commands:  

    GET <key>  
    SET <key> <value>  
    DELETE <key>  
    FLUSH  
    MGET <key1> ... <keyn>  
    MSET <key1> <value1> ... <keyn> <valuen>  

>We'll support the following data-types as well:  

    Strings and Binary Data  
    Numbers  
    NULL  
    Arrays (which may be nested)  
    Dictionaries (which may be nested)  
    Error messages  
  
We'll implement the REDIS database using Python as mentioned in Charles Leifer's page  
I'm going to attempt to use the standard Python libraries that was mentioned instead of gevent as well cause why not  
THE CODE IN THE BLOG POST WAS WRONG, YOU HAVE TO GO THROUGH THE GITHUB CODE TO ACTUALLY WORK IT OUT  
ARE WE TROLLING  
  
Suggestions from the blogpost:  
To extend the project, you might consider:

    Add more commands!
    Use the protocol handler to implement an append-only command log
    More robust error handling
    Allow client to close connection and re-connect
    Logging
    Re-write to use the standard library's SocketServer and ThreadingMixin
