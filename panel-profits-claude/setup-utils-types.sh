#!/bin/bash

# Create helpers.ts
cat > src/utils/helpers.ts << 'EOL'
export const formatCurrency = (value: number) => {
  // Implement currency formatting
};

export const calculatePercentage = (value: number, total: number) => {
  // Implement percentage calculation
};
EOL

# Create constants.ts
cat > src/utils/constants.ts << 'EOL'
export const API_BASE_URL = 'https://api.example.com';
export const DEFAULT_PAGINATION_LIMIT = 20;
EOL

# Create types.ts
cat > src/utils/types.ts << 'EOL'
export type MarketData = {
  // Define market data types
};

export type TradeOrder = {
  // Define trade order types
};
EOL

# Create market.ts
cat > src/types/market.ts << 'EOL'
export interface Instrument {
  // Define instrument interface
}

export interface Price {
  // Define price interface
}
EOL

# Create trading.ts
cat > src/types/trading.ts << 'EOL'
export interface Order {
  // Define order interface
}

export interface Trade {
  // Define trade interface
}
EOL

# Create portfolio.ts
cat > src/types/portfolio.ts << 'EOL'
export interface Holding {
  // Define holding interface
}

export interface Position {
  // Define position interface
}
EOL

echo "Utility and type files have been created!"
