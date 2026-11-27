import streamlit as st
import pandas as pd

st.set_page_config(page_title="პირადი ბიუჯეტის ტრეკერი", page_icon="💰", layout="centered")

st.title("💰 პირადი ბიუჯეტის ტრეკერი")
st.caption("ინტერაქტიული ვებ-აპლიკაცია ყოველდღიური ხარჯების აღრიცხვისთვის")

if "expenses" not in st.session_state:
    st.session_state.expenses = []

with st.sidebar:
    st.header("➕ ახალი ხარჯის დამატება")
    
    name = st.text_input("ხარჯის დასახელება", placeholder="მაგ: ყავა, სადილი...")
    amount = st.number_input("თანხა (₾)", min_value=0.0, step=0.5, format="%.2f")
    category = st.selectbox("კატეგორია", ["საკვები", "ტრანსპორტი", "გართობა", "კომუნალური", "სხვა"])
    
    if st.button("დამატება", type="primary", use_container_width=True):
        if name.strip() and amount > 0:
            st.session_state.expenses.append({
                "დასახელება": name.strip(),
                "კატეგორია": category,
                "თანხა (₾)": amount
            })
            st.success("ხარჯი წარმატებით დაემატა!")
        else:
            st.error("გთხოვთ შეიყვანოთ დასახელება და 0-ზე მეტი თანხა.")

    st.divider()
    
    if st.button("🗑️ სიის გასუფთავება", use_container_width=True):
        st.session_state.expenses = []
        st.rerun()

if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)
    
    categories = ["ყველა"] + list(df["კატეგორია"].unique())
    selected_category = st.selectbox("🔍 გაფილტვრა კატეგორიის მიხედვით:", categories)
    
    if selected_category != "ყველა":
        filtered_df = df[df["კატეგორია"] == selected_category]
    else:
        filtered_df = df

    total_amount = filtered_df["თანხა (₾)"].sum()
    st.metric(label=f"ჯამური დანახარჯი ({selected_category})", value=f"{total_amount:.2f} ₾")
    
    st.subheader("📋 ხარჯების სია")
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)
else:
    st.info("ჯერჯერობით ხარჯები არ არის დამატებული. გამოიყენეთ მარცხენა პანელი ახალი ხარჯის ჩასაწერად.")