#!/usr/bin/python

# draws this shape for a d4
def draw_d4(value: int) -> None:
    print("""
          ;;
        ,;  ;,
       ,;    ;,
      ,;      ;,
     ,;        ;,
    ,;          ;, 
   ,;     {}     ;,
  ,;              ;,
 ,;                ;, 
,;                  ;,
::::::::::::::::::::::
    """.format(value))

# draws this shape for a d6
def draw_d6(value: int) -> None:
    print("""
 ::::::::::::::
 ::          ::  
 ::          ::
 ::    {}    ::
 ::          ::
 ::          ::                
 :::::::::::::: 

    """.format(value))

# draws this shape for a d20
def draw_d20(value: int) -> None:
    # account for single and double digit numbers moving parts of the dice
    if value > 9: # says if the number if greater than 9 print this  
        print("""             
            ,:::,
       ,,,:;  :  ;:,,, 
   ,,,:       :       :,,, 
,,;...........:...........;,,
; ;          ;';          ; ;
;  ;        ;   ;        ;  ;
;   ;      ;     ;      ;   ;
;    ;    ;       ;    ;    ;
;     ;  ;   {}    ;  ;     ;
;      ;:...........:;      ;
;     , ;           ; ,     ;
;   ,'   ;         ;   ',   ;
'';'      ;       ;      ';''
   ''';    ;     ;    ;'''         
       ''':;;   ;;:'''
            ':::' 
    """.format(value))
        
    else: # prints this for any other statement that is not the one above
        print("""             
            ,:::,
       ,,,:;  :  ;:,,, 
   ,,,:       :       :,,, 
,,;...........:...........;,,
; ;          ;';          ; ;
;  ;        ;   ;        ;  ;
;   ;      ;     ;      ;   ;
;    ;    ;       ;    ;    ;
;     ;  ;    {}    ;  ;    ;
;      ;:...........:;      ;
;     , ;           ; ,     ;
;   ,'   ;         ;   ',   ;
'';'      ;       ;      ';''
   ''';    ;     ;    ;'''         
       ''':;;   ;;:'''
            ':::' 
    """.format(value))
