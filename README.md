# German Question Generation

This projects explores Question Generation in German. We train several Transformer-based machine learning 
models from the [T5 architecture](https://arxiv.org/abs/1910.10683). We open source two models on the Huggingface 
[model hub](https://huggingface.co/dehio).

## Question generation task

The task is to generate a question from a textual input where the answer is highlighted with a `<hl>` token and
prepended with `generate question: `.  

Example:

#### Input
```
generate question: Der Monk Sour Drink ist ein somit eine aromatische Überraschung, 
die sowohl <hl>im Sommer wie auch zu Silvester<hl> funktioniert."
```
#### Expected Question
`Zu welchen Gelegenheiten passt der Monk Sour gut?`

## Models

We open source two trained models: [german-qg-t5-quad](https://huggingface.co/dehio/german-qg-t5-quad) 
and [german-qg-t5-drink600](https://huggingface.co/dehio/german-qg-t5-drink600).

### german-qg-t5-quad

Based on [valhalla/t5-base-qg-hl](https://huggingface.co/valhalla/t5-base-qg-hl), which
is trained on the SQuAD dataset to generate English questions. We further
[fine-tuned](experiments/t5-base-pretrained.json) it on the [GermanQUAD](https://www.deepset.ai/germanquad) dataset, which 
contains 13’722 question and answer pairs. 

It achieves a **BLEU-4 score of 11.30** on the GermanQuAD test set (n=2204).  

We also fine-tuned the original t5-base model, which only achieved a BLEU-4 score of 10.12. 

### german-qg-t5-drink600

Based on *german-qg-t5-quad*, but further [fine-tuned](experiments/t5-base-pretrained-drink-600.json) on a dataset of 
603 German question/answer pairs that we annotated on drink receipts from [Mixology](https://mixology.eu/) ("drink600"). 
We have not yet open sourced the dataset, since we do not own copyright on the source material.

It achieves a **BLEU-4 score of 29.80** on the drink600 test set (n=120) and **11.30** on the GermanQUAD test set. 
Thus, fine-tuning on drink600 did not affect performance on GermanQuAD.

In comparison, *german-qg-t5-quad* achieves a BLEU-4 score of **10.76** on the drink600 test set.

# Credits

Both idea and code are partly inspired by [this repository by Suraj Patil](https://github.com/patil-suraj/question_generation)
and from [Hugging Face](https://github.com/huggingface/transformers/blob/master/examples/pytorch/translation/run_translation.py).
The GermanQUAD dataset was created by [deepset](https://www.deepset.ai), as well as the 
[annotation tool](https://github.com/deepset-ai/haystack/tree/master/annotation_tool) that we used.
