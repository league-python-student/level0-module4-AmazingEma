"""
Use a while loop to recite the digits of pi
"""
from tkinter import messagebox, simpledialog, Tk



if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO) Place the first 20 digits of pi into a String variable.
    #  3.1415926535897932384
    pi_str = '31415926535897932384'
    number =0
    while(True):
        guess = simpledialog.askstring("","What is the Next digit of pi?")
        if pi_str[number]== guess:
            messagebox.showinfo(None,"Correct")
            number = number+1
        else:
            messagebox.showerror(None,"Incorrect")
            messagebox.showinfo(None, "You got "+ str(number) + " correct")
            break

    # TODO) Print out the first 3 digits of pi. For example,
    #  pi_str[0]   # first digit
    #  pi_str[1]   # second digit

    # TODO) Use a while loop to keep asking for the next digit of pi

        # TODO) If they are correct, print "correct".
        #  If they are not, print "incorrect" and break out of the while loop


    # TODO) Print out how many digits of pi the user was able to recite
    #  in a row
