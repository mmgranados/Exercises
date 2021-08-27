import time

morse_dict={ ".-":'A', "-..." : 'B', "-.-.":'C', "-..":"D", ".":"E" , "..-.":"F" , "--.":"G" , "....":"H" , "..":'I' , ".---":"J" , "-.-":"K" , ".-..":"L" , "--":"M", "-.":"N",
             "---":"O", ".--.":"P" , "--.-":"Q", ".-.":"R" , "...":"S" , "-": "T", "..-":"U" , "...-":"V" , ".--":"W" , "-..-":"X" , "-.--":"Y" , "--..":"Z"}             
morse=[]
letter_buffer=[]
final_output=[]
user_input = input("Input Morse Code: ")
morse.append(user_input)
start_time = 0
code:str


def isZero(substring):
    if substring == "----":
        return True

def substring_check(string_init, translated_substring):
    global final_output
    substring_len = 1 # len = 1 on default length
    state = 0
    substring = ""
    # If out of bounds, go back.
    # this means, translation is invalid
    if string_init > len(code):
        return
    elif string_init == len(code):  # case: index = 8, valid translation..
        # if string_init is at index 8, append to final_output
        final_output.append(translated_substring)
        return


    # sub_len = 1
    # REMEMBER: for string slicing - [inclusive:exclusive]
    if isZero(code[string_init:string_init + substring_len + 0]):
        return
    # Avoid string "----"   
    substring = morse_dict[code[string_init: string_init + substring_len + 0]]  # Translates target substring
    substring_check(string_init+substring_len, translated_substring + substring)    # goes to next target
    # concatenate translated target substring to previously translated substrings
        
    # sub length + 2
    # Avoid out of bounds
    if string_init + substring_len + 1 > len(code):
        return
    # Avoid string "----"  
    if isZero(code[string_init:string_init + substring_len + 1]):
        return    
    substring = morse_dict[code[string_init:string_init + substring_len + 1]]   # Translates target substring into text equival
    substring_check(string_init + substring_len + 1, translated_substring + substring)  # goes to next target 
    # concatenate translated target substring to previously translated substrings

    # sub length + 3
    # Avoid out of bounds
    if string_init + substring_len + 2 > len(code):
        return
    # Avoid string "----"  
    if isZero(code[string_init:string_init + substring_len + 2]):
        return
    substring = morse_dict[code[string_init:string_init + substring_len + 2]]   # Translates target substring into text equival
    substring_check(string_init + substring_len + 2, translated_substring + substring)  # goes to next target
    # concatenate translated target substring to previously translated substrings
 
    # sub length + 4
    # Avoid out of bounds
    if string_init + substring_len + 3 > len(code):
        return
    # Avoid string "----"
    # Try-except for debugging purposes only    
    if isZero(code[string_init:string_init + substring_len + 3]):
        return
    try:
        substring = morse_dict[code[string_init:string_init + substring_len + 3]]   # Translates target substring into text equival
    except Exception as e:
        return
    substring_check(string_init + substring_len + 3, translated_substring + substring)  # goes to next target
    # concatenate translated target substring to previously translated substrings
    
    return

#Implement the Recursion
code = user_input
start_time = time.perf_counter_ns()
substring_check(0, translated_substring = "")
# show = morselist_decoder(morse, letter_buffer, final_output)


#Creating and writing the file
with open("output.txt", "w") as file_handle:
    for i in final_output:
        file_handle.write(i + " ")

print(time.perf_counter_ns() - start_time)
final_output.sort()        



# show.sort()
test_case=int(input("Test case #: "))
#Testing using the test cases
test_case_1="TTETTE TTETN TTEME TTEG TTATE TTAN TTWE TTP TNTTE TNTN TNME TNG TKTE TKN TYE METTE METN MEME MEG MATE MAN MWE MP GTTE GTN GME GG QTE QN"
test_case_2="ETTTEETT ETTTEEM ETTTEAT ETTTEW ETTTITT ETTTIM ETTTUT ETTNETT ETTNEM ETTNAT ETTNW ETTDTT ETTDM ETTXT ETMEETT ETMEEM ETMEAT ETMEW ETMITT ETMIM ETMUT ETGETT ETGEM ETGAT ETGW ETZTT ETZM EMTEETT EMTEEM EMTEAT EMTEW EMTITT EMTIM EMTUT EMNETT EMNEM EMNAT EMNW EMDTT EMDM EMXT EOEETT EOEEM EOEAT EOEW EOITT EOIM EOUT ATTEETT ATTEEM ATTEAT ATTEW ATTITT ATTIM ATTUT ATNETT ATNEM ATNAT ATNW ATDTT ATDM ATXT AMEETT AMEEM AMEAT AMEW AMITT AMIM AMUT AGETT AGEM AGAT AGW AZTT AZM WTEETT WTEEM WTEAT WTEW WTITT WTIM WTUT WNETT WNEM WNAT WNW WDTT WDM WXT JEETT JEEM JEAT JEW JITT JIM JUT"
test_case_3="TETE TEN TAE TR NTE NN KE C"
test_case_4="EEEET EEEA EEIT EEU EIET EIA EST EV IEET IEA IIT IU HT SET SA"
test_case_5="ETEETE ETEEN ETEAE ETER ETITE ETIN ETUE ETF ENETE ENEN ENAE ENR EDTE EDN EXE AEETE AEEN AEAE AER AITE AIN AUE AF RETE REN RAE RR LTE LN"
test_case_6="XOTE, XON, XTOE, XTTG, XTTTTE, XTTTN, XTTME, XTMTE, XTMN, XMG, XMTTE, XMTN, XMME, TIOG, TIOTTE, TIOTN, TIOME, TITOTE, TITON, TITTOE, TITTTG, TITTTTTE, TITTTTN, TITTTME, TITTMTE, TITTMN, TITMG, TITMTTE, TITMTN, TITMME, TIMOE, TIMTG, TIMTTTE, TIMTTN, TIMTME, TIMMTE, TIMMN, TEWOE, TEWTG, TEWTTTE, TEWTTN, TEWTME, TEWMTE, TEWMN, TEAOTE, TEAON, TEATOE, TEATTG, TEATTTTE, TEATTTN, TEATTME, TEATMTE, TEATMN, TEAMG, TEAMTTE, TEAMTN, TEAMME, TEEOG, TEEOTTE, TEEOTN, TEEOME, TEETOTE, TEETON, TEETTOE, TEETTTG, TEETTTTTE, TEETTTTN, TEETTTME, TEETTMTE, TEETTMN, TEETMG, TEETMTTE, TEETMTN, TEETMME, TEEMOE, TEEMTG, TEEMTTTE, TEEMTTN, TEEMTME, TEEMMTE, TEEMMN, TEJG, TEJTTE, TEJTN, TEJME, TUOTE, TUON, TUTOE, TUTTG, TUTTTTE, TUTTTN, TUTTME, TUTMTE, TUTMN, TUMG, TUMTTE, TUMTN, TUMME, DOG, DOTTE, DOTN, DOME, DTOTE, DTON, DTTOE, DTTTG, DTTTTTE, DTTTTN, DTTTME, DTTMTE, DTTMN, DTMG, DTMTTE, DTMTN, DTMME, DMOE, DMTG, DMTTTE, DMTTN, DMTME, DMMTE, DMMN, NWOE, NWTG, NWTTTE, NWTTN, NWTME, NWMTE, NWMN, NAOTE, NAON, NATOE, NATTG, NATTTTE, NATTTN, NATTME, NATMTE, NATMN, NAMG, NAMTTE, NAMTN, NAMME, NEOG, NEOTTE, NEOTN, NEOME, NETOTE, NETON, NETTOE, NETTTG, NETTTTTE, NETTTTN, NETTTME, NETTMTE, NETTMN, NETMG, NETMTTE, NETMTN, NETMME, NEMOE, NEMTG, NEMTTTE, NEMTTN, NEMTME, NEMMTE, NEMMN, NJG, NJTTE, NJTN, NJME "
error=0

if test_case == 1:
    check = test_case_1.split(" ")
    check.sort()
elif test_case == 2:
    check = test_case_2.split(" ")
    check.sort()
elif test_case == 3:
    check = test_case_3.split(" ")
    check.sort()
elif test_case == 4:
    check = test_case_4.split(" ")
    check.sort()
elif test_case == 5:
    check = test_case_5.split(" ")
    check.sort()
else:
    check = test_case_6.split(", ")
    check.sort()    
for i in range(len(final_output)):
    if final_output[i] not in check:
        error += 1
print(len(final_output))
print(error)
if error == 0:
    print("No error")

# if __name__ == "__main__":
#     main()




