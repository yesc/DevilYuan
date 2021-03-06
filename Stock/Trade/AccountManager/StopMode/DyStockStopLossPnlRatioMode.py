from .DyStockStopMode import *
from ...DyStockTradeCommon import *


class DyStockStopLossPnlRatioMode(DyStockStopMode):
    
    def __init__(self, accountManager, pnlRatio):
        super().__init__(accountManager)

        self._pnlRatio = pnlRatio

    def onTicks(self, ticks):
        for code, pos in self._accountManager.curPos.items():
            tick = ticks.get(code)
            if tick is None:
                continue

            if pos.pnlRatio < self._pnlRatio:
                self._accountManager.closePos(tick.datetime, code, getattr(tick, DyStockTradeCommon.sellPrice), DyStockSellReason.stopLoss, tickOrBar=tick)

    def onBars(self, bars):
        self.onTicks(bars)
