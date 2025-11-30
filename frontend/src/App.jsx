import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import AfricaInteractive from './pages/AfricanMap'


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div className="App">
        <AfricaInteractive />
      </div>
    </>
  );
}

export default App
