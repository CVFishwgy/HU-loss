import torch
form fl import flpc()
from sl import sls
weight1= torch.tensor(flpc().s,flpc().b)
weight2= torch.tensor(flpc().s*sls())
class HULoss(torch.nn.Module):
    def __init__(self):
        super(HULoss, self).__init__()

    def forward(self, logits, target):
        # logits: [N, C, H, W], target: [N, H, W]
        # loss = sum(-y_i * log(c_i))
        if logits.dim() > 2:
            logits = logits.view(logits.size(0), logits.size(1), -1)  # [N, C, HW]
            logits = logits.transpose(1, 2)   # [N, HW, C]
            logits = logits.contiguous().view(-1, logits.size(2))    # [NHW, C]
        target = target.view(-1, 1)    # [NHW，1]

        logits = F.log_softmax(logits, 1)
        logits = logits.gather(1, target)   # [NHW, 1]
        loss = -1 * logits


        loss = loss.mean(weight1,weight2)
        return loss