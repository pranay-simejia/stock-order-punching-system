import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000'; // Adjust the base URL as needed

export const triggerOrderProcessing = async () => {
    try {
        const response = await axios.post(`${API_BASE_URL}/api/process-orders`);
        return response.data;
    } catch (error) {
        throw new Error(`Error triggering order processing: ${error.message}`);
    }
};

export const fetchOrderStatus = async (clientId) => {
    try {
        const response = await axios.get(`${API_BASE_URL}/api/order-status/${clientId}`);
        return response.data;
    } catch (error) {
        throw new Error(`Error fetching order status for client ${clientId}: ${error.message}`);
    }
};