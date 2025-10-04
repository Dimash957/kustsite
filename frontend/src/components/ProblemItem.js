import React, { useState } from 'react';
import '../styles/ProblemItem.css';

/**
 * ProblemItem Component
 * Individual problem card with expandable details and accessibility features
 */
function ProblemItem({ item, index }) {
  const [isExpanded, setIsExpanded] = useState(false);
  
  const { title, description, severity = 'Medium', source } = item;
  
  const severityClass = `severity-${severity.toLowerCase()}`;
  const itemId = `problem-${index}`;
  const descriptionId = `${itemId}-description`;

  const toggleExpanded = () => {
    setIsExpanded(!isExpanded);
  };

  return (
    <article 
      className={`problem-item ${severityClass}`}
      aria-labelledby={itemId}
    >
      <div className="problem-header">
        <div className="problem-title-group">
          <h3 id={itemId} className="problem-title">
            <span className="problem-number" aria-label={`Challenge ${index + 1}`}>
              {index + 1}.
            </span>
            {title}
          </h3>
          
          <span 
            className={`severity-badge ${severityClass}`}
            aria-label={`Severity: ${severity}`}
          >
            {severity}
          </span>
        </div>

        {description && description.length > 150 && (
          <button
            className="expand-button"
            onClick={toggleExpanded}
            aria-expanded={isExpanded}
            aria-controls={descriptionId}
            aria-label={isExpanded ? 'Show less' : 'Show more'}
          >
            {isExpanded ? 'Show less' : 'Show more'}
          </button>
        )}
      </div>

      <div 
        id={descriptionId}
        className={`problem-description ${isExpanded ? 'expanded' : ''}`}
        aria-hidden={!isExpanded && description && description.length > 150}
      >
        {description ? (
          <p>{description}</p>
        ) : (
          <p className="no-description">
            <em>No detailed description available for this challenge.</em>
          </p>
        )}
      </div>

      {source && (
        <div className="problem-metadata">
          <span className="metadata-label">Source type:</span>
          <span className="metadata-value">{source}</span>
        </div>
      )}
    </article>
  );
}

export default ProblemItem;
