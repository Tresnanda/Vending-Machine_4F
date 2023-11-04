class NFA():
    def __init__(self):
        self.current_state = "q0"
        self.final_state = []
        
    def addFinalState(self, states):
        for state in states:
            self.final_state.append(state)

    def addCurrentState(self, state):
        self.current_state = state


def automata(nfa, input):
    current_penjurusan = ""
    for letter in input:    #for i in range(len(input)): i = input[i]            if i == 'B' and input[i+1] == '+'
        if nfa.current_state == "q0": # State sekarang adalah q0
            if letter == '1':
                nfa.current_state = 'J1'
            if letter == '2':
                nfa.current_state = 'J2'
            if letter == '3':
                nfa.current_state = 'J3'
            if letter ==  '4':
                nfa.current_state = 'J4'
            if letter == '5':
                nfa.current_state = 'J5'
            
            print(f"Final State: {nfa.current_state}")

        elif nfa.current_state == "J1": # State sekarang adalah j1
            current_penjurusan = 'J1'
            if letter == '1':
                nfa.current_state = 'ALP'

        elif nfa.current_state == 'ALP': # State sekarang adalah ALP
               if current_penjurusan in {'J1', 'J2', 'J3', 'J4', 'J5'}:  # Penjaluran yang di ambil adalah J1
                   if letter in {'1', '2', '3'}: #nilai A, B+, B diubah menjadi 1, 2, 3
                       if current_penjurusan == 'J1':
                           nfa.current_state = 'TBO'
                       elif current_penjurusan == 'J2':
                           nfa.current_state = 'RPL'
                       elif current_penjurusan == 'J3':
                           nfa.current_state = 'MI'
                       elif current_penjurusan == 'J4':
                           nfa.current_state = 'SDG'
                       elif current_penjurusan == 'J5':
                           nfa.current_state = 'KDJK'
                   else:
                       nfa.current_state = 'TDK'
                       print(f"Final State: {nfa.current_state}")

        elif nfa.current_state == 'TBO': # State sekarang adalah TBO
            if letter == '1':
                nfa.current_state = 'BD'
            else:
                nfa.current_state = 'P/S'
                print(f"Final State: {nfa.current_state}")

        elif nfa.current_state == 'BD': # State sekarang adalah BD
            if current_penjurusan == 'J1':
                if letter in {'1', '2'}:
                    nfa.current_state = 'MI'
                else:
                    nfa.current_state = 'TDK'

            elif current_penjurusan == 'J2':
                if letter in {'1', '2'}:
                    nfa.current_state = 'MI'
                else:
                    nfa.current_state = 'TDK'

            elif current_penjurusan == 'J3':
                if letter in {'1', '2'}:
                    nfa.current_state = 'SDG'
                else:
                    nfa.current_state = 'TDK'

            elif current_penjurusan == 'J4':
                if letter in {'1', '2'}:
                    nfa.current_state = 'MI'
                else:
                    nfa.current_state = 'TDK'

            # elif current_penjurusan == 'J5':
            #     tambahkan transisi
        
        elif nfa.current_state == 'MI':
            if current_penjurusan == 'J1':
                if letter in {'1', '2'}:
                    nfa.current_state = 'SD'
                else:
                    nfa.current_state = 'TDK'

            elif current_penjurusan == 'J2':
                if letter in {'1', '2'}:
                    nfa.current_state = 'SD'
                else:
                    nfa.current_state = 'TDK'

            # elif current_penjurusan == 'J3':
            #     #Tambahkan transisi
                
            elif current_penjurusan == 'J4':
                if letter in {'1', '2'}:
                    nfa.current_state = 'SD'
                else:
                    nfa.current_state = 'TDK'

            elif current_penjurusan == 'J5':
                if letter in {'1', '2'}:
                    nfa.current_state = 'MD2'
                else:
                    nfa.current_state = 'TDK'
        
        elif nfa.current_state == 'SD':
            if current_penjurusan == 'J1':
                if letter in {'1', '2'}:
                    nfa.current_state = 'MD1'
                else:
                    nfa.current_state = 'TDK'
            
            elif current_penjurusan == 'J2':
                if letter in {'1', '2'}:
                    nfa.current_state = 'DAA'
                else:
                    nfa.current_state = 'TDK'

            # elif current_penjurusan == 'J3':
            #     print("WID")

            elif current_penjurusan == 'J4':
                if letter in {'1', '2'}:
                    nfa.current_state = 'SO'
                else:
                    nfa.current_state = 'TDK'

            # # elif current_penjurusan == 'J5':
            # #     print("WID")

        elif nfa.current_state == 'MD1':
            if current_penjurusan == 'J1':
                if letter in {'1', '2'}:
                    nfa.current_state = 'ACC'
                else:
                    nfa.current_state = 'TDK'
            if current_penjurusan == 'J3':
                if letter in {'1', '2'}:
                    nfa.current_state = 'ACC'
                else:
                    nfa.current_state = 'TDK'

        elif nfa.current_state == 'P/S':
            if letter == 'T':
                nfa.current_state = 'TDK'
            if current_penjurusan in {'J1', 'J2', 'J3', 'J4'}:
                if letter == 'Y':
                    nfa.current_state = 'BD'
            else:
                if letter == 'Y':
                    nfa.current_state = 'RPL'

# =================================================================
        #Penjaluran 2
        elif nfa.current_state == "J2": # State sekarang adalah j2
            current_penjurusan = 'J2'
            if letter == '2':
                nfa.current_state = 'ALP'

        elif nfa.current_state == 'ALP': # State sekarang adalah ALP
               if current_penjurusan in {'J1', 'J2', 'J3', 'J4', 'J5'}:  # Penjaluran yang di ambil adalah J1
                   if letter in {'1', '2', '3'}: #nilai A, B+, B diubah menjadi 1, 2, 3
                       if current_penjurusan == 'J1':
                           nfa.current_state = 'TBO'
                       elif current_penjurusan == 'J2':
                           nfa.current_state = 'RPL'
                       elif current_penjurusan == 'J3':
                           nfa.current_state = 'MI'
                       elif current_penjurusan == 'J4':
                           nfa.current_state = 'SDG'
                       elif current_penjurusan == 'J5':
                           nfa.current_state = 'KDJK'
                   else:
                       nfa.current_state = 'TDK'

        elif nfa.current_state == 'RPL': # State sekarang adalah RPL
            if letter == '1':
                nfa.current_state = 'BD'
            else:
                nfa.current_state = 'P/S'

        elif nfa.current_state == 'BD': # State sekarang adalah BD
            if current_penjurusan == 'J1':
                if letter in {'1', '2'}:
                    nfa.current_state = 'MI'
                else:
                    nfa.current_state = 'TDK'

            elif current_penjurusan == 'J2':
                if letter in {'1', '2'}:
                    nfa.current_state = 'MI'
                else:
                    nfa.current_state = 'TDK'

            elif current_penjurusan == 'J3':
                if letter in {'1', '2'}:
                    nfa.current_state = 'SDG'
                else:
                    nfa.current_state = 'TDK'

            elif current_penjurusan == 'J4':
                if letter in {'1', '2'}:
                    nfa.current_state = 'MI'
                else:
                    nfa.current_state = 'TDK'

        #     # elif current_penjurusan == 'J5':
        #     #     tambahkan transisi

        elif nfa.current_state == 'MI':
            if current_penjurusan == 'J1':
                if letter in {'1', '2'}:
                    nfa.current_state = 'SD'
                else:
                    nfa.current_state = 'TDK'

            elif current_penjurusan == 'J2':
                if letter in {'1', '2'}:
                    nfa.current_state = 'SD'
                else:
                    nfa.current_state = 'TDK'

            # elif current_penjurusan == 'J3':
                #Tambahkan transisi
                
            elif current_penjurusan == 'J4':
                if letter in {'1', '2'}:
                    nfa.current_state = 'SD'
                else:
                    nfa.current_state = 'TDK'

            elif current_penjurusan == 'J5':
                if letter in {'1', '2'}:
                    nfa.current_state = 'MD2'
                else:
                    nfa.current_state = 'TDK'
        
        elif nfa.current_state == 'SD':
            if current_penjurusan == 'J1':
                if letter in {'1', '2'}:
                    nfa.current_state = 'MD1'
                else:
                    nfa.current_state = 'TDK'
            
            elif current_penjurusan == 'J2':
                if letter in {'1', '2'}:
                    nfa.current_state = 'DAA'
                else:
                    nfa.current_state = 'TDK'

            # elif current_penjurusan == 'J3':
            #     print("WID")

            elif current_penjurusan == 'J4':
                if letter in {'1', '2'}:
                    nfa.current_state = 'SO'
                else:
                    nfa.current_state = 'TDK'

            # elif current_penjurusan == 'J5':
            # transisi

        elif nfa.current_state == 'DAA':
            if current_penjurusan == 'J2':
                if letter in {'1', '2'}:
                    nfa.current_state = 'ACC'
                else:
                    nfa.current_state = 'TDK'
                    
        #PENJALURAN 3

        elif nfa.current_state == 'J3': # State sekarang adalah j3
            current_penjurusan = 'J3'
            if letter == '3':
                nfa.current_state = 'ALP'

        elif nfa.current_state == 'ALP': # State sekarang adalah ALP
               if current_penjurusan in {'J1', 'J2', 'J3', 'J4', 'J5'}:  # Penjaluran yang di ambil adalah J1
                   if letter in {'1', '2', '3'}: #nilai A, B+, B diubah menjadi 1, 2, 3

                       if current_penjurusan == 'J1':
                           nfa.current_state = 'TBO'
                       elif current_penjurusan == 'J2':
                           nfa.current_state = 'RPL'
                       elif current_penjurusan == 'J3':
                           nfa.current_state = 'MI'
                       elif current_penjurusan == 'J4':
                           nfa.current_state = 'SDG'
                       elif current_penjurusan == 'J5':
                           nfa.current_state = 'KDJK'
                           print(f'Transition: ALP -> {nfa.current_state}')
                   else:
                       nfa.current_state = 'TDK'

        elif nfa.current_state == 'MI': # State sekarang adalah TBO
            if letter == '1':
                nfa.current_state = 'BD'
            else:
                nfa.current_state = 'P/S'


        elif nfa.current_state == 'BD': # State sekarang adalah BD
            if current_penjurusan == 'J3':
                if letter in {'1', '2'}:
                    nfa.current_state = 'SDG'
                else:
                    nfa.current_state = 'TDK'

            elif current_penjurusan == 'J2':
                if letter in {'1', '2'}:
                    nfa.current_state = 'MI'
                else:
                    nfa.current_state = 'TDK'

            elif current_penjurusan == 'J3':
                if letter in {'1', '2'}:
                    nfa.current_state = 'SDG'
                else:
                    nfa.current_state = 'TDK'

            elif current_penjurusan == 'J4':
                if letter in {'1', '2'}:
                    nfa.current_state = 'MI'
                else:
                    nfa.current_state = 'TDK'

            # elif current_penjurusan == 'J5':
            #     tambahkan transisi

        elif nfa.current_state == 'SDG':
            if current_penjurusan == 'J3':
                if letter in {'1', '2'}:
                    nfa.current_state = 'DAA'
                else:
                    nfa.current_state = 'TDK'
        
        elif nfa.current_state == 'DAA':
            if current_penjurusan == 'J3':
                if letter in {'1', '2'}:
                    nfa.current_state = 'MD1'
                else:
                    nfa.current_state = 'TDK'

        elif nfa.current_state == 'MD1':
            if current_penjurusan == 'J3':
                if letter in {'1', '2'}:
                    nfa.current_state = 'ACC'
                else:
                    nfa.current_state = 'TDK'
                    
        elif nfa.current_state == 'P/S':
            if letter == 'T':
                nfa.current_state = 'TDK'
            if current_penjurusan in {'J1', 'J2', 'J3', 'J4'}:
                if letter == 'Y':
                    nfa.current_state = 'BD'
            else:
                if letter == 'Y':
                    nfa.current_state = 'RPL'
    
#Penjaluran 4

        elif nfa.current_state == "J4": # State sekarang adalah j4
            current_penjurusan = 'J4'
            if letter == '4':
                nfa.current_state = 'ALP'

        elif nfa.current_state == 'ALP': # State sekarang adalah ALP
               if current_penjurusan in {'J1', 'J2', 'J3', 'J4', 'J5'}:  # Penjaluran yang di ambil adalah J1
                   if letter in {'1', '2', '3'}: #nilai A, B+, B diubah menjadi 1, 2, 3
                       if current_penjurusan == 'J1':
                           nfa.current_state = 'TBO'
                       elif current_penjurusan == 'J2':
                           nfa.current_state = 'RPL'
                       elif current_penjurusan == 'J3':
                           nfa.current_state = 'MI'
                       elif current_penjurusan == 'J4':
                           nfa.current_state = 'SDG'
                       elif current_penjurusan == 'J5':
                           nfa.current_state = 'KDJK'
                   else:
                       nfa.current_state = 'TDK'

        elif nfa.current_state == 'SDG': # State sekarang adalah TBO
            if letter == '1':
                nfa.current_state = 'RPL'
            else:
                nfa.current_state = 'P/S'

        elif nfa.current_state == 'RPL': # State sekarang adalah BD
            if current_penjurusan == 'J4':
                if letter in {'1', '2'}:
                    nfa.current_state = 'MI'
                else:
                    nfa.current_state = 'TDK'

            # elif current_penjurusan == 'J2':
            #     if letter in {'1', '2'}:
            #         nfa.current_state = 'MI'
            #     else:
            #         nfa.current_state = 'TDK'

            # elif current_penjurusan == 'J3':
            #     if letter in {'1', '2'}:
            #         nfa.current_state = 'SDG'
            #     else:
            #         nfa.current_state = 'TDK'

            # elif current_penjurusan == 'J4':
            #     if letter in {'1', '2'}:
            #         nfa.current_state = 'MI'
            #     else:
            #         nfa.current_state = 'TDK'

            # # elif current_penjurusan == 'J5':
            # #     tambahkan transisi

        elif nfa.current_state == 'MI':
            if current_penjurusan == 'J1':
                if letter in {'1', '2'}:
                    nfa.current_state = 'SD'
                else:
                    nfa.current_state = 'TDK'

            elif current_penjurusan == 'J2':
                if letter in {'1', '2'}:
                    nfa.current_state = 'SD'
                else:
                    nfa.current_state = 'TDK'

            # elif current_penjurusan == 'J3':
            #     #Tambahkan transisi
                
            elif current_penjurusan == 'J4':
                if letter in {'1', '2'}:
                    nfa.current_state = 'SD'
                else:
                    nfa.current_state = 'TDK'

            elif current_penjurusan == 'J5':
                if letter in {'1', '2'}:
                    nfa.current_state = 'MD2'
                else:
                    nfa.current_state = 'TDK'
        
        elif nfa.current_state == 'SD':
            if current_penjurusan == 'J1':
                if letter in {'1', '2'}:
                    nfa.current_state = 'MD1'
                else:
                    nfa.current_state = 'TDK'
            
            elif current_penjurusan == 'J2':
                if letter in {'1', '2'}:
                    nfa.current_state = 'DAA'
                else:
                    nfa.current_state = 'TDK'

            # elif current_penjurusan == 'J3':
            #     print("WID")

            elif current_penjurusan == 'J4':
                if letter in {'1', '2'}:
                    nfa.current_state = 'SO'
                else:
                    nfa.current_state = 'TDK'

            # # elif current_penjurusan == 'J5':
            # #     print("WID")

        elif nfa.current_state == 'SO':
            if current_penjurusan == 'J4':
                if letter in {'1', '2'}:
                    nfa.current_state = 'ACC'
                else:
                    nfa.current_state = 'TDK'
            if current_penjurusan == 'J5':
                if letter in {'1', '2'}:
                    nfa.current_state = 'ACC'
                else:
                    nfa.current_state = 'TDK'

#Penjaluran 5
        elif nfa.current_state == "J5": # State sekarang adalah j1
            current_penjurusan = 'J5'
            if letter == '5':
                nfa.current_state = 'ALP'

        elif nfa.current_state == 'ALP': # State sekarang adalah ALP
               if current_penjurusan in {'J1', 'J2', 'J3', 'J4', 'J5'}:  # Penjaluran yang di ambil adalah J1
                   if letter in {'1', '2', '3'}: #nilai A, B+, B diubah menjadi 1, 2, 3
                       if current_penjurusan == 'J1':
                           nfa.current_state = 'TBO'
                       elif current_penjurusan == 'J2':
                           nfa.current_state = 'RPL'
                       elif current_penjurusan == 'J3':
                           nfa.current_state = 'MI'
                       elif current_penjurusan == 'J4':
                           nfa.current_state = 'SDG'
                       elif current_penjurusan == 'J5':
                           nfa.current_state = 'KDJK'
                   else:
                       nfa.current_state = 'TDK'

        elif nfa.current_state == 'KDJK': # State sekarang adalah KDJK
            if letter == '1':
                nfa.current_state = 'RPL'
            else:
                nfa.current_state = 'P/S'

        elif nfa.current_state == 'RPL': # State sekarang adalah RPL
            if current_penjurusan == 'J5':
                if letter in {'1', '2'}:
                    nfa.current_state = 'MI'
                else:
                    nfa.current_state = 'TDK'

        elif nfa.current_state == 'MI':
            if current_penjurusan == 'J1':
                if letter in {'1', '2'}:
                    nfa.current_state = 'SD'
                else:
                    nfa.current_state = 'TDK'

            elif current_penjurusan == 'J2':
                if letter in {'1', '2'}:
                    nfa.current_state = 'SD'
                else:
                    nfa.current_state = 'TDK'

            # elif current_penjurusan == 'J3':
            #     #Tambahkan transisi
                
            elif current_penjurusan == 'J4':
                if letter in {'1', '2'}:
                    nfa.current_state = 'SD'
                else:
                    nfa.current_state = 'TDK'

            elif current_penjurusan == 'J5':
                if letter in {'1', '2'}:
                    nfa.current_state = 'MD2'
                else:
                    nfa.current_state = 'TDK'
        
        elif nfa.current_state == 'MD2':
            if current_penjurusan == 'J5':
                if letter in {'1', '2'}:
                    nfa.current_state = 'SO'
                else:
                    nfa.current_state = 'TDK'

        elif nfa.current_state == 'SO':
            if current_penjurusan == 'J5':
                if letter in {'1', '2'}:
                    nfa.current_state = 'ACC'
                else:
                    nfa.current_state = 'TDK'
            if current_penjurusan == 'J4':
                if letter in {'1', '2'}:
                    nfa.current_state = 'ACC'
                else:
                    nfa.current_state = 'TDK'

        elif nfa.current_state == 'P/S':
            if letter == 'T':
                nfa.current_state = 'TDK'
            if current_penjurusan in {'J1', 'J2', 'J3', 'J4'}:
                if letter == 'Y':
                    nfa.current_state = 'BD'
            else:
                if letter == 'Y':
                    nfa.current_state = 'RPL'
                    
        elif nfa.current_state == 'P/S':
            if letter == 'T':
                nfa.current_state = 'TDK'
            if current_penjurusan in {'J1', 'J2', 'J3', 'J4'}:
                if letter == 'Y':
                    nfa.current_state = 'BD'
            else:
                if letter == 'Y':
                    nfa.current_state = 'RPL'
        print(f"Transition: {current_penjurusan} -> {nfa.current_state}")

    print(f"Final State: {nfa.current_state}")
        
    if nfa.current_state == 'ACC':
        return True
    elif nfa.current_state == 'TDK':
        return False
    else:
        return None
    

    
#MENGUJI    
a = NFA()
a.addFinalState("ACC")
string = "3322Y2111" 
if automata(a, string) == True:
    print("Terima")
elif automata(a, string) == False:
    print("Tolak")
else:
    print("Input Illegal Wak")