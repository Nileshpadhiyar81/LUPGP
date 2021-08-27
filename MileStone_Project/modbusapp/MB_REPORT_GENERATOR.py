import tkinter as tk
from tkinter import *
import tkinter.messagebox
import easymodbus.modbusClient
import pandas as pd
import time
import datetime
from datetime import datetime


def show_entry_fields():
    IP_ADD = e1.get()
    PORT_NO = int(e2.get())
    STARTING_ADDRESS = int(e3.get())
    LENGTH = int(e4.get())
    DURATION = int(e5.get())


    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)
    e4.delete(0, tk.END)
    e5.delete(0, tk.END)


    # MODBUS CLIENT COMMUNICATION
    modbus_client = easymodbus.modbusClient.ModbusClient(IP_ADD, PORT_NO)

    modbus_client.connect()


    df = pd.DataFrame()
    for dur in range(DURATION):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S:%f")
        D_T = now.strftime("%d_%m_%Y-%H_%M_%S")
        Name_start = STARTING_ADDRESS
        if STARTING_ADDRESS==0:
            holding_registers = modbus_client.read_holdingregisters(Name_start, LENGTH)
        else:
            holding_registers = modbus_client.read_holdingregisters(Name_start - 1, LENGTH)
        keys = ["Time"]
        values = [date_time]

        for i in range(LENGTH):

            val = holding_registers[i]
            values.append(val)
            i = i + 1
            name = 'Register_0%d' % Name_start
            keys.append(name)
            Name_start = Name_start + 1
            continue
        data_withlength_dict = {key: value for key, value in zip(keys, values)}
        print(data_withlength_dict)
        df = df.append([data_withlength_dict], ignore_index=True)
        time.sleep(1)


    report = 'Report Of {}.xlsx'.format(D_T)
    df.to_excel(report, index=False)
    print(df)
    print("file is genrated as report as", report)
    # cols = df.columns.tolist()
    # print(cols)
    modbus_client.close()
    # master.after(DURATION,onClick())
    tk.Label(master, text=f'{report}, Generated!', bg='#ffbf00', pady=2 ).grid(row=6,column=1,sticky =W)


def onClick():
    tkinter.messagebox.showinfo("ABOUT", "This Application Can Read Integer Values From Holding Registers")

master = tk.Tk()
master.geometry('400x300')
master['bg'] = '#ffbf00'
master.title("MB_TCP_REPORTER")
master.resizable(False, False) # to make window nonresizable

tk.Label(master, text="IP ADDRESS: ",  pady=2, bg='#ffbf00').grid(row=0, sticky = W)
tk.Label(master, text="PORT NO: ", pady=2, bg='#ffbf00').grid(row=1, sticky = W)
tk.Label(master, text="STARTING ADDRESS:", pady=2, bg='#ffbf00').grid(row=2, sticky = W)
tk.Label(master, text="LENGTH: ", pady=2, bg='#ffbf00').grid(row=3, sticky = W)
tk.Label(master, text="DURATION(in Sec): ", pady=2, bg='#ffbf00').grid(row=4, sticky = W)


e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)
e5 = tk.Entry(master)


e1.grid(row=0, column=1, ipadx="30", sticky = W)
e2.grid(row=1, column=1, ipadx="30", sticky = W)
e3.grid(row=2, column=1, ipadx="30", sticky = W)
e4.grid(row=3, column=1, ipadx="30", sticky = W)
e5.grid(row=4, column=1, ipadx="30", sticky = W)

tk.Button(master,
          text='Cancle',
          command=master.quit).grid(row=5,
                                    column=1,
                                    sticky=tk.W,
                                    pady=20,padx=70)
tk.Button(master, text='Connect', command=show_entry_fields).grid(row=5,
                                                                  column=1,
                                                                  sticky=tk.W,
                                                                  pady=20)

tk.Button(master, text='Help', command=onClick).grid(row=5,
                                                                  column=1,
                                                                  sticky=tk.W,
                                                                  pady=20,padx=140)

master.mainloop()
