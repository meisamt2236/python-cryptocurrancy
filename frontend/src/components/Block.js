import React, {useState} from 'react';
import Transaction from './Transaction';
import {Button} from 'react-bootstrap';
import {MILLISECONDS_PY} from '../config';

function ToggleTransactionDisplay({block}) {
    const [displayTransaction, setDisplayTransaction] = useState(false);
    const {data} = block;
    const toggleDisplayTransaction = () => {
        setDisplayTransaction(!displayTransaction);
    }
    if (displayTransaction) {
        return (
            <div>
                {data.map(transaction => (
                    <div key={transaction.id}><hr /><Transaction transaction={transaction}/></div>
                ))}
                <br/>
                <Button variant="info" size="sm" onClick={toggleDisplayTransaction}>Show less</Button>
            </div>
        )
    }
    return (
        <div>
            <br />
            <Button variant="info" size="sm" onClick={toggleDisplayTransaction}>Show more</Button>
        </div>
    )   
}

function Block({block}) {
    const {timestamp, hash} = block;
    const hashDisplay = `${hash.substring(0, 15)}...`;
    const timestampDisplay = new Date(timestamp / MILLISECONDS_PY).toLocaleString();
    return(
        <div className="Block">
            <div>Hash: {hashDisplay}</div>
            <div>Timestamp: {timestampDisplay}</div>
            <ToggleTransactionDisplay block={block} />
        </div>
    )
}

export default Block;