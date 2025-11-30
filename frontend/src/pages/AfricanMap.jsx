// AfricaMap.jsx
import React from 'react';
import { ReactComponent as AfricaMap } from '../assets/africaMap.svg';

export default function AfricaInteractive() {

    const handleCountryClick = (e) => {
        const countryCode = e.target.id;
        if (!countryCode) return;
        console.log("Clicked:", countryCode);
        // Fetch your API: /countries/{countryCode}
    };

    return (
        <div className="w-full h-[600px] flex justify-center" style={{ width: '800px', height: '600px' }}>
            <AfricaMap onClick={handleCountryClick} className="cursor-pointer" />
        </div>
    );
}