import tkinter as tk
from tkinter import messagebox
import requests

def obtener_cotizaciones():
    try:
        url = "https://economia.awesomeapi.com.br/json/last/USD-ARS,EUR-ARS,BRL-ARS"
        respuesta = requests.get(url)
        datos = respuesta.json()
        cotizaciones = {
            "USD": float(datos["USDARS"]["bid"]),
            "EUR": float(datos["EURARS"]["bid"]),
            "BRL": float(datos["BRLARS"]["bid"])
        }
        return cotizaciones
    except Exception:
        messagebox.showerror("Error", "Revisa tu internet.")
        return None

def realizar_conversion():
    precios = obtener_cotizaciones()
    if not precios: return
    try:
        monto_pesos = float(entry_pesos.get())
        usd = monto_pesos / precios["USD"]
        eur = monto_pesos / precios["EUR"]
        brl = monto_pesos / precios["BRL"]
        
        lbl_usd.config(text=f"Dólares (USD): ${usd:,.2f}")
        lbl_eur.config(text=f"Euros (EUR): €{eur:,.2f}")
        lbl_brl.config(text=f"Reales (BRL): R${brl:,.2f}")
    except ValueError:
        messagebox.showerror("Error", "Ingresa un número válido.")

ventana = tk.Tk()
ventana.title("Santander - Divisas")
ventana.geometry("400x420")
ventana.config(bg="#ECF0F1")

titulo = tk.Label(ventana, text="CONVERSOR EN VIVO", font=("Arial", 12, "bold"), bg="#ECF0F1", fg="#2C3E50")
titulo.pack(pady=15)

marco = tk.Frame(ventana, bg="#ECF0F1")
marco.pack(pady=10)

lbl_pesos = tk.Label(marco, text="Monto Pesos ($):", font=("Arial", 10), bg="#ECF0F1")
lbl_pesos.pack(side="left")

entry_pesos = tk.Entry(marco, font=("Arial", 10), width=15)
entry_pesos.insert(0, "7000")
entry_pesos.pack(side="right")

btn_cotizar = tk.Button(ventana, text="CONVERTIR", command=realizar_conversion, bg="#E74C3C", fg="white", font=("Arial", 10, "bold"))
btn_cotizar.pack(pady=15)

frame_res = tk.LabelFrame(ventana, text=" Resultados ", font=("Arial", 10), bg="white")
frame_res.pack(fill="x", padx=30, pady=10)

lbl_usd = tk.Label(frame_res, text="Dólares (USD): $0.00", font=("Arial", 10), bg="white")
lbl_usd.pack(fill="x", pady=5)

lbl_eur = tk.Label(frame_res, text="Euros (EUR): €0.00", font=("Arial", 10), bg="white")
lbl_eur.pack(fill="x", pady=5)

lbl_brl = tk.Label(frame_res, text="Reales (BRL): R$0.00", font=("Arial", 10), bg="white")
lbl_brl.pack(fill="x", pady=5)

ventana.mainloop()


