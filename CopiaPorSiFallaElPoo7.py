from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException,ElementClickInterceptedException,NoSuchElementException
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

def check():
    driver.switch_to.default_content()
    sleep(1)
    driver.find_element(By.XPATH,value='/html/body/app/div/learner/activity-view/div/div/main/div/div[2]/div/a[1]').click()

def Continue():
    driver.switch_to.default_content()
    sleep(1)
    try:
        driver.find_element(By.XPATH,"/html/body/app/div/learner/activity-view/div/div/main/div/div[1]/result-screen/div/div/div/div/div/div/div[3]/p[1]/a").click()
    except:
        pass

def Iniciar_Sesion():   
    driver.find_element(By.XPATH,value='//*[@id="onboarding-header-login-btn"]').click()
    
    driver.find_element(By.XPATH,value='//*[@id="gigya-loginID-56269462240752180"]').send_keys("umb-1034279369")
    driver.find_element(By.XPATH,value='//*[@id="gigya-password-56383998600152700"]').send_keys("umb-1034279369")
    driver.find_element(By.XPATH,value='//*[@id="gigya-login-form"]/div[2]/div[1]/input').click()     
    
def Buscar_tareas():
    driver.implicitly_wait(5)
    #driver.find_element(By.XPATH,value='//*[@id="bundleCollapse-72d1b0f2-345e-4dec-b25d-e8304251e097-ic53a"]/material-container/div/div/div[1]/div[2]/material-tile/div/a').click()
    driver.find_element(By.XPATH,value='//*[@id="bundleCollapse-5be0105e-f858-425f-8a8c-980652b2dad2-ic52a"]/material-container/div/div/div[1]/div[2]/material-tile/div/a').click()

    sleep(3)
    
    #Interchange Fifth Edition Level 3A
    #driver.find_element(By.XPATH,value='//*[@id="gigya-loginID-56269462240752180"]').send_keys("umb-1001204193")
    #driver.find_element(By.XPATH,value='//*[@id="gigya-password-56383998600152700"]').send_keys("umb-1001204193")
    
    prueba = driver.find_elements(By.TAG_NAME,value='a')
    #AGREGAR LA FUNCION DE ELEGIR QUE MODULO
    
    x = input("joce")
    # for element in prueba:
    #  qid_attribute = element.get_attribute("qid")
    #  if qid_attribute == "productView-5-7-1-4":
    #  #if qid_attribute == "productView-5-0-1-2":
    #         element.click()
    #         break
    
    sleep(3)
    
    #tenia iframes por eso no encontraba
    
    #Controlar exepcion por si ya hay elementos digitados en siguiente    
def Tarea_Escribir():
    driver.execute_script("window.open(window.location.href);")
    sleep(1)
    ventanas = driver.window_handles 
    driver.switch_to.window(ventanas[0])
    
    iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
    driver.switch_to.frame(iframe)  
    
    inputs = driver.find_elements(By.TAG_NAME,value='input')
    try:        
        for element in inputs:
            element.send_keys("1")
    except ElementNotInteractableException:
        pass
    
    check()
        
    iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
    driver.switch_to.frame(iframe)  
    
    sleep(1)
    try:
        driver.find_element(By.XPATH,value='//*[@id="feedback-text-info__close"]').click()
    except:
        pass
    
    inputs = driver.find_elements(By.CSS_SELECTOR,value='div.check.wrong.has-feedback') 
    correctas = []

    body = driver.find_element(By.TAG_NAME,value='body')
    sleep(1)
    
    for element in inputs:
    #Actividad productView-5-10-0-0 medulo 11
        try:
            element.click()
        except ElementClickInterceptedException:
            body.click()
            body.send_keys(Keys.HOME)
            try:
                driver.find_element(By.CLASS_NAME,value="ui-button.ui-widget.ui-state-default").click()
            except:
                pass
            # x = driver.find_element(By.XPATH,value="/html/body/div[3]/div[1]/button")
            # x.click() 
        finally:
            sleep(0.15)
            try:
             element.click()
            except:
                body.click()
                for _ in range(4):
                    body.send_keys(Keys.ARROW_DOWN)
                sleep(1)
                element.click()
            temp = driver.find_element(By.CSS_SELECTOR, 'div.ui-dialog-content').text.split('\n')
            temp = temp[2]      
        correctas.append(temp)

    driver.close()
    
    sleep(1)
    ventanas = driver.window_handles 
    driver.switch_to.window(ventanas[0])

    iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
    driver.switch_to.frame(iframe)  
        
    inputs = driver.find_elements(By.TAG_NAME,value='input')

    try:        
        for contador,element in enumerate(inputs):
            element.send_keys(correctas[contador])
    except:
        pass
    
    check()
    check()
    Continue()
    
def Tarea_Seleccionar():
    driver.execute_script("window.open(window.location.href);")
    ventanas = driver.window_handles 
    driver.switch_to.window(ventanas[0])
    
    iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
    driver.switch_to.frame(iframe)  
    
    inputs = driver.find_elements(By.CLASS_NAME,value='input-radio')
    body = driver.find_element(By.TAG_NAME,value='body')
    
    try:        
        for element in inputs:
            element.click()
    except ElementClickInterceptedException:
        body.click()
        for _ in range(8):
                body.send_keys(Keys.ARROW_DOWN)   
        sleep(1)
        element.click()
    
    check()
        
    iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
    driver.switch_to.frame(iframe)  
    
    body = driver.find_element(By.TAG_NAME,value='body')
    body.click()
    body.send_keys(Keys.HOME)
    
    sleep(1)
    try:
        driver.find_element(By.XPATH,value='//*[@id="feedback-text-info__close"]').click()
    except:
        pass

    correctas = []

    body = driver.find_element(By.TAG_NAME,value='body')
    inputs = driver.find_elements(By.CSS_SELECTOR,value='.check.has-feedback')
    for element in inputs:
        try:
            element.click() 
            temp = driver.find_element(By.CSS_SELECTOR, 'div.ui-dialog-content').find_element(By.TAG_NAME, 'p').text[26:].strip()
            if temp == "":
                aux = element.find_element(By.XPATH,value='..').find_element(By.TAG_NAME,value="label").text
                temp = aux
            sleep(0.25)
        except ElementClickInterceptedException:
            body = driver.find_element(By.TAG_NAME,value='body')
            body.click()
            for _ in range(8):
                body.send_keys(Keys.ARROW_DOWN)   
            sleep(1)
            element.click()
            sleep(1)
            element.click()    
            temp = driver.find_element(By.CSS_SELECTOR, 'div.ui-dialog-content').find_element(By.TAG_NAME, 'p').text[26:].strip()
            if temp == "":
                aux = element.find_element(By.XPATH,value='..').find_element(By.TAG_NAME,value="label").text
                temp = aux
        except:
            pass
        correctas.append(temp)
    driver.close()
    ventanas = driver.window_handles 
    driver.switch_to.window(ventanas[0])
    
    iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
    driver.switch_to.frame(iframe)  
    
    #digitar respuestas
    
    inputs = driver.find_elements(By.CLASS_NAME,value='is-radiobutton-choice-text')
    cant = len(inputs)/len(correctas)
    contador=0
    contadoraux=True
    print(correctas)
    try:        
        for i,element in enumerate(inputs,1):
            if contadoraux:
                print(element.text,contador,correctas[contador],sep=" , ")
                if element.text == correctas[contador]:
                    try:
                        element.find_element(By.XPATH,value="..").click()
                    except:
                        body = driver.find_element(By.TAG_NAME,value='body')
                        body.click()
                        for _ in range(8):
                            body.send_keys(Keys.ARROW_DOWN)   
                        sleep(1)
                        element.click()
                    contador+=1
                    contadoraux=False
            if (i%cant)==0:
                contadoraux=True
            if contador == len(correctas):
                break
    except ElementNotInteractableException:
        pass
    
    check()
    check()
    Continue()

def Tarea_desplegable():
    driver.execute_script("window.open(window.location.href);")
    ventanas = driver.window_handles 
    driver.switch_to.window(ventanas[0])
    
    iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
    driver.switch_to.frame(iframe)          
    
    inputs = driver.find_elements(By.CLASS_NAME,value="rich-dropdown")
    body = driver.find_element(By.TAG_NAME,value='body')

    for elements in inputs:
        try:    
            elements.click()
            aux = elements.find_element(By.TAG_NAME,value='li').click()
        except:
            body.click()
            for _ in range(8):
                body.send_keys(Keys.ARROW_DOWN)   
            sleep(1)
            elements.click()
            aux = elements.find_element(By.TAG_NAME,value='li').click()

    check()
        
    iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
    driver.switch_to.frame(iframe)  
    
    body = driver.find_element(By.TAG_NAME,value='body')
    body.click()
    body.send_keys(Keys.HOME)
    
    sleep(1)
    driver.find_element(By.XPATH,value='//*[@id="feedback-text-info__close"]').click()

    correctas = []

    inputs = driver.find_elements(By.CSS_SELECTOR,value='.check.has-feedback')
    for element in inputs:
    #Actividad productView-5-10-0-0 medulo 11
        try:
            try:
                element.click()
            except:
                body.click()
                for _ in range(2):
                    body.send_keys(Keys.ARROW_UP)   
            sleep(1) 
            element.click()
            temp = driver.find_element(By.CSS_SELECTOR, 'div.ui-dialog-content').find_element(By.TAG_NAME, 'p').text[26:].strip()
            if temp == "":
                aux = element.find_element(By.XPATH,value='..').find_element(By.CLASS_NAME,value="label.drop-label").text
                temp = aux
            sleep(0.25)
        except ElementClickInterceptedException:
            try:
                driver.find_element(By.CLASS_NAME,value="ui-button.ui-widget.ui-state-default").click()
            except:
                pass
            body = driver.find_element(By.TAG_NAME,value='body')
            body.click()
            for _ in range(8):
                body.send_keys(Keys.ARROW_DOWN)   
            sleep(1)
            try:
                element.click()
            except:
                body.click()
                for _ in range(2):
                 body.send_keys(Keys.ARROW_UP)   
                sleep(1)
                element.click()
            temp = driver.find_element(By.CSS_SELECTOR, 'div.ui-dialog-content').find_element(By.TAG_NAME, 'p').text[26:].strip()
            if temp == "":
                aux = element.find_element(By.XPATH,value='..').find_element(By.CLASS_NAME,value="label.drop-label").text
                temp = aux
                
        except:
            pass
        correctas.append(temp)
        
    driver.close()
    ventanas = driver.window_handles 
    driver.switch_to.window(ventanas[0])

    iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
    driver.switch_to.frame(iframe)
    
    inputs = driver.find_elements(By.CLASS_NAME,value="rich-dropdown")
    contador=0
    
    body = driver.find_element(By.TAG_NAME,value='body')
    
    for elements in inputs:
        try:   
            elements.click()
        except:
            body.click()
            for _ in range(8):
                body.send_keys(Keys.ARROW_DOWN)   
            sleep(2)
            elements.click()
    
        finally:
            aux = elements.find_elements(By.TAG_NAME,value='li')
            for element in aux:
                if element.text == correctas[contador]:
                    element.click()
            contador+=1
            
    check()
    check()    
    Continue()
    
def Tarea_DragAndDrop():
    driver.execute_script("window.open(window.location.href);")
    sleep(2)
    ventanas = driver.window_handles 
    driver.switch_to.window(ventanas[0])
    
    iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
    driver.switch_to.frame(iframe)          
    
    inputs = driver.find_elements(By.CLASS_NAME,value="drop_area.has_drag.gap_match_gap_text_view")
    
    sleep(1)
    
    for elements in inputs:
        elements.click()
        
    check()
    sleep(1)
    
    iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
    driver.switch_to.frame(iframe)  
    
    sleep(1)
    driver.find_element(By.XPATH,value='//*[@id="feedback-text-info__close"]').click()
    
    correctas = []

    body = driver.find_element(By.TAG_NAME,value='body')
    inputs = driver.find_elements(By.CSS_SELECTOR,value='.check.has-feedback')

    for element in inputs:
        try:
            element.click() 
            temp = driver.find_element(By.CSS_SELECTOR, 'div.ui-dialog-content').find_element(By.TAG_NAME, 'p').text[26:].strip()
            if temp == "":
                aux = element.find_element(By.XPATH,value='..').find_element(By.CLASS_NAME,value="content").text
                temp = aux
            sleep(0.25)
        except ElementClickInterceptedException:
            try:
                driver.find_element(By.CLASS_NAME,value="ui-button.ui-widget.ui-state-default").click()
            except:
                pass
            sleep(0.25)
            try:
             element.click()    
            except ElementClickInterceptedException:
                body.click()
                for i in range(4):
                  body.send_keys(Keys.ARROW_DOWN)
                sleep(1)
                element.click()
            finally:
                temp = driver.find_element(By.CSS_SELECTOR, 'div.ui-dialog-content').find_element(By.TAG_NAME, 'p').text[26:].strip()
                if temp == "":
                    aux = element.find_element(By.XPATH,value='..').find_element(By.CLASS_NAME,value="content").text
                    temp = aux
        except NoSuchElementException:
            pass
        correctas.append(temp)
        
    print(correctas)  
    driver.close()
    
    ventanas = driver.window_handles 
    driver.switch_to.window(ventanas[0])

    iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
    driver.switch_to.frame(iframe)
    
    inputs = driver.find_elements(By.CLASS_NAME,'drop_area.gap_match_gap_text_view.has_drag')    
    
    contador=0
    while(contador < len(correctas)):    
        for elements in inputs:
            aux = elements.text.strip()
            try:
                if aux.lower() == correctas[contador].lower():
                    elements.click()
                    contador+=1
            except:
                break
    check()
    check()
    Continue()
    
def Tarea_DragAndDrop2():
    driver.execute_script("window.open(window.location.href);")
    sleep(1)
    ventanas = driver.window_handles 
    driver.switch_to.window(ventanas[0])
    
    iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
    driver.switch_to.frame(iframe)
    
    inputs = driver.find_elements(By.CLASS_NAME,value="pool.ui-droppable")
    
    correctas = []

    for i in range(len(inputs)):
        zone = driver.find_elements(By.CLASS_NAME,value="pool.ui-droppable")
        zone = zone[i].find_elements(By.CLASS_NAME,'drag_element.gap_match_drag.image-between-text')
        
        opciones = []
        for elements in zone:
         opcion = elements.find_element(By.CLASS_NAME,'content').text
         opcion = opcion.lower()
         opciones.append(opcion)
        
        for i,elements in enumerate(zone,1):
            if i%2==0:
                elements.click()
        
        check()
        
        iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
        driver.switch_to.frame(iframe)  
        
        try:
            driver.find_element(By.XPATH,value='//*[@id="feedback-text-info__close"]').click()
        except:
            pass

        cadena = driver.find_element(By.CLASS_NAME, 'ui-draggable.ui-draggable-handle').find_element(By.TAG_NAME, 'p').text[26:].strip()   
        cadena = cadena.lower()
            
        if "," in opciones:   
         cadena = cadena.replace(",", " ,")
         
        if "'" in cadena:
            cadena = cadena.replace("'", "’")
            
        opciones = [element.replace("'", "’") for element in opciones]
        
        print(cadena)
        print(opciones)
        
        N_cadena = [] 
        palabras = cadena.split()
        
        aux = ""
        
        for palabra in palabras:
            aux += palabra + " "    

            if aux.strip() in opciones:
                opciones.remove(aux.strip())
                N_cadena.append(aux.strip()) 
                aux = ""

        if aux.strip():
            N_cadena.append(aux.strip()[:-1])

        for respuestas in N_cadena:
            correctas.append(respuestas)

        check()
        iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
        driver.switch_to.frame(iframe)
    driver.close()
    
    ventanas = driver.window_handles 
    driver.switch_to.window(ventanas[0])

    iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
    driver.switch_to.frame(iframe)
    
    inputs = driver.find_elements(By.CLASS_NAME,value="pool.ui-droppable")
    
    contador,contadoraux = 0,0
    print(correctas)
    
    for i in range(len(inputs)):
        a=True
        zone = driver.find_elements(By.CLASS_NAME,value="pool.ui-droppable")
        zone = zone[i].find_elements(By.CLASS_NAME,'drag_element.gap_match_drag.image-between-text')
        while(a):    
            for i,elements in enumerate(zone,1):
                try:
                    label = elements.find_element(By.CLASS_NAME,'content').text
                    label = label.lower()
                    if "'" in label:
                      label = label.replace("'", "’")
                except:
                    pass
                try:
                    # print(label, correctas[contador])
                    if label == correctas[contador]:
                        elements.click()
                        contador+=1
                        contadoraux+=1
                        if contadoraux == len(zone)/2:
                            contadoraux=0
                            check()
                            check()
                            a = False
                            iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
                            driver.switch_to.frame(iframe)  
                except IndexError:
                    Continue()
# def checkbox():
#     driver.execute_script("window.open(window.location.href);")
#     sleep(1)
#     ventanas = driver.window_handles 
#     driver.switch_to.window(ventanas[0])
    
#     iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
#     driver.switch_to.frame(iframe)
    
#     inputs = driver.find_elements(By.CLASS_NAME,value="is-checkbox-choice-text")
#     body = driver.find_element(By.TAG_NAME,value='body')
    
#     for element in inputs:
#         try:
#             element.click()
#         except:
#             pass

#     check()
        
#     iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
#     driver.switch_to.frame(iframe)  
    
#     sleep(1)
#     try:
#         driver.find_element(By.XPATH,value='//*[@id="feedback-text-info__close"]').click()
#     except:
#         pass
    
#     correctas = []

#     body = driver.find_element(By.TAG_NAME,value='body')
    
#     cantidadDivisiones = len(driver.find_elements(By.CLASS_NAME,value="choice_interaction.algn-ver.has-input"))
#     cantidadOpciones = len(driver.find_elements(By.CLASS_NAME,value="is-checkbox-choice-text"))
#     cantidadXdivision = cantidadOpciones/cantidadDivisiones
    
#     inputs = driver.find_elements(By.CSS_SELECTOR,value='.check.has-feedback')
#     print("????",len(inputs))
#     body.click()
#     body.send_keys(Keys.HOME)
#     sleep(1)
    
#     for element in inputs:
#         try:
#             element.click()
#             temp = driver.find_element(By.CSS_SELECTOR, 'div.ui-dialog-content').find_element(By.TAG_NAME, 'p').text[26:].strip()
#             if temp == "":
#                 aux = element.find_element(By.XPATH,value='..').text
#                 temp = aux
#             sleep(0.25)
#         except ElementClickInterceptedException:
#             try:
#                 driver.find_element(By.CLASS_NAME,value="ui-button.ui-widget.ui-state-default").click()
#             except:
#                 pass
#             sleep(0.25)
#             try:
#              element.click()    
#             except ElementClickInterceptedException:
#                 body.click()
#                 for i in range(4):
#                   body.send_keys(Keys.ARROW_DOWN)
#                 sleep(1)
#                 element.click()
#             finally:
#                 temp = driver.find_element(By.CSS_SELECTOR, 'div.ui-dialog-content').find_element(By.TAG_NAME, 'p').text[26:].strip()
#                 if temp == "":
#                     aux = element.find_element(By.XPATH,value='..').text
#                     temp = aux
#         except NoSuchElementException:
#             pass
#         correctas.append(temp)
        
#     print(correctas)


def Inicio():
    driver.get("https://www.cambridgeone.org")
    
    driver.maximize_window()
    driver.implicitly_wait(10)
    
    Iniciar_Sesion()
    Buscar_tareas()

def Tareas():            
    
    if (inputs := driver.find_elements(By.CLASS_NAME, "input-text.has-input")):
        Tarea_Escribir() 
            
    elif(dragAndDrop := driver.find_elements(By.CLASS_NAME,"pool.ui-droppable")) and len(dragAndDrop) == 1: 
        Tarea_DragAndDrop()
        
    elif(dragAndDrop2 := driver.find_elements(By.CLASS_NAME,"pool.ui-droppable")) and len(dragAndDrop2) > 1: 
        Tarea_DragAndDrop2()
        #prueba = input("darganddrop")
            
    elif(desplegar := driver.find_elements(By.CLASS_NAME,"rich-dropdown")): 
        Tarea_desplegable()
        
    elif(desplegar2 := driver.find_elements(By.CLASS_NAME,"rich-dropdown"))and len(desplegar2) > 1: 
        prueba = input("desplegable2")
        
    elif(Checkbox := driver.find_elements(By.CLASS_NAME,"input-checkbox")): 
        #checkbox();
        prueba = input("Checkbox")
        
    elif(seleccionar := driver.find_elements(By.CLASS_NAME,"contentblock.alignment-vertical")) and len(seleccionar) == 1: 
        Tarea_Seleccionar()    
            
    elif(seleccionar2 := driver.find_elements(By.CLASS_NAME,"contentblock.alignment-vertical")) and len(seleccionar2) > 1: 
            prueba = input("Seleccionar2")
        
    else:
        print("no entro a ninguna")
            
    # while(True):
    #     pass contentblock alignment-vertical

Inicio()
contador = 0
while(True):
    try:
        iframe = driver.find_elements(By.TAG_NAME,'iframe')[0]
        driver.switch_to.frame(iframe)
    except Exception as e:
        print("exept extraño",e)
        pass
    contador+=1
    print(f"it : {contador}")
    try:
     Tareas()
    except Exception as e:
        print(e)
        input("error del try catch inicial")
    sleep(1)



