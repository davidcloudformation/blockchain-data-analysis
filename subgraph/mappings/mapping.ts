import { Swap } from "../generated/schema"
import { Swap as SwapEvent } from "../generated/Uniswap/Uniswap"
import { BigInt } from "@graphprotocol/graph-ts"

export function handleSwap(event: SwapEvent): void {
  let swap = new Swap(event.transaction.hash.toHex())
  swap.pair = event.params.pair.toHex()
  swap.sender = event.params.sender
  swap.amount0In = event.params.amount0In
  swap.amount1In = event.params.amount1In
  swap.amount0Out = event.params.amount0Out
  swap.amount1Out = event.params.amount1Out
  swap.to = event.params.to
  swap.timestamp = event.block.timestamp
  swap.save()
}