@Echo Ricordarsi di installare esptools...

@echo --- Elenco Porte ---
@rem https://stackoverflow.com/questions/12090503/listing-available-com-ports-with-python

@python ./ports.py
@echo --------------------

@set porta="COM11"
@rem set esptoolpath="C:\Users\maurizio\esp\esp-idf\components\esptool_py\esptool"
@rem set esptoolpath="C:\msys32\home\maurizio\esp\esp-idf\components\esptool_py\esptool"
@rem set esptoolpath="\\wsl.localhost\Ubuntu-20.04\home\maurizio\esp-idf"
@set esptoolpath="..\esptool"

@rem python %esptoolpath%\esptool.py --chip esp32s2 --port %porta% flash_id
@python %esptoolpath%\esptool.py --chip esp32s2 --port %porta% erase_flash

// Firmware compilato da me
//@python %esptoolpath%\esptool.py --chip esp32s2 --port %porta% -b 460800 --before default_reset --after hard_reset --chip esp32-S2  write_flash --flash_mode dio --flash_size detect --flash_freq 40m 0x1000 bootloader.bin 0x8000 partition-table.bin 0x10000 micropython.bin

// Firmware scaricato su singolo file
@python %esptoolpath%\esptool.py --chip esp32s2 --port %porta% write_flash -z 0x1000 LOLIN_S2_MINI-20220117-v1.18.bin