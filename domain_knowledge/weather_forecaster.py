```json
{
    "domain_knowledge/weather_forecaster.py": {
        "content": "
import logging
from typing import List, Dict
from pydantic import BaseModel
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd
from google.cloud import firestore

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WeatherForecaster(BaseModel):
    """
    A class used to forecast weather patterns.

    Attributes:
    ----------
    non_stationary_drift_index : float
        The index of non-stationary drift in the time series data.
    stochastic_regime_switch : bool
        A flag indicating whether to use stochastic regime switch or not.

    Methods:
    -------
    forecast_weather(data: List[Dict]) -> List[float]
        Forecasts the weather pattern based on the given data.
    """

    non_stationary_drift_index: float
    stochastic_regime_switch: bool

    def __init__(self, non_stationary_drift_index: float, stochastic_regime_switch: bool):
        """
        Initializes the WeatherForecaster object.

        Args:
        ----
        non_stationary_drift_index (float): The index of non-stationary drift in the time series data.
        stochastic_regime_switch (bool): A flag indicating whether to use stochastic regime switch or not.
        """
        self.non_stationary_drift_index = non_stationary_drift_index
        self.stochastic_regime_switch = stochastic_regime_switch

    def forecast_weather(self, data: List[Dict]) -> List[float]:
        """
        Forecasts the weather pattern based on the given data.

        Args:
        ----
        data (List[Dict]): A list of dictionaries containing the weather data.

        Returns:
        -------
        List[float]: A list of forecasted weather values.
        """
        try:
            # Convert data to pandas DataFrame
            df = pd.DataFrame(data)

            # Create a random forest regressor model
            model = RandomForestRegressor()

            # Train the model
            model.fit(df.drop('target', axis=1), df['target'])

            # Make predictions
            predictions = model.predict(df.drop('target', axis=1))

            # Calculate the mean squared error
            mse = mean_squared_error(df['target'], predictions)

            # Log the mean squared error
            logger.info(f'Mean squared error: {mse}')

            # Return the forecasted weather values
            return predictions.tolist()

        except Exception as e:
            # Log the error
            logger.error(f'Error forecasting weather: {str(e)}')

            # Return an empty list
            return []

    def save_to_firestore(self, data: List[Dict]):
        """
        Saves the forecasted weather data to Google Cloud Firestore.

        Args:
        ----
        data (List[Dict]): A list of dictionaries containing the forecasted weather data.
        """
        try:
            # Create a Firestore client
            db = firestore.Client()

            # Create a collection reference
            collection_ref = db.collection('weather_forecasts')

            # Add the data to the collection
            for doc in data:
                collection_ref.add(doc)

            # Log the success
            logger.info('Forecasted weather data saved to Firestore')

        except Exception as e:
            # Log the error
            logger.error(f'Error saving forecasted weather data to Firestore: {str(e)}')

if __name__ == '__main__':
    # Create a WeatherForecaster object
    forecaster = WeatherForecaster(non_stationary_drift_index=0.5, stochastic_regime_switch=True)

    # Create some sample data
    data = [
        {'temperature': 20, 'humidity': 60, 'target': 10},
        {'temperature': 25, 'humidity': 70, 'target': 15},
        {'temperature': 30, 'humidity': 80, 'target': 20}
    ]

    # Forecast the weather
    forecasted_weather = forecaster.forecast_weather(data)

    # Print the forecasted weather
    print(forecasted_weather)

    # Save the forecasted weather data to Firestore
    forecaster.save_to_firestore([{'forecast': value} for value in forecasted_weather])
",
        "commit_message": "feat: implement specialized weather_forecaster logic"
    }
}
```