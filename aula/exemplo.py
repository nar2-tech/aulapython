import pyautogui
import time

pyautogui.FAILSAFE = True

# Aguarda o usuário preparar o ambiente
time.sleep(3)

# PASSO 1 - Ativar janela do navegador
pyautogui.click(200, 200)   # clique em uma área do navegador

# PASSO 2 - Digitar a URL
pyautogui.hotkey("ctrl", "l")   # seleciona barra de endereço
time.sleep(0.5)
pyautogui.press("enter")

# Aguarda carregamento
time.sleep(3)

# Digitar termo pesquisado
pyautogui.write("Clima hoje em maceió")
pyautogui.press("enter")

# PASSO 3 - Clicar no campo de pesquisa da Wikipedia
pyautogui.click(600, 350)  # ajuste se necessário

# Aguarda carregar
time.sleep(3)

# PASSO 4 - Screenshot
screenshot = pyautogui.screenshot()
screenshot.save("previsao.png")

print("Automação finalizada com sucesso!")
