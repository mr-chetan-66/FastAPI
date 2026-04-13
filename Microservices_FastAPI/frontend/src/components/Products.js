import {Wrapper} from "./Wrapper";
import {useState, useEffect} from "react";
import {Link} from 'react-router-dom';
import "./Products.css";

export const Products = () => {

    const [product, setProduct] = useState([]);

    useEffect(() => {
        void (async () => {
            const response = await fetch('http://localhost:8000/products');
            const content = await response.json();
            setProduct(content);
        })();
    }, []);

    const deleteProduct = async (id) => {
        if (window.confirm("Are you really want ot delete this record?")){
            await fetch(`http://localhost:8000/products/${id}`, {
                method: "DELETE"
            });
            setProduct(product.filter(p => p.id !== id));
        }
    };

    return (
        <Wrapper>

            <div className="page-header">
                <h2 style={{margin: 0}}>Products</h2>

                <Link to={'/create'} className="btn-custom">Add Product</Link>
            </div>

            <h1 className="box-title">Product List</h1>

            <div className="table-container">
                <table className="data-table">
                    <thead>
                    <tr>
                        <th>#</th>
                        <th>Name</th>
                        <th>Price</th>
                        <th>Quantity</th>
                        <th>Action</th>
                    </tr>
                    </thead>

                    <tbody>
                    {product.map(product => (
                        <tr key={product.id}>
                            <td>{product.id}</td>
                            <td>{product.name}</td>
                            <td>{product.price}</td>
                            <td>{product.quantity}</td>
                            <td>
                                <button
                                    className="btn-danger"
                                    onClick={() => deleteProduct(product.id)}
                                >
                                    Delete
                                </button>
                            </td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            </div>

        </Wrapper>
    );
};