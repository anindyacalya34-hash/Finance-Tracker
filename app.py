import streamlit as st

st.title("💰 Finance Tracker")

# Menggunakan input angka yang rapi
i = st.number_input("Masukkan pemasukan bulan ini:", min_value=0, step=1000)
e = st.number_input("Masukkan pengeluaran bulan ini:", min_value=0, step=1000)

if st.button("Hitung Alokasi"):
    # Rumus
    n = i * 0.5 # Kebutuhan
    w = i * 0.3 # Keinginan
    s = i * 0.2 # Tabungan
    b = i - e   # Saldo

    # Tampilan Hasil
    st.subheader("Hasil Analisis:")
    st.write(f"🏠 Alokasi Kebutuhan (50%): Rp{n:,.0f}")
    st.write(f"🎨 Alokasi Keinginan (30%): Rp{w:,.0f}")
    st.write(f"🏦 Alokasi Tabungan (20%): Rp{s:,.0f}")
    st.divider()
    st.write(f"💵 Sisa Saldo Anda: **Rp{b:,.0f}**")

    # Logika if-else
    if b > 500000:
        st.success("Saldo aman! ✅")
    else:
        st.warning("Harus hemat!! ⚠️")