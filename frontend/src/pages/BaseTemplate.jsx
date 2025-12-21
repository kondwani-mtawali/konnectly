/* 
BaseTemplate.jsx - 12/19/2025 -> Create a base template/page to render above every other page
*/

import React from "react";
import { Outlet } from "react-router-dom";

export default function BaseTemplate({ children }) {
  return (
    <>
      {/* Top Bar */}
      <header
        style={{
          position: "fixed",
          top: 0,
          left: 0,
          width: "100vw",
          height: "70px",
          background: "rgba(0, 0, 0, 0.95)",
          backdropFilter: "blur(10px)",
          color: "white",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          zIndex: 1000,
          fontFamily: "system-ui, sans-serif",
        }}
      >
        <h1 style={{
          fontSize: "2.4rem",
          fontWeight: "bold",
          margin: 0,
          letterSpacing: "1px",
        }}>
          Konnectly
        </h1>

      </header>

      {/* Main Content (children or Outlet) */}
      <main style={{ marginTop: "70px", marginBottom: "60px" }}>
        {children || <Outlet />}
      </main>

      {/* Bottom Bar */}
      <footer
        style={{
          position: "fixed",
          bottom: 0,
          left: 0,
          width: "100vw",
          height: "60px",
          background: "rgba(17, 17, 17, 0.95)",
          color: "#aaa",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          fontSize: "1rem",
          fontFamily: "system-ui, sans-serif",
        }}
      >
        Real economic World Bank data | AI-powered investment insights • Updated for 2025
      </footer>
    </>
  );
}