import React from 'react';

const FilterGroup = ({ 
  label, 
  options, 
  value, 
  onChange, 
  type = 'radio', 
  name,
  description 
}) => {
  const handleChange = (optionValue) => {
    onChange(optionValue);
  };

  const handleKeyDown = (e, optionValue) => {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      onChange(optionValue);
    }
  };

  return (
    <fieldset className="filter-group" role="group" aria-labelledby={`${name}-legend`}>
      <legend id={`${name}-legend`} className="filter-legend">
        {label}
      </legend>
      
      {description && (
        <p className="filter-description" id={`${name}-description`}>
          {description}
        </p>
      )}

      <div 
        className="filter-options"
        role={type === 'radio' ? 'radiogroup' : 'group'}
        aria-labelledby={`${name}-legend`}
        aria-describedby={description ? `${name}-description` : undefined}
      >
        {options.map((option, index) => {
          const optionId = `${name}-${index}`;
          const isSelected = value === option;
          
          return (
            <div key={option} className="filter-option">
              <input
                type={type}
                id={optionId}
                name={name}
                value={option}
                checked={isSelected}
                onChange={() => handleChange(option)}
                className="filter-input"
                aria-describedby={`${optionId}-label`}
              />
              <label
                id={`${optionId}-label`}
                htmlFor={optionId}
                className="filter-label"
                tabIndex={-1}
                onKeyDown={(e) => handleKeyDown(e, option)}
              >
                {option}
              </label>
            </div>
          );
        })}
      </div>
    </fieldset>
  );
};

export default FilterGroup;