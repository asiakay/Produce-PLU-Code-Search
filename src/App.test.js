import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import App from './App';

// Mock the JSON data for testing
jest.mock('./pluData.json', () => [
  { item: 'Apple', plu: '123' },
  { item: 'Banana', plu: '456' },
  { item: 'Orange', plu: '789' },
]);

describe('App', () => {
  test('renders the main title', () => {
    render(<App />);
    const titleElement = screen.getByText('PLU Code Search');
    expect(titleElement).toBeInTheDocument();
  });

  test('allows searching for a produce item and displays PLU code', () => {
    render(<App />);
    
    // Type a search term
    const searchInput = screen.getByPlaceholderText('Enter produce item');
    fireEvent.change(searchInput, { target: { value: 'Apple' } });

    // Click the search button
    const searchButton = screen.getByLabelText('Search');
    fireEvent.click(searchButton);

    // Verify that the PLU code is displayed
    const pluCodeElement = screen.getByText('PLU Code: 123');
    expect(pluCodeElement).toBeInTheDocument();
  });

  test('displays suggestions when typing in the search input', () => {
    render(<App />);
    
    // Type a search term
    const searchInput = screen.getByPlaceholderText('Enter produce item');
    fireEvent.change(searchInput, { target: { value: 'Ap' } });

    // Verify that suggestions are displayed
    const suggestionElement = screen.getByText('Apple');
    expect(suggestionElement).toBeInTheDocument();
  });

  test('handles suggestion click and updates the search input and PLU code', () => {
    render(<App />);
    
    // Type a search term
    const searchInput = screen.getByPlaceholderText('Enter produce item');
    fireEvent.change(searchInput, { target: { value: 'Banana' } });

    // Click a suggestion
    const suggestionElement = screen.getByText('Banana');
    fireEvent.click(suggestionElement);

    // Verify that the search input and PLU code are updated
    expect(searchInput).toHaveValue('Banana');
    const pluCodeElement = screen.getByText('PLU Code: 456');
    expect(pluCodeElement).toBeInTheDocument();
  });
});
