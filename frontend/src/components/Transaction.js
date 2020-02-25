import React from 'react';

function Transaction({transaction}) {
    const {input, output} = transaction;
    const recipient = Object.keys(output);
    return (
        <div className="Transaction">
            <div key={recipient}>From: {input.address}</div>
            {recipient.map(recipient => (
                <div>To: {recipient} | Sent: {output[recipient]}</div>
            ))}
        </div>
    )
}

export default Transaction;