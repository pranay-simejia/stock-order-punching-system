import React from 'react';

interface ClientSummaryProps {
    clientId: string;
    ordersPlaced: Array<{ stock: string; quantity: number; status: string; message: string }>;
    errors: Array<{ stock: string; reason: string }>;
}

const ClientSummary: React.FC<ClientSummaryProps> = ({ clientId, ordersPlaced, errors }) => {
    return (
        <div className="p-4 border rounded shadow">
            <h2 className="text-xl font-bold">Client Summary: {clientId}</h2>
            <h3 className="mt-4 text-lg">Orders Placed</h3>
            <ul className="list-disc pl-5">
                {ordersPlaced.map((order, index) => (
                    <li key={index}>
                        {order.stock}: {order.quantity} - {order.status} ({order.message})
                    </li>
                ))}
            </ul>
            <h3 className="mt-4 text-lg">Errors</h3>
            <ul className="list-disc pl-5">
                {errors.map((error, index) => (
                    <li key={index}>
                        {error.stock}: {error.reason}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ClientSummary;