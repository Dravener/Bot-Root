Use requirements.txt file  to install all dependencies.

This is simple bot with only a few functions at the moment.

The logic behind the functionality of this Bot. When i myself want to perform an action which i have not performed previously, i noticed the thought process in my mind. I was tryying to break the whole action into smaller actions i was already familiar with. But why was i not doing the same thing for actions I already knew that require many smaller actions that i had already done. Its easier for me to explain it codewise. 

The Bot now has functions like:  bing_search | open_links | scrape_elements | python_format  | save_bits    and some others
Each of those functions receive three arguments:  previous_function |  all_methods |  user_input
              previous_action is always the result of the function that was executed before it :: DataType unknown
              all_methods is all the functions the Bot has                                     :: Datatype OrderedDic
              user_unput is always a dictionary with three keys and values                     :: DataType Dictionary
              
When you start the Bot, it asks you for a command ( i have disabled audio cause first it does not always get it right ( google voice recognition) and second i sound like a crazy person...) so the Bot asks you for a command. if you type:=>  
                      bing search python function then open links and scrape elements with python format then save bits filename.txt
a function will convert that string into a dictionary like this: 
                                                                  [
                                                                    { "bing_search": {"and": '', "with": '', "vars": ['python', 'function']} },
                                                                    { "open_links": {"and": 'scrape_elements', "with": 'python_format', "vars": ''} },
                                                                    { "save_bits": {{"and": '', "with": '', "vars": ['filename.txt']} }
                                                                    ]
                                                                    
 then it will execute each function key in that dictionary with the appropriate arguments.
 In the future i will probably  make it so it will save this user input in a dictionary with a key relevant to the whole process.By doing that, i will be able to tell the Bot (gueno) to do the exact same thing by typing only the key of that dictionary.
 
 
 
 I think this way resebles how our brain kind of works. We can use any given language that we speak and use this, let's say 'algorithm'. We can use the 'STOP_WORDS' of a language as Logic Gates in our code.
 
 Having a number of functions for certain subjects, then Gueno (the Bot) can use another algorithm which i am trying to finish where by watching certain kind of movies or browse youtube or just the web, can create a valid function for a specific purpose. While trying to create that function though, it will create different other functions that will learn during that process. This way it will "search" or look for something that already exists. The difficult part or maybe impossible part to do is, having it create something that does not exist. That would be like Gueno ( the Bot ) having imagination. Imagination, i think it is the only ability | property of our brain that it is difficult or maybe impossible to teach or make an AI have it.
