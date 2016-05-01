# reddit-counter
An easily customizable python program that automatically counts in the main counting threads at /r/counting


#Usage 
* Edit the settings.txt file to include your reddit username and password
* Edit `THREAD` to include the thread you want to count in
* If you are counting in a specialized thread you can edit the convert_comment_to_num and get_next_number function to work with your special case
* You can adjust `MIN_SLEEP` and `MAX_SLEEP` to specify the range that you want the program to sleep in (in seconds) between checking comments
* If you just want the program to check once, you can set `CONSTANTLOOP = False`
