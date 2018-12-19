# facebook-messenger-chat-bot
A facebook messenger chat bot that can help users to look up bus arriving time and ticket price.
![finite state graph](https://github.com/a693691122/facebook-messenger-chat-bot/blob/master/img/show-fsm.png "finite state graph")

# States description:
* user : the initial state
* state1 : the state which askng user to input their query. 

  「1」 for looking up the arriving time of bus in Tainan.
  
  「2」 for looking up the ticket price.
  
  「3」 for knowing the latest discount of the bus fare.
  
* state2 : require user to input the path name and direction of the path.

  Note that the path name and direction should be separated by a space bar.
  
  for example, 綠1 去, 藍11 返, etc...
  
  the bot will return the arriving time of all stops in this path.
  
* state3 : require user to input the path name, start stop and end stop.

  Note that the path name, start stop and end stop should be separated by a space bar respectively.
  
  for example, 綠1 新化站 國泰大樓, 藍11 佳里站 下營, etc...
  
  the bot will return the ticket fare.
  
* state4 : return latest discount immediately after entering this state.

* state5 : return the arriving time of all stops in specific path.

* state6 : return the ticket fare.

