第一部分 Word2vec 基础

1. [Word2Vec] Distributed Representations of Words and Phrases and their Compositionality (Google 2013)

Google 的 Tomas Mikolov 提出 word2vec 的两篇文章之一，这篇文章更具有综述性质，列举了 NNLM、RNNLM 等诸多词向量模型，但最重要的还是提出了 CBOW 和 Skip-gram 两种 word2vec 的模型结构。虽然词向量的研究早已有之，但不得不说还是 Google 的 word2vec 的提出让词向量重归主流，拉开了整个 embedding 技术发展的序幕。

2. [Word2Vec] Efficient Estimation of Word Representations in Vector Space (Google 2013)

Tomas Mikolov 的另一篇 word2vec 奠基性的文章。相比上一篇的综述，本文更详细的阐述了 Skip-gram 模型的细节，包括模型的具体形式和 Hierarchical Softmax 和 Negative Sampling 两种可行的训练方法。

3. [Word2Vec] Word2vec Parameter Learning Explained (UMich 2016)

虽然 Mikolov 的两篇代表作标志的 word2vec 的诞生，但其中忽略了大量技术细节，如果希望完全读懂 word2vec 的原理和实现方法，比如词向量具体如何抽取，具体的训练过程等，强烈建议大家阅读 UMich Xin Rong 博士的这篇针对 word2vec 的解释性文章。惋惜的是 Xin Rong 博士在完成这篇文章后的第二年就由于飞机事故逝世，在此也致敬并缅怀一下 Xin Rong 博士。

第二部分 Word2vec 的衍生及应用

4. [Item2Vec] Item2Vec-Neural Item Embedding for Collaborative Filtering (Microsoft 2016)

这篇论文是微软将 word2vec 应用于推荐领域的一篇实用性很强的文章。该文的方法简单易用，可以说极大拓展了 word2vec 的应用范围，使其从 NLP 领域直接扩展到推荐、广告、搜索等任何可以生成 sequence 的领域。

5. [Airbnb Embedding] Real-time Personalization using Embeddings for Search Ranking at Airbnb (Airbnb 2018)

Airbnb 的这篇论文是 KDD 2018 的 best paper，在工程领域的影响力很大，也已经有很多人对其进行了解读。简单来说，Airbnb 对其用户和房源进行 embedding 之后，将其应用于搜索推荐系统，获得了实效性和准确度的较大提升。文中的重点在于 embedding 方法与业务模式的结合，可以说是一篇应用 word2vec 思想于公司业务的典范。