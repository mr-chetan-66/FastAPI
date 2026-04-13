import {Wrapper} from "./Wrapper";
import "./Orders.css";
import {useEffect, useState} from "react";
import {Link} from "react-router-dom";

export const Orders = () => {

    const [id, setId] = useState("");
    const [quantity, setQuantity] = useState("");
    const [message, setMessage] = useState("Buy your favorite product");

    useEffect(() => {
        (async () => {
            try {
                if (id) {
                    const response = await fetch(`http://localhost:8000/products/${id}`);
                    const content = await response.json();

                    // multiply price just like your logic
                    const price = parseFloat(content.price) * 1.2;

                    setMessage(`Your product price is $${price}`);
                }
            } catch (e) {
                setMessage("Product not found");
            }
        })();
    }, [id]);

    const submitOrder = (e) => {
        e.preventDefault();
        alert("Order placed!");
    };

    return (
        <Wrapper>

            <div className="order-header">
                <h2>Checkout Form</h2>
                <Link to="/" className="btn-back">← Back</Link>
            </div>

            <h1 className="order-banner">Buy your favorite product</h1>

            <form className="order-form" onSubmit={submitOrder}>

                <div className="form-group">
                    <label>Product ID</label>
                    <input
                        type="number"
                        name="productId"
                        className="input-box"
                        placeholder="Enter product ID"
                        value={id}
                        onChange={(e) => setId(e.target.value)}
                    />
                </div>

                <div className="form-group">
                    <label>Quantity</label>
                    <input
                        type="number"
                        name="quantity"
                        className="input-box"
                        placeholder="Enter quantity"
                        value={quantity}
                        onChange={(e) => setQuantity(e.target.value)}
                    />
                </div>

                <button className="submit-btn" type="submit">Buy</button>
            </form>

            {/* ✅ PRICE MESSAGE DISPLAYED BELOW FORM */}
            <div className="price-box">
                {message}
            </div>

        </Wrapper>
    );
};