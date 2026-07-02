# Title
st.title("Shopping Cart Total Calculator")

st.subheader("Enter Item Details")

# Shirt details
shirt_price = st.number_input(
    "Price of Shirt (INR)", min_value=0.0, step=1.0
)
shirt_quantity = st.number_input(
    "Quantity of Shirts (PCS)", min_value=0, step=1
)

# Saree details
saree_price = st.number_input(
    "Price of Saree (INR)", min_value=0.0, step=1.0
)
saree_quantity = st.number_input(
    "Quantity of Sarees (PCS)", min_value=0, step=1
)

# Pant details
pant_price = st.number_input(
    "Price of Pant (INR)", min_value=0.0, step=1.0
)
pant_quantity = st.number_input(
    "Quantity of Pants (PCS)", min_value=0, step=1
)

# Calculate button
if st.button("Calculate Total"):
    total_cost = (
        (shirt_price * shirt_quantity)
        + (saree_price * saree_quantity)
        + (pant_price * pant_quantity)
    )

    total_cost2 = total_cost - (total_cost * 5 / 100)

    st.write(f"**Total before discount:** ₹{total_cost:.2f}")
    st.success(f"**Total after 5% discount:** ₹{total_cost2:.2f}")