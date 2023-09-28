import React from 'react';

function IframeComponent(props) {
    return (
        <iframe 
            src={props.src} 
            width={props.width || "100%"} 
            height={props.height || "500px"} 
            title={props.title || "Iframe"}
        ></iframe>
    );
}

export default IframeComponent;
