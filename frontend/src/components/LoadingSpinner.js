import React from 'react';

const LoadingSpinner = () => {
  return (
    <div className="loading-spinner" role="status" aria-live="polite">
      <div className="spinner" aria-hidden="true"></div>
      <p className="loading-text">Processing your request...</p>
    </div>
  );
};

export default LoadingSpinner;