import React from 'react';

const ErrorMessage = ({ message, onDismiss }) => {
  return (
    <div 
      className="error-message" 
      role="alert" 
      aria-live="assertive"
      aria-labelledby="error-title"
    >
      <div className="error-content">
        <h3 id="error-title" className="error-title">Error</h3>
        <p className="error-text">{message}</p>
        {onDismiss && (
          <button
            className="error-dismiss"
            onClick={onDismiss}
            aria-label="Dismiss error message"
          >
            ×
          </button>
        )}
      </div>
    </div>
  );
};

export default ErrorMessage;