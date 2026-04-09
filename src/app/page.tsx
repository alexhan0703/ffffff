'use client';

import { useState, useEffect } from 'react';
import confetti from 'canvas-confetti';

export default function CounterPage() {
  const [count, setCount] = useState(0);

  const increment = () => {
    const newCount = count + 1;
    setCount(newCount);

    if (newCount === 10) {
      fireworks();
    }
  };

  const fireworks = () => {
    const duration = 3 * 1000;
    const end = Date.now() + duration;

    (function frame() {
      confetti({
        particleCount: 5,
        angle: 60,
        spread: 55,
        origin: { x: 0 },
        colors: ['#ff0000', '#ffa500', '#ffff00', '#008000', '#0000ff', '#4b0082', '#ee82ee']
      });
      confetti({
        particleCount: 5,
        angle: 120,
        spread: 55,
        origin: { x: 1 },
        colors: ['#ff0000', '#ffa500', '#ffff00', '#008000', '#0000ff', '#4b0082', '#ee82ee']
      });

      if (Date.now() < end) {
        requestAnimationFrame(frame);
      }
    }());
  };

  return (
    <div className="container">
      <h1>{count}</h1>
      <button onClick={increment}>눌러보세요!</button>
      {count >= 10 && <div className="message">축하합니다! 10을 달성했어요! 🎉</div>}

      <style jsx>{`
        .container {
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          height: 100vh;
          font-family: 'Pretendard', sans-serif;
          background-color: #f0f2f5;
        }
        h1 {
          font-size: 3rem;
          color: #333;
          margin-bottom: 1rem;
        }
        button {
          padding: 15px 30px;
          font-size: 1.25rem;
          cursor: pointer;
          background-color: #007bff;
          color: white;
          border: none;
          border-radius: 10px;
          transition: transform 0.1s, background-color 0.2s;
        }
        button:hover {
          background-color: #0056b3;
        }
        button:active {
          transform: scale(0.95);
        }
        .message {
          margin-top: 1rem;
          font-weight: bold;
          color: #28a745;
          font-size: 1.2rem;
        }
      `}</style>
    </div>
  );
}
