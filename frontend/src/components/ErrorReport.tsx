import React from 'react';

const ErrorReport: React.FC<{ errors: string[] }> = ({ errors }) => {
    return (
        <div className="error-report">
            <h2 className="text-red-600">Error Report</h2>
            {errors.length === 0 ? (
                <p>No errors encountered.</p>
            ) : (
                <ul className="list-disc pl-5">
                    {errors.map((error, index) => (
                        <li key={index} className="text-red-500">
                            {error}
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default ErrorReport;