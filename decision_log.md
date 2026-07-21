# Decision Log

## Skylark Business Intelligence Agent

This document outlines the key technical and architectural decisions made during the development of the Skylark Business Intelligence Agent.

---

# 1. Backend Framework

**Decision:** FastAPI

### Reason

- High performance and asynchronous support
- Automatic API documentation using Swagger
- Easy request validation with Pydantic
- Simple REST API development

---

# 2. Frontend Framework

**Decision:** Streamlit

### Reason

- Rapid dashboard development
- Built-in interactive widgets
- Seamless integration with Python
- Suitable for analytics and business intelligence applications

---

# 3. Data Visualization

**Decision:** Plotly

### Reason

- Interactive charts
- Professional appearance
- Easy customization
- Native Streamlit support

---

# 4. Data Source

**Decision:** Monday.com GraphQL API

### Reason

- Direct access to live business data
- Flexible querying
- Reduced unnecessary API calls
- Supports multiple boards efficiently

---

# 5. Project Structure

The project is separated into two independent components:

```
Frontend (Streamlit)
        ↓
FastAPI REST API
        ↓
Analytics Engine
        ↓
Monday.com API
```

### Reason

This separation improves:

- Maintainability
- Scalability
- Testing
- Future deployment flexibility

---

# 6. Business Intelligence Pipeline

The application follows the following workflow:

1. Fetch data from Monday.com
2. Normalize records
3. Validate missing or inconsistent values
4. Generate analytics
5. Produce executive insights
6. Display results on dashboard

---

# 7. KPI Selection

The dashboard includes:

- Total Deals
- Total Work Orders
- Deal Status Distribution
- Work Order Status
- Sector Distribution
- Data Quality Summary

### Reason

These metrics provide a quick overview of business performance while supporting executive decision-making.

---

# 8. Error Handling

Implemented:

- API exception handling
- Empty dataset checks
- Missing field validation
- User-friendly error messages in the frontend

---

# 9. Security

Security measures include:

- Environment variables for API credentials
- Excluding `.env` from version control
- No hardcoded secrets in the repository

---

# 10. User Experience

The dashboard was designed with:

- Modern responsive layout
- KPI cards
- Interactive charts
- Expandable analytics section
- Clean typography
- High-contrast color scheme for readability

---

# 11. Scalability

The architecture supports future enhancements such as:

- Predictive analytics
- AI-powered conversational interface
- Authentication and authorization
- Cloud deployment
- Report export (PDF/Excel)
- Additional business data sources

---

# Challenges Encountered

- Mapping Monday.com GraphQL responses into a consistent structure.
- Handling missing or inconsistent values across boards.
- Improving dashboard readability by refining Plotly chart styling.
- Separating frontend visualization from backend analytics for better maintainability.

---

# Future Improvements

- LLM-powered conversational business assistant
- Real-time dashboard updates
- Advanced forecasting models
- Automated anomaly detection
- Multi-user authentication
- Cloud deployment with CI/CD

---

# Conclusion

The final solution follows a modular architecture with a clear separation between data collection, analytics, and presentation. This design improves maintainability, scalability, and extensibility while delivering a clean and interactive business intelligence dashboard.
