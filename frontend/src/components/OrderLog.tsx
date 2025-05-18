import React, { useEffect, useState } from 'react';
import { fetchOrderLogs } from '../services/api';

const OrderLog: React.FC = () => {
    const [logs, setLogs] = useState<any[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const getOrderLogs = async () => {
            try {
                const response = await fetchOrderLogs();
                setLogs(response.data);
            } catch (err) {
                setError('Failed to fetch order logs');
            } finally {
                setLoading(false);
            }
        };

        getOrderLogs();
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>{error}</div>;
    }

    return (
        <div>
            <h2>Order Logs</h2>
            <ul>
                {logs.map((log, index) => (
                    <li key={index}>
                        {log.client_id} - {log.stock} - {log.quantity} - {log.status} - {log.message}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default OrderLog;